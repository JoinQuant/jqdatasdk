# coding=utf-8

"""
财经/宏观经济数据
"""
from .utils import *
import sys
from .client import JQDataClient
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
# try:
#     from functools import lru_cache
# except ImportError:
#     from fastcache import lru_cache

__all__ = [
    "finance",
    "macro",
    "opt",
    "ssymmetry",
    "bond",
    "sup",
    "DBTable",
]


class DBTable(object):
    RESULT_ROWS_LIMIT = 5000

    def __init__(self, db, disable_join=False):
        self.__disable_join = True
        self.__table_names = []
        self.db_name = db

    @assert_auth
    def __load_table_names(self):
        self.__table_names = JQDataClient.instance().get_table_orm(db=self.db_name)
        for name in self.__table_names:
            setattr(self, name, None)

    @assert_auth
    # @lru_cache(maxsize=3)
    def run_query(self, query_object):
        from .client import JQDataClient
        if self.__disable_join:
            check_no_join(query_object)

        limit = self.RESULT_ROWS_LIMIT
        if query_object._limit:
            limit = min(limit, query_object._limit)
        query_object = query_object.limit(limit)

        sql = compile_query(query_object)
        df = JQDataClient.instance().db_query(db=self.db_name, sql=sql)
        return df

    def __load_table_class(self, table_name):
        import datetime
        from sqlalchemy import Date, Column, DateTime, Integer, INTEGER, Numeric, SmallInteger, String, Table, Text, \
            text
        from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL, DOUBLE

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
            raise AttributeError("database %r has no table %r" % (self.db_name, key))

    def __getattribute__(self, key):
        v = object.__getattribute__(self, key)
        if v is None:
            if key in self.__table_names:
                v = self.__load_table_class(key)
                setattr(self, key, v)
        return v


finance = DBTable("finance")
macro = DBTable("macro")
opt = DBTable("opt")
ssymmetry = DBTable("ssymmetry")
bond = DBTable("bond")
sup = DBTable("sup")
