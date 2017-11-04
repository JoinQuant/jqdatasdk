# coding=utf-8
from .utils import *
from .api import *
import thriftpy
from thriftpy.rpc import make_client
import msgpack
import time

from os import path

thrift_path = path.join(path.dirname(__file__), "jqdata.thrift")
thrift = thriftpy.load(thrift_path)


class JQDataClient(object):

    _instance = None

    @classmethod
    def instance(cls):
        assert cls._instance, "请先调用jqdatalite.init初始化"
        return cls._instance

    def __init__(self, host, port, username="", password="", retry_cnt=30):
        assert host, "host不能为空"
        assert port, "port不能为空"
        assert username, "username不能为空"
        assert password, "password不能为空"
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None
        self.inited = False
        self.retry_cnt = retry_cnt
        cls = self.__class__
        cls._instance = self

    def ensure_auth(self):
        if not self.inited:
            if not self.username or self.username == "":
                raise RuntimeError("not inited")
            self.client = make_client(thrift.JqDataService, self.host, self.port)
            self.inited = True
            response = self.client.auth(self.username, self.password)
            if not response.status:
                raise RuntimeError(response.error)
            else:
                print("登录成功")

    def _reset(self):
        if self.client:
            self.client.close()
            self.client = None
        self.inited = False

    def __call__(self, method, **kwargs):
        request = thrift.St_Query_Req()
        request.method_name = method
        request.params = msgpack.packb(kwargs)

        err, result = None, None
        for idx in range(self.retry_cnt):
            try:
                self.ensure_auth()
                response = self.client.query(request)
                if response.status:
                    # buffer = msgpack.unpackb(response.msg)
                    buffer = response.msg
                    if six.PY2:
                        buffer = buffer.encode("utf-8")
                        result = pickle.loads(buffer)
                    else:
                        result = pickle.loads(bytes(buffer, "ascii"), encoding="iso-8859-1")
                else:
                    if six.PY2:
                        err = Exception(response.error.encode("utf-8"))
                    else:
                        err = Exception(response.error)
                break
            except KeyboardInterrupt as e:
                self._reset()
                err = e
                raise
            except OSError as e:
                self._reset()
                err = e
                time.sleep(idx * 2)
                continue
            except Exception as e:
                self._reset()
                err = e
                break

        if result is None:
            if isinstance(err, Exception):
                raise err

        return result

    def __getattr__(self, method):
        return lambda **kwargs: self(method, **kwargs)



if __name__ == "__main__":
    client = JQDataClient(host="101.200.217.122", port=7000, username="admin", password="admin")
    df = get_trade_days(start_date="2015-01-01")
    print(df)

