# coding=utf-8
import six
import datetime
from functools import wraps
import re
import pandas as pd
if six.PY2:
    import cPickle as pickle
else:
    import pickle as pickle


class Security(object):
    code = None
    display_name = None
    name = None
    start_date = None
    end_date = None
    type = None
    parent = None

    def __init__(self, **kwargs):
        self.code = kwargs.get("code", None)
        self.display_name = kwargs.get("display_name", None)
        self.name = kwargs.get("name", None)
        self.start_date = to_date(kwargs.get("start_date", None))
        self.end_date = to_date(kwargs.get("end_date", None))
        self.type = kwargs.get("type", None)
        self.parent = kwargs.get("parent", None)

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code


def no_sa_warnings(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        import warnings
        from sqlalchemy import exc as sa_exc
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)
            return f(*args, **kwds)
    return wrapper


def get_tables_from_sql(sql):
    """ 从 sql 语句中拿到所有引用的表名字 """
    m = re.search(r'FROM (.*?)($| WHERE| GROUP| HAVING| ORDER)', sql, flags=re.M)
    return [t.strip() for t in m.group(1).strip().split(',')] if m else []


@no_sa_warnings
def check_no_join(query):
    """ 确保 query 中没有 join 语句, 也就是说: 没有引用多个表 """
    tables = get_tables_from_sql(str(query.statement))
    if len(tables) != 1:
        raise Exception("only a table is allowed to query every time")


def remove_duplicated_tables(sql):
    """
    去除sql中from重复的表名
    from a, b, a  --》 from a, b
    :param sql:
    :return: sql
    """
    assert isinstance(sql, six.string_types), "sql类型有误"
    table_names = re.findall("from(.*?) where", sql, re.S) or re.findall("FROM(.*?)WHERE", sql, re.S)
    assert table_names, "未从sql语句中发现对应表名"
    unique_table_names = list(set(table_names[0].strip().replace(" ", "").split(",")))
    unique_sql = sql.replace(table_names[0], " " + ",".join(unique_table_names) + " ")
    return unique_sql


def compile_query(query):
    """ 把一个 sqlalchemy query object 编译成mysql风格的 sql 语句 """
    from sqlalchemy.sql import compiler
    from sqlalchemy.dialects import mysql as mysql_dialetct
    from pymysql.converters import conversions, escape_item, encoders

    dialect = mysql_dialetct.dialect()
    statement = query.statement
    comp = compiler.SQLCompiler(dialect, statement)
    comp.compile()
    enc = dialect.encoding
    comp_params = comp.params
    params = []
    for k in comp.positiontup:
        v = comp_params[k]
        if six.PY2 and isinstance(v, unicode):
            v = v.encode(enc)
        if six.PY3 and isinstance(v, bytes):
            v = v.decode(enc)
        v = escape_item(v, conversions, encoders)
        params.append(v)
    return (comp.string % tuple(params))


class ParamsError(Exception):
    pass


def today():
    return datetime.date.today()


def is_str(s):
    return isinstance(s, six.string_types)


def to_date_str(dt):
    if dt is None:
        return None

    if isinstance(dt, six.string_types):
        return dt
    if isinstance(dt, datetime.datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(dt, datetime.date):
        return dt.strftime("%Y-%m-%d")


def is_list(l):
    return isinstance(l, (list, tuple))


def convert_security(s):
    if isinstance(s, six.string_types):
        return s
    elif isinstance(s, Security):
        return str(s)
    elif isinstance(s, (list, tuple)):
        res = []
        for i in range(len(s)):
            if isinstance(s[i], Security):
                res.append(str(s[i]))
            elif isinstance(s[i], six.string_types):
                res.append(s[i])
            else:
                raise ParamsError("can't find symbol {}".format(s[i]))
        return res
    elif s is None:
        return s
    else:
        raise ParamsError("security's type should be Security or list")


def normal_security_code(code):
    """

    :param code:"000001.XSHE"
    :return: "000001"
    """
    if is_str(code):
        if "." in code:
            return code.split(".")[0]
        else:
            return code
    elif is_list(code):
        res = []
        for i in code:
            if "." in i:
                res.append(i.split(".")[0])
            else:
                res.append(i)
        return res
    elif code is None:
        return code
    else:
        raise ParamsError("security type is invalid! type is {}".format(type(code)))


def to_date(date):
    """
    >>> convert_date('2015-1-1')
    datetime.date(2015, 1, 1)

    >>> convert_date('2015-01-01 00:00:00')
    datetime.date(2015, 1, 1)

    >>> convert_date(datetime.datetime(2015, 1, 1))
    datetime.date(2015, 1, 1)

    >>> convert_date(datetime.date(2015, 1, 1))
    datetime.date(2015, 1, 1)
    """
    if is_str(date):
        if ':' in date:
            date = date[:10]
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
    elif isinstance(date, datetime.datetime):
        return date.date()
    elif isinstance(date, datetime.date):
        return date
    elif date is None:
        return None
    raise ParamsError("type error")


def _get_session():
    from sqlalchemy.orm import scoped_session, sessionmaker
    session = scoped_session(sessionmaker())
    return session


session = _get_session()


def query(*args, **kwargs):
    return session.query(*args, **kwargs)


def assert_auth(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        from .client import JQDataClient
        if not JQDataClient.instance():
            print("run jqdatasdk.auth first")
        else:
            return func(*args, **kwargs)
    return _wrapper

