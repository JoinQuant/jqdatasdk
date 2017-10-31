# coding=utf-8
from .utils import *
import inspect
import sys


# for cython
if not hasattr(sys.modules[__name__], '__file__'):
    __file__ = inspect.getfile(inspect.currentframe())


class Gta(object):
    RESULT_ROWS_LIMIT = 3000
    query = staticmethod(query)

    def __init__(self):
        self.__disable_join = True
        self.__table_names = self.__load_table_names()
        # 加载 table 太慢了, 动态加载
        for name in self.__table_names:
            setattr(self, name, None)
        pass

    def run_query(self, query_object):
        from .client import JQDataClient
        if self.__disable_join:
            # 不能查询多个表: http://jira.kuanke100.com/browse/GFR-55
            check_no_join(query_object)

        # 限制返回结果最多3000行: http://jira.kuanke100.com/browse/GFR-55
        limit = self.RESULT_ROWS_LIMIT
        if query_object._limit:
            limit = min(limit, query_object._limit)
        query_object = query_object.limit(limit)

        # query object to sql
        sql = compile_query(query_object)
        return JQDataClient.instance().gta_query(sql=sql)

    def _compat_old(self, df):
        # 保持跟以前一样的代码, 返回一样的结果
        csv = df.to_csv(index=False, encoding='utf-8')
        dtypes = df.dtypes.to_csv(None, encoding='utf-8')
        df = pd.read_csv(six.StringIO(csv), dtype=pd.Series.from_csv(six.StringIO(dtypes)), encoding='utf-8')
        return df

    def __load_table_names(self):
        import os
        tables_dir = os.path.join(os.path.dirname(__file__), 'gta_tables')
        if not os.path.exists(tables_dir):
            return
        names = []
        for table_file in os.listdir(tables_dir):
            if table_file.endswith('.py') and not table_file.startswith('__'):
                names.append(table_file[:-3])
        return names

    def __load_table_class(self, table_name):
        table_module = __import__('jqdatalite.gta_tables.' + table_name, fromlist=[table_name])
        return getattr(table_module, table_name)

    def __getattribute__(self, key):
        v = object.__getattribute__(self, key)
        # 如果 table 没有加载, 动态加载
        if v is None:
            if key in self.__table_names:
                v = self.__load_table_class(key)
                setattr(self, key, v)
        return v

gta = Gta()




