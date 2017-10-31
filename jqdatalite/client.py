# coding=utf-8

from api import *
import thriftpy
from thriftpy.rpc import make_client
import msgpack
import cPickle as pickle

from os import path

thrift_path = path.join(path.dirname(__file__), "../jqdata.thrift")
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
                    result = msgpack.unpackb(response.msg)
                    result = pickle.loads(result)
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
                print err.message
                raise err

        return result

    def __getattr__(self, method):
        return lambda **kwargs: self(method, **kwargs)


if __name__ == "__main__":
    client = JQDataClient(host="0.0.0.0", port=7000, username="admin", password="admin")
    print client.get_price(security=["000001.XSHE", "000002.XSHE"], start_date="2017-10-01", end_date="2017-10-26")

