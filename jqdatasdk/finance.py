# coding=utf-8

"""
宏观经济数据
"""
from .utils import *
import sys


class Finance(object):
    RESULT_ROWS_LIMIT = 3000

    def __init__(self, disable_join=False):
        self.__disable_join = True
        self.__table_names = self.__load_table_names()
        for name in self.__table_names:
            setattr(self, name, self.__load_table_class(name))

    def __load_table_names(self):
        import os
        tables_dir = os.path.join(sys.modules["ROOT_DIR"], 'fin_tables')
        names = []
        if os.path.exists(tables_dir):
            for table_file in os.listdir(tables_dir):
                if table_file.endswith('.py') and not table_file.startswith('__'):
                    names.append(table_file[:-3])
        return names

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
        table_module = __import__('jqdatasdk.fin_tables.' + table_name, fromlist=[table_name])
        return getattr(table_module, table_name)

    # def __getattribute__(self, key):
    #     v = object.__getattribute__(self, key)
    #     if v is None:
    #         if key in self.__table_names:
    #             v = self.__load_table_class(key)
    #             setattr(self, key, v)
    #     return v


finance = Finance()


