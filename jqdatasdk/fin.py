# coding=utf-8
import os
import sys
from .utils import assert_auth

__all__ = []
tables_dir = os.path.join(sys.modules["ROOT_DIR"], 'fin_tables')
names = []
if os.path.exists(tables_dir):
    for table_file in os.listdir(tables_dir):
        if table_file.endswith('.py') and not table_file.startswith('__'):
            names.append(table_file[:-3])


for table_name in names:
    table_module = __import__('jqdatasdk.fin_tables.' + table_name, fromlist=[table_name])
    globals()[table_name] = getattr(table_module, table_name)
    __all__.append(table_name)


def _run_query(query_object):
    from .utils import compile_query
    limit = 3000
    if query_object._limit:
        limit = min(limit, query_object._limit)
    query_object = query_object.limit(limit)
    sql = compile_query(query_object)
    from .client import JQDataClient
    df = JQDataClient.instance().fin_query(sql=sql)
    return df

run_query = assert_auth(_run_query)


__all__.append("run_query")

