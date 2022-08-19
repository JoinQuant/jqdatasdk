# coding=utf-8

import platform
import time
import socket
import zlib
import threading
import json
import random
import itertools
from os import getenv

import six
import msgpack
import requests
import pandas as pd
from thriftpy2 import transport, protocol
from thriftpy2.rpc import make_client

try:
    from urllib.parse import quote as urlquote
except ImportError:
    from urllib import quote as urlquote

from .utils import classproperty, isatty, get_mac_address
from .version import __version__ as current_version
from .compat import pickle_compat as pc
from .thriftclient import thrift
from .exceptions import ResponseError


if platform.system().lower() != "windows":
    socket_error = (transport.TTransportException, socket.error, protocol.cybin.ProtocolError)
else:
    socket_error = (transport.TTransportException, socket.error)

AUTH_API_URL = "https://dataapi.joinquant.com/apis"  # 获取token


class JQDataClient(object):

    _threading_local = threading.local()
    _auth_params = {}

    _default_host = "39.107.190.114"
    _default_port = 7000

    request_timeout = 300
    request_attempt_count = 3

    @classproperty
    def _local_socket_timeout(cls):
        """本地网络超时时间

        由于网络稍有延迟，将该时间设置为比服务器超时时间略长一点
        否则会有服务端正常处理完，而客户端已超时断开的问题
        """
        return cls.request_timeout + 5

    @staticmethod
    def _get_auth_param_from_env(name):
        for prefix in ["JQDATA", "JQDATASDK"]:
            value = getenv('_'.join([prefix, name]).upper())
            if value:
                return value

    @classmethod
    def _get_username_from_env(cls):
        for name in ["username", "user", "account", "mob"]:
            value = cls._get_auth_param_from_env(name)
            if value:
                return value

    @classmethod
    def _get_password_from_env(cls):
        for name in ["password", "passwd"]:
            value = cls._get_auth_param_from_env(name)
            if value:
                return value

    @classmethod
    def instance(cls):
        _instance = getattr(cls._threading_local, '_instance', None)
        if _instance is None:
            if not cls._auth_params:
                username = cls._get_username_from_env()
                password = cls._get_password_from_env()
                host = cls._get_auth_param_from_env("host")
                port = cls._get_auth_param_from_env("port")
                if username and password:
                    cls._auth_params = {
                        "username": username,
                        "password": password,
                        "host": host or cls._default_host,
                        "port": port or cls._default_port,
                    }
            if cls._auth_params:
                _instance = JQDataClient(**cls._auth_params)
            cls._threading_local._instance = _instance
        return _instance

    def __init__(self, host=None, port=None, username="", password="", token=""):
        self.host = host or self._default_host
        self.port = int(port or self._default_port)
        self.username = username
        self.password = password
        self.token = token

        assert self.host, "host is required"
        assert self.port, "port is required"
        assert self.username or self.token, "username is required"
        assert self.password or self.token, "password is required"

        self.client = None
        self.inited = False
        self.not_auth = True
        self.compress = True
        self.data_api_url = ""
        self._http_token = ""

        self._request_id_generator = itertools.count(
            random.choice(range(0, 1000, 10))
        )

    @classmethod
    def set_request_params(cls, **params):
        if "request_timeout" in params:
            try:
                request_timeout = float(params["request_timeout"])
                if request_timeout < 0:
                    raise ValueError()
            except (TypeError, ValueError):
                raise ValueError("请求的超时时间需要为一个大于等于 0 的数")
            cls.request_timeout = request_timeout
            try:
                instance = cls.instance()
            except Exception:
                instance = None
            if instance and instance.inited and instance.client:
                try:
                    try:
                        sock = instance.client._iprot.trans._trans.sock
                    except AttributeError:
                        sock = instance.client._iprot.trans.sock
                    sock.settimeout(cls.request_timeout)
                except Exception:
                    pass
        if "request_attempt_count" in params:
            try:
                request_attempt_count = int(params["request_attempt_count"])
                if request_attempt_count <= 0 or request_attempt_count > 10:
                    raise ValueError()
            except (TypeError, ValueError):
                raise ValueError("请求的尝试次数需要为一个大于 0 且小于等于 10 的整数")
            cls.request_attempt_count = request_attempt_count

    @classmethod
    def set_auth_params(cls, **params):
        if params != cls._auth_params and cls.instance():
            cls.instance()._reset()
            cls._threading_local._instance = None
        cls._auth_params = params
        cls.instance().ensure_auth()

    def _create_client(self):
        self.client = make_client(
            thrift.JqDataService,
            self.host,
            self.port,
            timeout=(self.request_timeout * 1000)
        )
        return self.client

    def ensure_auth(self):
        if self.inited:
            return

        if not self.username and not self.token:
            raise RuntimeError("not inited")

        self._create_client()
        if self.username:
            error, response = None, None
            for _ in range(self.request_attempt_count):
                try:
                    response = self.client.auth(
                        self.username,
                        self.password,
                        self.compress,
                        get_mac_address(),
                        current_version,
                    )
                    break
                except socket_error as ex:
                    error = ex
                    time.sleep(0.5)
                    self.client.close()
                    self._create_client()
                    continue
            else:
                if error and not response:
                    raise error
            if response and response.error:
                self.data_api_url = response.error
            else:
                self.data_api_url = AUTH_API_URL
        else:
            response = self.client.auth_by_token(self.token)
        auth_message = response.msg
        if not isatty():
            auth_message = ""
        if not response.status:
            self._threading_local._instance = None
            raise self.get_error(response)
        else:
            if self.not_auth:
                print("auth success %s" % auth_message)
                self.not_auth = False
        self.inited = True

    def _reset(self):
        if self.client:
            self.client.close()
            self.client = None
        self.inited = False
        self.http_token = ""

    def logout(self):
        self._reset()
        self._threading_local._instance = None
        self.__class__._auth_params = {}
        print("已退出")

    def get_error(self, response):
        err = None
        if six.PY2:
            system = platform.system().lower()
            if system == "windows":
                err = Exception(response.error.encode("gbk"))
            else:
                err = Exception(response.error.encode("utf-8"))
        else:
            err = Exception(response.error)
        return err

    def query(self, method, params):
        params["timeout"] = self.request_timeout
        params["request_id"] = next(self._request_id_generator)
        request = thrift.St_Query_Req()
        request.method_name = method
        request.params = msgpack.packb(params)
        buffer = six.BytesIO()
        result = None
        try:
            self.ensure_auth()
            response = self.client.query(request)
            if response.status:
                msg = response.msg
                if six.PY3 and isinstance(msg, str):
                    try:
                        msg = msg.encode("ascii")
                    except UnicodeError:
                        raise ResponseError("bad msg {!r}".format(msg))
                msg = zlib.decompress(msg)
                buffer.write(msg)
                pickle_encoding = None
                if six.PY3:
                    pickle_encoding = "latin1"
                result = pc.load(buffer, encoding=pickle_encoding)
            else:
                raise self.get_error(response)
        finally:
            buffer.close()

        if not isinstance(result, dict) or "request_id" not in result:
            return result

        if params["request_id"] != result["request_id"]:
            raise ResponseError("request_id {!r} != {!r}".format(
                params["request_id"], result["request_id"]
            ))
        return result["msg"]

    def _ping_server(self):
        if not self.client or not self.inited:
            return False
        for _ in range(self.request_attempt_count):
            try:
                msg = self.query("ping", {})
            except ResponseError:
                msg = None
                continue
            except Exception:
                return False
        return msg == "pong"

    @classmethod
    def convert_message(cls, msg):
        if isinstance(msg, dict):
            data_type = msg.get("data_type", None)
            data_value = msg.get("data_value", None)
            if data_type is not None and data_value is not None:
                params = data_value
                if data_type.startswith("pandas"):
                    data_index_type = params.pop("index_type", None)
                    if data_index_type == "Index":
                        params["index"] = pd.Index(params["index"])
                    elif data_index_type == "MultiIndex":
                        params["index"] = (
                            pd.MultiIndex.from_tuples(params["index"])
                            if len(params["index"]) > 0 else None
                        )
                    if data_type == "pandas_dataframe":
                        dtypes = params.pop("dtypes", None)
                        msg = pd.DataFrame(**params)
                        if dtypes:
                            msg = msg.astype(dtypes, copy=False)
                    elif data_type == "pandas_series":
                        msg = pd.Series(**params)
            else:
                msg = {
                    key: cls.convert_message(val)
                    for key, val in msg.items()
                }
        return msg

    def __call__(self, method, **kwargs):
        err, result = None, None
        for _ in range(self.request_attempt_count):
            try:
                result = self.query(method, kwargs)
                break
            except socket_error as ex:
                if not self._ping_server():
                    self._reset()
                err = ex
                time.sleep(0.6)
            except ResponseError as ex:
                err = ex

        if result is None and isinstance(err, Exception):
            raise err

        return self.convert_message(result)

    def __getattr__(self, method):
        return lambda **kwargs: self(method, **kwargs)

    def get_data_api_url(self):
        return self.data_api_url

    @property
    def http_token(self):
        if not self._http_token:
            self.set_http_token()
        return self._http_token

    @http_token.setter
    def http_token(self, value):
        self._http_token = value

    @http_token.deleter
    def http_token(self):
        self._http_token = ""

    def set_http_token(self):
        username, password = self.username, self.password
        if not username or not password:
            return
        body = {
            "method": "get_current_token",
            "mob": username,
            "pwd": urlquote(password),  # 给密码编码，防止使用特殊字符登录失败
        }
        headers = {'User-Agent': 'JQDataSDK/{}'.format(current_version)}
        try:
            res = requests.post(
                AUTH_API_URL,
                data=json.dumps(body),
                headers=headers,
                timeout=self.request_timeout
            )
            self._http_token = res.text.strip()
        except Exception:
            pass
        return self._http_token

    def get_http_token(self):
        return self.http_token
