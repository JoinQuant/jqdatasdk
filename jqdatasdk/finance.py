# coding=utf-8

"""
宏观经济数据
"""
from .utils import *
import sys
from .client import JQDataClient
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

class Finance(object):
    RESULT_ROWS_LIMIT = 3000

    db_name = "finance"

    def __init__(self, disable_join=False):
        self.__disable_join = True
        self.__table_names = []

    def __load_table_names(self):
        self.__table_names = JQDataClient.instance().get_table_orm(db=self.db_name)
        for name in self.__table_names:
            setattr(self, name, None)

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
        df = JQDataClient.instance().fin_query(sql=sql)
        return df

    def __load_table_class(self, table_name):
        """
        服务端返回结果示例：

        data = {"name": "IDX_WEIGHT_MONTH", 
                "columns": 
                    [
                        ("id", 'Column(Integer, primary_key=True)'), 
                        ("index_code", 'Column(String(12), nullable=False, comment="指数代码")'), 
                        ("end_date", 'Column(Date, nullable=False, comment="截止日期")'), 
                        ("weight", 'Column(DECIMAL(10, 4), nullable=False, comment="权重")'), 
                        ("status", 'Column(TINYINT(display_width=4), default=0, comment="是否同步,0:未同步,1:已同步")'), 
                        ("addTime", 'Column(TIMESTAMP, default=datetime.datetime.now, comment="插入时间")'), 
                        ("modTime", 'Column(TIMESTAMP, default=datetime.datetime.now, comment="最后修改时间")'), 
                    ]}
        """
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


finance = Finance()


