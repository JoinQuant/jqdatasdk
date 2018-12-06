# coding=utf-8

"""
财经/宏观经济数据
"""
from .utils import *
import sys
from .client import JQDataClient
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base


class DBTable(object):

    RESULT_ROWS_LIMIT = 3000

    db_name = None

    def __init__(self, disable_join=False):
        self.__disable_join = True
        self.__table_names = []

    def __load_table_names(self):
        self.__table_names = JQDataClient.instance().get_table_orm(db=self.db_name)
        for name in self.__table_names:
            setattr(self, name, None)

    def get_data(self, sql):
        raise NotImplementedError()

    @assert_auth
    def run_query(self, query_object):
        from .client import JQDataClient
        if self.__disable_join:
            check_no_join(query_object)

        limit = self.RESULT_ROWS_LIMIT
        if query_object._limit:
            limit = min(limit, query_object._limit)
        query_object = query_object.limit(limit)

        sql = compile_query(query_object)
        df = self.get_data(sql=sql)
        return df

    def __load_table_class(self, table_name):
        import datetime
        from sqlalchemy import Date, Column, DateTime, Integer, INTEGER, Numeric, SmallInteger, String, Table, Text, text
        from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL

        data = JQDataClient.instance().get_table_orm(db=self.db_name, table=table_name)
        dct = {}
        for k, v in data["columns"]:
            column = eval(v)
            dct[k] = column
            column.name = k
        dct["__tablename__"] = data["name"]
        return type(data["name"], (declarative_base(),), dct)

    def __getattr__(self, key):
        # 如果没有预先加载了table名字, 加载它
        if not self.__table_names:
            self.__load_table_names()
        # 只对table的名字调用getattr, 否则会无限递归
        if key in self.__table_names:
            return getattr(self, key)
        else:
            raise AttributeError("%r object has no attribute %r" % (self.__class__.__name__, key))

    def __getattribute__(self, key):
        v = object.__getattribute__(self, key)
        if v is None:
            if key in self.__table_names:
                v = self.__load_table_class(key)
                setattr(self, key, v)
        return v


class Finance(DBTable):

    db_name = "finance"

    def get_data(self, sql):
        return JQDataClient.instance().fin_query(sql=sql)


class Macro(DBTable):

    db_name = "macro"

    def get_data(self, sql):
        return JQDataClient.instance().macro_query(sql=sql)


class OPT(DBTable):

    db_name = "opt"

    def get_data(self, sql):
        return JQDataClient.instance().opt_query(sql=sql)


finance = Finance()
macro = Macro()
opt = OPT()
