# coding=utf-8
import platform
import socket
import sys
import threading
import time
import zlib
from os import path

import msgpack
import thriftpy2 as thriftpy
from pandas.compat import pickle_compat as pc
from thriftpy2.protocol import cybin
from thriftpy2.rpc import make_client

from .api import *

thrift_path = path.join(sys.modules["ROOT_DIR"], "jqdata.thrift")
thrift_path = path.abspath(thrift_path)
module_name = path.splitext(path.basename(thrift_path))[0]
thrift = None
with open(thrift_path) as f:
    thrift = thriftpy.load_fp(f, "jqdata_thrift")


class JQDataClient(object):

    _threading_local = threading.local()
    _auth_params = {}

    @classmethod
    def instance(cls):
        _instance = getattr(cls._threading_local, '_instance', None)
        if _instance is None:
            if cls._auth_params:
                _instance = JQDataClient(**cls._auth_params)
            cls._threading_local._instance = _instance
        return _instance

    def __init__(self, host, port, username="", password="", token="", retry_cnt=5):
        assert host, "host is required"
        assert port, "port is required"
        assert username or token, "username is required"
        assert password or token, "password is required"
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.token = token
        self.client = None
        self.inited = False
        self.retry_cnt = retry_cnt
        self.not_auth = True
        self.compress = True

    @classmethod
    def set_auth_params(cls, **params):
        cls._auth_params = params
        cls.instance().ensure_auth()

    def ensure_auth(self):
        if not self.inited:
            if not self.username and not self.token:
                raise RuntimeError("not inited")
            self.client = make_client(thrift.JqDataService, self.host, self.port)
            self.inited = True
            if self.username:
                response = self.client.auth(self.username, self.password, self.compress)
            else:
                response = self.client.auth_by_token(self.token)
            if not response.status:
                self._threading_local._instance = None
                raise self.get_error(response)
            else:
                if self.not_auth:
                    print("auth success %s" % response.msg)
                    self.not_auth = False
        return not self.not_auth

    def _reset(self):
        if self.client:
            self.client.close()
            self.client = None
        self.inited = False

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
        request = thrift.St_Query_Req()
        request.method_name = method
        request.params = msgpack.packb(kwargs)
        err, result = None, None
        for idx in range(self.retry_cnt):
            try:
                self.ensure_auth()
                file = six.BytesIO()
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
            except (thriftpy.transport.TTransportException, socket.error, cybin.ProtocolError) as e:
                self._reset()
                err = e
                time.sleep(idx * 2)
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
