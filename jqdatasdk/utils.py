# coding=utf-8

import sys
import re
import json
import copy
import datetime
from functools import wraps
from collections import namedtuple
from importlib import import_module

import six


for _modname in ("functools", "fastcache", "functools32"):
    try:
        lru_cache = import_module(_modname).lru_cache
    except (ImportError, AttributeError):
        continue
    else:
        break
else:
    def lru_cache(*args, **kwargs):
        def wrapper(func):
            @wraps(func)
            def _func(*args, **kwargs):
                return func(*args, **kwargs)
            _func.cache_info = lambda: None
            _func.cache_clear = lambda: None
            return _func
        return wrapper

Serialized = namedtuple('Serialized', 'json')


class classproperty(object):
    """将方法转换为类属性 @classmethod + @property"""

    def __init__(self, func):
        self.func = classmethod(func)

    def __get__(self, instance, owner):
        return self.func.__get__(instance, owner)()


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


class Security2(Security):

    __slots__ = ("code", "display_name", "name", "start_date", "end_date",
                 "type", "parent",)

    def __repr__(self):
        if sys.version_info[0] < 3:
            display_name = self.display_name.encode('utf-8')
        else:
            display_name = self.display_name
        return (
            "Security(code='{}', type='{}', start_date='{}', end_date='{}', "
            "display_name='{}')"
        ).format(
            self.code, self.type, self.start_date, self.end_date, display_name
        )

    def __str__(self):
        return self.code

    def to_dict(self):
        return {name: getattr(self, name, None) for name in self.__slots__}


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
    """从 sql 语句中拿到所有引用的表名字"""
    sql = re.sub(r'\s+', ' ', sql).replace('`', '').replace('"', '')
    pattern = re.compile(
        r'(?:\b(?:from)|(?:join)\b)\s+(\w+(?:\s*,\s*\w+)*)\b',
        flags=re.I
    )
    matchs = re.findall(pattern, sql)
    tables = ' '.join(matchs).replace(',', ' ')
    return {tab for tab in tables.split()}


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


def _get_sql_session():
    from sqlalchemy.orm import scoped_session, sessionmaker
    session = scoped_session(sessionmaker())
    return session


_sql_session = _get_sql_session()


class SqlQuery(import_module("sqlalchemy.orm").Query):

    limit_value = None
    offset_value = None

    def limit(self, limit):
        self.limit_value = limit
        return super(SqlQuery, self).limit(limit)

    def offset(self, offset):
        self.offset_value = offset
        return super(SqlQuery, self).offset(offset)


def query(*args, **kwargs):
    return SqlQuery(args, **kwargs).with_session(_sql_session)


def compile_query(query):
    """把一个 sqlalchemy query object 编译成mysql风格的 sql 语句"""
    # from sqlalchemy.sql import compiler
    from sqlalchemy.dialects import mysql as mysql_dialetct
    from pymysql.converters import conversions, escape_item, encoders

    dialect = mysql_dialetct.dialect()
    statement = query.statement
    # comp = compiler.SQLCompiler(dialect, statement, literal_binds=True)
    compile_kwargs = {"render_postcompile": True}
    comp = statement.compile(dialect=dialect, compile_kwargs=compile_kwargs)
    # comp.sql_compile()
    # enc = dialect.encoding
    comp_params = comp.params
    params = []
    for k in comp.positiontup:
        v = comp_params[k]
        if six.PY2 and isinstance(v, six.string_types) and not isinstance(v, six.text_type):
            v = v.decode("utf8")
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
        return dt
    try:
        if isinstance(dt, datetime.datetime):
            return "{:0>4}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}".format(
                dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
                )
        elif isinstance(dt, datetime.date):
            return "{:0>4}-{:0>2}-{:0>2}".format(dt.year, dt.month, dt.day)
        elif isinstance(dt, six.string_types):
            ts = to_datetime(dt)
            if len(dt) > 10:
                return "{:0>4}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}".format(
                    ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second
                    )
            else:
                return "{:0>4}-{:0>2}-{:0>2}".format(ts.year, ts.month, ts.day)
        elif isinstance(dt, int):
            return to_date_str(str(dt))
        elif isinstance(dt, six.binary_type):
            return to_date_str(dt.decode('utf-8'))
        else:
            ts = to_datetime(dt)
            return "{:0>4}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}".format(
                ts.year, ts.month, ts.day, ts.hour, ts.minute, ts.second
                )
    except ValueError:
        raise ValueError("无效的日期：{!r}".format(dt))


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


def convert_fields_to_str(s):
    if isinstance(s, (list, tuple)):
        res = [str(item) for item in s]
        return res
    else:
        raise ParamsError("fields's type should be list or tuple")


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


def to_date(value):
    """转化为 datetime.date 类型"""
    if not value:
        return value
    if isinstance(value, six.string_types):
        date = value[:10]
        try:
            separator = date[4]
            if separator in {'-', '/'}:
                return datetime.date(*map(int, date.split(separator)))
            else:
                return datetime.date(int(value[:4]), int(value[4:6]), int(value[6:8]))
        except Exception:
            pass
    elif isinstance(value, datetime.datetime):
        return value.date()
    elif isinstance(value, datetime.date):
        return value
    elif isinstance(value, int):
        return to_date(str(value))
    elif isinstance(value, bytes):
        return to_date(value.decode('utf8'))
    raise ValueError("无效的日期：{!r}".format(value))


def to_datetime(value):
    """转化为 datetime.datetime 类型"""
    if not value:
        return value
    elif isinstance(value, six.string_types):
        try:
            slen = len(value)
            if slen == 12 or slen == 14:  # 202101010000 or 20210101000000
                return datetime.datetime(
                    int(value[:4]),
                    *map(int, (value[idx:(idx + 2)] for idx in range(4, slen, 2)))
                )
            else:
                return datetime.datetime(*map(int, re.split(r"\W+", value)))
        except Exception:
            return datetime.datetime.strptime(str(to_date(value)), '%Y-%m-%d')
    elif isinstance(value, datetime.datetime):
        return value
    elif isinstance(value, datetime.date):
        return datetime.datetime.combine(value, datetime.time.min)
    elif isinstance(value, bytes):
        return to_datetime(value.decode('utf8'))
    raise ValueError("无效的日期：{!r}".format(value))


def assert_auth(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        from .client import JQDataClient
        if not JQDataClient.instance():
            raise Exception("Please run jqdatasdk.auth first")
        else:
            return func(*args, **kwargs)
    return _wrapper


def get_mac_address():
    import uuid
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
    return '%s:%s:%s:%s:%s:%s' % (mac[0:2], mac[2:4], mac[4:6], mac[6:8],mac[8:10], mac[10:])


def hashable_lru(maxsize=16):
    def hashable_cache_internal(func):
        cache = lru_cache(maxsize=maxsize)

        def deserialize(value):
            if isinstance(value, Serialized):
                return json.loads(value.json)
            else:
                return value

        def func_with_serialized_params(*args, **kwargs):
            _args = tuple([deserialize(arg) for arg in args])
            _kwargs = {k: deserialize(v) for k, v in six.viewitems(kwargs)}
            return func(*_args, **_kwargs)

        cached_func = cache(func_with_serialized_params)

        @wraps(func)
        def hashable_cached_func(*args, **kwargs):
            _args = tuple([
                Serialized(json.dumps(arg, sort_keys=True))
                if type(arg) in (list, dict) else arg
                for arg in args
            ])
            _kwargs = {
                k: Serialized(json.dumps(v, sort_keys=True))
                if type(v) in (list, dict) else v
                for k, v in kwargs.items()
            }
            return copy.deepcopy(cached_func(*_args, **_kwargs))
        hashable_cached_func.cache_info = cached_func.cache_info
        hashable_cached_func.cache_clear = cached_func.cache_clear
        return hashable_cached_func

    return hashable_cache_internal


def get_security_type(security):
    exchange = security[-4:]
    code = security[:-5]
    if code.isdigit():
        if exchange == "XSHG":
            if code >= "600000" or code[0] == "9":
                return "stock"
            elif code >= "500000":
                return "fund"
            elif code[0] == "0":
                return "index"
            elif len(code) == 8 and code[0] == '1':
                return "option"
        elif exchange == "XSHE":
            if code[0] == "0" or code[0] == "2" or code[:3] == "300":
                return "stock"
            elif code[:3] == "399":
                return "index"
            elif code[0] == "1":
                return "fund"
        else:
            raise Exception("找不到标的%s" % security)
    else:
        if exchange in ("XSGE", "XDCE", "XZCE", "XINE", "CCFX"):
            if len(code) > 6:
                return "option"
            return "future"
    return 0


class PandasChecker(object):

    @staticmethod
    def check_version():
        if import_module("pandas").__version__[:4] >= "0.25":
            return True
        return False

    VERSION_NOTICE_MESSAGE = (
        "当前环境 pandas 版本高于 0.25，get_price 与 get_fundamentals_continuously "
        "接口的 panel 参数将固定为 False（0.25 及以上版本的 pandas 不再支持 panel，"
        "如使用该数据结构和相关函数请注意修改）"
    )


def isatty(stream=None):
    stream = stream or sys.stdout
    _isatty = getattr(stream, 'isatty', None)
    return _isatty and _isatty()


class suppress(object):

    def __init__(self, *exceptions, **kwargs):
        self.exceptions = exceptions or Exception
        self.logger = kwargs.get("logger") or kwargs.get("log")
        self.loglevel = kwargs.get("loglevel", "exception")

        self._log = None
        if self.logger:
            self._log = getattr(self.logger, self.loglevel, None)

        self.error_count = 0

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type or not issubclass(exc_type, self.exceptions):
            return
        if exc_val and self._log:
            self._log(exc_val)
        self.error_count += 1
        return True

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with self:
                try:
                    return func(*args, **kwargs)
                except self.exceptions as ex:
                    try:
                        func_name = func.__name__
                    except AttributeError:
                        func_name = str(func)
                    msg = "call {}(args={}, kwargs={}) error: {}".format(
                        func_name, args, kwargs, ex
                    )
                    raise Exception(msg)
        return wrapper
