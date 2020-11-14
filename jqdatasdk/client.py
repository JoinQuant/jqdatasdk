# coding=utf-8
import platform
import socket
import sys
import threading
import time
import zlib
import requests
from os import path

import msgpack
import thriftpy2 as thriftpy
from pandas.compat import pickle_compat as pc
from thriftpy2 import transport, protocol
from thriftpy2.rpc import make_client
if platform.system().lower() != "windows":
    socket_error = (transport.TTransportException, socket.error, protocol.cybin.ProtocolError)
else:
    socket_error = (transport.TTransportException, socket.error)

from .api import *
from .utils import get_mac_address, is_pandas_version_25, get_pandas_notice

thrift_path = path.join(sys.modules["ROOT_DIR"], "jqdata.thrift")
thrift_path = path.abspath(thrift_path)
module_name = path.splitext(path.basename(thrift_path))[0]
thrift = None
with open(thrift_path) as f:
    thrift = thriftpy.load_fp(f, "jqdata_thrift")

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

    @classmethod
    def instance(cls):
        _instance = getattr(cls._threading_local, '_instance', None)
        if _instance is None:
            if cls._auth_params:
                _instance = JQDataClient(**cls._auth_params)
            cls._threading_local._instance = _instance
        return _instance

    def __init__(self, host, port, username="", password="", token="", version=""):
        self.host = host or self._default_host
        self.port = int(port or self._default_port)
        self.username = username
        self.password = password
        self.token = token
        self.version = version

        assert self.host, "host is required"
        assert self.port, "port is required"
        assert self.username or self.token, "username is required"
        assert self.password or self.token, "password is required"

        self.client = None
        self.inited = False
        self.not_auth = True
        self.compress = True
        self.http_token = ""
        self.data_api_url = ""

    @classmethod
    def set_request_params(cls, **params):
        if "request_timeout" in params:
            request_timeout = params["request_timeout"]
            if not request_timeout:
                cls.request_timeout = None
            else:
                request_timeout = float(request_timeout)
                cls.request_timeout = (
                    request_timeout if request_timeout > 0 else None
                )
            instance = cls.instance()
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
            request_attempt_count = int(params["request_attempt_count"])
            if request_attempt_count > 10:
                raise Exception("请求的尝试次数不能大于 10 次")
            cls.request_attempt_count = request_attempt_count

    @classmethod
    def set_auth_params(cls, **params):
        cls._auth_params = params
        cls.instance().ensure_auth()

    def ensure_auth(self):
        if not self.inited:
            if not self.username and not self.token:
                raise RuntimeError("not inited")
            self.client = make_client(
                thrift.JqDataService,
                self.host,
                self.port,
                timeout=(self.request_timeout * 1000)
            )
            self.inited = True
            if self.username:
                response = self.client.auth(
                    self.username,
                    self.password,
                    self.compress,
                    get_mac_address(),
                    self.version
                )
                self.data_api_url = response.error if response.error else AUTH_API_URL
                self.set_http_token()
            else:
                response = self.client.auth_by_token(self.token)
            auth_message = response.msg
            if not sys.stdout.isatty():
                auth_message = ""
            if not response.status:
                self._threading_local._instance = None
                raise self.get_error(response)
            else:
                if self.not_auth:
                    print("auth success %s" % auth_message)
                    self.not_auth = False

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

    def __call__(self, method, **kwargs):
        kwargs["timeout"] = self.request_timeout
        request = thrift.St_Query_Req()
        request.method_name = method
        request.params = msgpack.packb(kwargs)
        err, result = None, None
        for idx in range(self.request_attempt_count):
            try:
                file = six.BytesIO()
                self.ensure_auth()
                response = self.client.query(request)
                if response.status:
                    buffer = response.msg
                    if six.PY3:
                        if type(buffer) is str:
                            buffer = bytes(buffer, "ascii")
                    buffer = zlib.decompress(buffer)
                    file.write(buffer)
                    pickle_encoding = None
                    if six.PY3:
                        pickle_encoding = "latin1"
                    result = pc.load(file, encoding=pickle_encoding)
                else:
                    err = self.get_error(response)
                break
            except KeyboardInterrupt as e:
                self._reset()
                err = e
                raise
            except socket_error as e:
                self._reset()
                err = e
                if idx < self.request_attempt_count - 1:
                    print("网络错误：'{}', 将进行重试".format(e))
                continue
            except Exception as e:
                self._reset()
                err = e
                break
            finally:
                file.close()

        if result is None:
            if isinstance(err, Exception):
                raise err

        return result

    def __getattr__(self, method):
        return lambda **kwargs: self(method, **kwargs)

    def get_data_api_url(self):
        return self.data_api_url

    def get_http_token(self):
        return self.http_token

    def set_http_token(self):
        body = {
            "method": "get_current_token",
            "mob": self.username,
            "pwd": self.password
        }
        try:
            res = requests.post(
                AUTH_API_URL,
                data=json.dumps(body),
                timeout=cls.request_timeout
            )
            self.http_token = res.text
        except Exception:
            pass
        return self.http_token


class AnalysisDNS(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(AnalysisDNS, self).__init__(*args, **kwargs)
        self.daemon = True

    def run(self):
        try:
            requests.get(AUTH_API_URL, timeout=6)
        except Exception:
            pass
