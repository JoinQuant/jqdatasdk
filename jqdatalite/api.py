# coding=utf-8

from functools import wraps
from .utils import *
from codec import Codec
import numpy as np

client = None


def assert_auth(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        if client is None:
            print("请先调用jqdatalite.init进行认证")
        else:
            return func(*args, **kwargs)
    return _wrapper


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


@assert_auth
def get_price(security, start_date=None, end_date=None, frequency='daily', 
    fields=None, skip_paused=False, fq='pre', count=None):
    """
    获取历史数据
    :param security     一支股票代码或者一个股票代码的list
    :param count        与 start_date 二选一，不可同时使用. 数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据
    :parm start_date    与 count 二选一，不可同时使用. 
                        字符串或者 datetime.datetime/datetime.date 对象, 开始时间. 
    :param end_date     格式同上, 结束时间, 默认是’2015-12-31’, 包含此日期. 
                        注意: 当取分钟数据时, 如果 end_date 只有日期, 则日内时间等同于 00:00:00, 所以返回的数据是不包括 end_date 这一天的.
    :param frequency    单位时间长度, 几天或者几分钟, 现在支持’Xd’,’Xm’, ‘daily’(等同于’1d’), ‘minute’(等同于’1m’), X是一个正整数, 
                        分别表示X天和X分钟(不论是按天还是按分钟回测都能拿到这两种单位的数据), 
                        注意, 当X > 1时, fields只支持[‘open’, ‘close’, ‘high’, ‘low’, ‘volume’, ‘money’]这几个标准字段. 默认值是daily
    """
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    assert (not start_date) ^ (not count), "count 与 start_date 二选一，不可同时使用"
    return client.get_price(**locals())


@assert_auth
def history(count, unit='1d', field='avg', security_list=None,
            df=True, skip_paused=False, fq='pre', pre_factor_ref_date=None):
    assert security_list, "security_list不能为空"
    return client.history(**locals())


@assert_auth
def attribute_history(security, count, unit='1d',
                      fields=['open', 'close', 'high', 'low', 'volume', 'money'],
                      skip_paused=True,
                      df=True,
                      fq='pre'):
    assert is_str(security), "security 为字符串类型"
    return client.attribute_history(**locals())


@assert_auth
def get_trade_days(start_date=None, end_date=None, count=None):
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return client.get_trade_days(**locals())


@assert_auth
def get_all_trade_days():
    return client.get_all_trade_days()


@assert_auth
def get_extras(info, security_list, start_date=None, end_date=None, df=True, count=None):
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return client.get_extras(**locals())


@assert_auth
def get_index_stocks(index_symbol, date=today()):
    assert index_symbol, "指数代码不能为空"
    date = to_date_str(date)
    return client.get_index_stocks(**locals())


@assert_auth
def get_industry_stocks(industry_code, date=today()):
    assert industry_code, "行业编码不能为空"
    date = to_date_str(date)
    return client.get_industry_stocks(**locals())


@assert_auth
def get_concept_stocks(concept_code, date=today()):
    assert concept_code, "概念板块编码不能为空"
    date = to_date_str(date)
    return client.get_concept_stocks(**locals())


@assert_auth
def get_all_securities(types=[], date=None):
    date = to_date_str(date)
    return client.get_all_securities(**locals())


@assert_auth
def get_security_info(code):
    assert code, "标的代码不能为空"
    result = client.get_security_info(**locals())
    if result:
        return Security(**result)


@assert_auth
def get_history_name(code, date):
    date = to_date_str(date)
    return client.get_history_name(**locals())


@assert_auth
def get_money_flow(security_list, start_date=None, end_date=None, fields=None, count=None):
    assert security_list, "security_list不能为空"
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return client.get_money_flow(**locals())


@assert_auth
def get_fundamentals(query_object, date=None, statDate=None):
    from .finance_service import get_fundamentals_sql
    assert (not date) ^ (not statDate), "date和statDate参数只能传入一个"
    sql = get_fundamentals_sql(query_object, date, statDate)
    return client.get_fundamentals(sql=sql)


@assert_auth
def get_mtss(security_list, start_date=None, end_date=None, fields=None, count=None):
    assert (not start_date) ^ (not count), "count 与 start_date 二选一，不可同时使用"
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return client.get_mtss(**locals())



__all__ = ["get_price", "history", "attribute_history", "get_trade_days", "get_all_trade_days", "get_extras", 
            "get_index_stocks", "get_industry_stocks", "get_concept_stocks", "get_all_securities",
            "get_security_info", "get_history_name", "get_money_flow", "get_fundamentals", "get_mtss"]


