# coding: utf-8

from __future__ import print_function

import re
import time
import datetime
import logging

import pytest
try:
    from unittest import mock
except ImportError:
    import mock

import numpy as np
import pandas as pd

import jqdatasdk
from jqdatasdk.utils import ParamsError
from jqdatasdk.table import DBTable
from jqdatasdk import *  # noqa
from jqdatasdk.technical_analysis import *  # noqa
from jqdatasdk.finance_service import get_fundamentals_sql


log = logging


def assert_sequence_equal(a, b, error=1e-5):
    assert type(a) == type(b)
    for x, y in zip(a, b):
        if isinstance(x, float):
            assert np.isclose(x, y, error)
        else:
            assert x == y


def assert_dict_equal(a, b, error=1e-5):
    assert len(a) == len(b)
    for k, v in a.items():
        if isinstance(v, float):
            assert np.isclose(v, b[k], error)
        else:
            assert v == b[k]


def test_base():
    assert get_test()
    assert float(get_now_time()) > time.time() - 10
    print("Server Version: {}".format(get_server_version()))
    print("Privilege: {}".format(get_privilege()))


@pytest.mark.trylast
def test_set_params():
    cli = jqdatasdk.JQDataClient.instance()

    set_params(request_timeout=10)
    assert cli.request_timeout == 10
    set_params(request_timeout=10000)
    assert cli.request_timeout == 10000
    with pytest.raises(ValueError):
        set_params(request_timeout=-1)

    set_params(request_attempt_count=5)
    assert cli.request_attempt_count == 5
    with pytest.raises(ValueError):
        set_params(request_attempt_count=0)
    with pytest.raises(ValueError):
        set_params(request_attempt_count=20)

    username, password = '13888888888', '123456'
    set_params(request_username=username, request_password=password)
    assert cli._auth_params['username'] == username
    assert cli._auth_params['password'] == password

    host, port = '127.0.0.1', 7000
    set_params(request_host=host, request_port=port)
    assert cli._auth_params['host'] == host
    assert cli._auth_params['port'] == port

    set_params(enable_auth_prompt=False)
    assert cli.enable_auth_prompt is False


def test_get_index_stocks():
    assert len(get_index_stocks('000300.XSHG')) == 300
    assert len(get_index_stocks('000300.XSHG', '2015-11-01')) == 300
    assert len(get_index_stocks('000300.XSHG', datetime.date.today())) == 300
    assert len(get_index_stocks('000300.XSHG', datetime.datetime.now())) == 300
    pass


def test_get_industry_stocks():
    assert len(get_industry_stocks('A01'))
    assert len(get_industry_stocks('C21', datetime.date(2010, 1, 1)))
    assert len(get_industry_stocks('C21', datetime.date(2015, 1, 1)))
    assert len(get_industry_stocks("HY001", datetime.date(2017, 1, 1)))
    assert len(get_industry_stocks("HY002", datetime.date(2017, 12, 12)))
    assert len(get_industry_stocks("HY011", datetime.date(2017, 12, 12)))
    assert len(get_industry_stocks("851521", datetime.date(2012, 12, 12)))


def test_get_industry_stocks2():
    with pytest.raises(Exception) as e:
        get_industry_stocks('XXX')
    with pytest.raises(Exception) as e:
        get_industry_stocks(123)

    stocks = get_industry_stocks("HY001", datetime.date(2017, 12, 12))
    assert '000059.XSHE' in stocks
    with pytest.raises(ValueError) as e:
        stocks.index("300132.XSHE")
    with pytest.raises(ValueError) as e:
        stocks.index("600885.XSHG")
        print(str(e))

    stocks = get_industry_stocks("857241", datetime.date(2015, 6, 6))
    assert "002743.XSHE" in stocks
    assert "002524.XSHE" in stocks
    assert "600496.XSHG" in stocks
    assert "300517.XSHE" not in stocks
    assert "603098.XSHG" not in stocks
    pass


def test_get_concept_stocks():
    with pytest.raises(Exception) as e:
        get_concept_stocks('XXX')
        print(str(e))
    with pytest.raises(Exception) as e:
        get_concept_stocks(123)

    assert get_concept_stocks('SC0001').__len__() > 0
    assert len(get_concept_stocks('sc0001', date=datetime.date(2017, 5, 5))) > 0
    assert len(get_concept_stocks('SC0001', date=datetime.date(2018, 1, 1))) > 0
    assert len(get_concept_stocks('SC0075')) > 0
    assert len(get_concept_stocks('SC0116', datetime.date(2017, 6, 5))) == 0
    assert len(get_concept_stocks('SC0146', datetime.date(2018, 1, 1)))
    assert len(get_concept_stocks('SC0201', datetime.date.today()))
    assert get_concept_stocks("SC0116", datetime.date(2005, 1, 1)) == []


def test_get_all_securities():
    get_all_securities()
    get_all_securities('index')
    get_all_securities(['index'])
    get_all_securities(['index', 'stock'])
    get_all_securities('lof')
    get_all_securities(['etf', 'lof', 'fja', 'fjb'])
    get_all_securities('index', '1990-01-01')
    get_all_securities(['etf', 'lof'], '2015-10-10')
    get_all_securities(date="0001-01-01")
    pass


def test_get_extras():
    df = get_extras('is_st', ['000001.XSHE', '000018.XSHE'], '2013-12-02', '2013-12-03')
    assert list(df.columns) == ['000001.XSHE', '000018.XSHE']
    assert list(df.index) == [datetime.datetime(2013, 12, 2), datetime.datetime(2013, 12, 3)]
    assert (df.values == np.array([[False, True], [False, True]])).all()


def test_get_extras2():
    print(get_extras('unit_net_value', ['511880.XSHG', '511990.XSHG'],
                     start_date="2015-01-05", end_date="2015-01-05", df=True))
    print(get_extras('unit_net_value', ['511880.XSHG', '511990.XSHG'],
                     start_date="2015-01-05", end_date="2015-01-05", df=False))
    pass


def test_get_extras3():
    df = get_extras("futures_sett_price", "IC1509.CCFX",
                    start_date='2015-06-18', end_date='2015-06-19')
    assert list(df.to_dict().keys()) == ['IC1509.CCFX']
    assert list(df.index) == [datetime.datetime(2015, 6, 18), datetime.datetime(2015, 6, 19)]
    assert len(df.values) == 2

    dict = get_extras("futures_sett_price", ["IC1505.CCFX", "IC1606.CCFX"],
                      start_date='2015-04-16', end_date='2016-06-17', df=False)
    assert len(dict.keys()) == 2

    df = get_extras("futures_positions", ["IC1505.CCFX", "IC1606.CCFX", "TF1612.CCFX"],
                    "2016-03-14", datetime.date(2016, 5, 12), df=True)
    assert len(df.columns) == 3
    assert len(df.index) == 42

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)
    df = get_extras("futures_sett_price", "TF1612.CCFX", start_date, end_date)
    print(df)


def test_get_extras4():
    assert len(get_extras('is_st', ['000001.XSHE', '000018.XSHE'],
                          end_date='2015-12-03', count=10)) == 10
    assert len(get_extras('futures_sett_price', 'IC1509.CCFX', count=10)) == 10
    extras = get_extras('futures_positions', 'IC1509.CCFX',
                        end_date='2015-05-01', df=False, count=20)
    assert len(extras) == 1
    assert len(extras['IC1509.CCFX']) == 20

    extras = get_extras('unit_net_value', ['510300.XSHG',
                                           '510050.XSHG'], end_date='2015-01-01', count=10)
    assert len(extras) == 10
    assert len(extras['510050.XSHG']) == 10
    assert str(extras.index.tolist()[-1]) == '2014-12-31 00:00:00'

    with pytest.raises(Exception, match="start_date 参数与 count 参数只能二选一"):
        get_extras('is_st', ['000001.XSHE', '000018.XSHE'], '2015-02-02', '2013-12-03', count=10)
    with pytest.raises(Exception, match="start_date 参数与 count 参数只能二选一"):
        get_extras('acc_net_value', 'IC1509.CCFX', start_date='2015-01-01', count=10)
    with pytest.raises(Exception, match="start_date 参数与 count 参数只能二选一"):
        get_extras('acc_net_value', 'IC1509.CCFX', start_date='2015-01-01', df=False, count=10)


def test_get_security_info():
    res = {
        'display_name': u'\u5e73\u5b89\u94f6\u884c',
        # 'name': u'PAYH',
        'parent': None,
        'end_date': datetime.date(2200, 1, 1),
        'type': 'stock',
        'start_date': datetime.date(1991, 4, 3)
    }
    info = get_security_info('000001.XSHE', date="2019-06-06")
    for f in res:
        assert getattr(info, f) == res[f]
    assert get_security_info('000001.XSHE').type == 'stock'
    assert get_security_info('111000.XSHG').type == 'conbond'
    assert get_security_info('510300.XSHG').type == 'etf'
    assert get_security_info('510300.XSHG').parent is None
    assert get_security_info('502050.XSHG').parent == '502048.XSHG'
    assert get_security_info("180801.XSHE").type == 'reits'

    info = get_security_info2("600000.XSHG")
    print(repr(info))
    assert info.type == "stock"
    assert info.to_dict()["code"] == "600000.XSHG"
    assert "start_date" in repr(info)


def test_normalize_code():
    for code in (1, '000001', 'SZ000001', '000001SZ', '000001.sz', '000001.XSHE'):
        assert '000001.XSHE' == normalize_code(code)
    for code in (600000, '600000', 'SH600000', '600000.XSHG'):
        assert '600000.XSHG' == normalize_code(code)
    assert 'IF1607.CCFX' == normalize_code('IF1607.CCFX')
    pass


def round_df(df, decimal):
    return np.round(df, decimal)


def test_get_price_conbond():
    d = get_security_info("111000.XSHG")
    assert str(d) == "111000.XSHG"
    d = get_price('111000.XSHG',
                  start_date=datetime.date(2022, 1, 1),
                  end_date=datetime.date(2022, 2, 1),
                  frequency='daily',
                  fields=(u'open', 'close', 'paused'))
    assert len(d) == 19
    d = get_price('125301.XSHE',
                  start_date=datetime.date(2022, 1, 1),
                  end_date=datetime.date(2022, 2, 1),
                  frequency='minute',
                  fields=(u'open', 'close', 'paused'))
    assert len(d) == 4560
    d = get_ticks(security='111000.XSHG', end_dt='2022-05-24', start_dt='2022-05-01',
                  skip=False)
    assert len(d) == 40423
    get_price(['125301.XSHE', '111000.XSHG'],
              start_date=datetime.date(2022, 1, 1),
              end_date=datetime.date(2022, 2, 1),
              frequency='minute',
              fields=(u'open', 'close', 'paused'))
    get_price(['125301.XSHE', '125301.XSHE'],
              start_date=datetime.date(2022, 1, 1),
              end_date=datetime.date(2022, 2, 1),
              frequency='minute',
              fields=(u'open', 'close', 'paused'))


def test_get_price():
    # 传入两个重复股票
    get_price(['000001.XSHE', '000001.XSHE'],
              start_date=datetime.date(2015, 1, 1),
              end_date=datetime.date(2015, 2, 1),
              frequency='daily',
              fields=(u'open', 'close', 'paused'))

    get_price('000300.XSHG')
    get_price(u'000300.XSHG')
    get_price('000001.XSHE',
              start_date=datetime.date(2015, 1, 1),
              end_date=datetime.date(2015, 2, 1),
              frequency='daily',
              fields=(u'open', 'close', 'paused', 'factor'))
    get_price('000001.XSHE',
              start_date=datetime.datetime(2015, 1, 1),
              end_date=datetime.datetime(2015, 2, 1),
              frequency='daily',
              fields=[u'open', 'close'])
    get_price('000001.XSHE',
              start_date=datetime.datetime(2015, 1, 1),
              end_date=datetime.datetime(2015, 2, 1),
              frequency='daily',
              fields='open')
    assert get_price('000001.XSHE', start_date='2015-01-01', end_date='2015-02-01', frequency='1d',
                     fq=None).to_csv().replace('\r', '') == \
        """,open,close,high,low,volume,money
2015-01-05,15.99,16.02,16.28,15.6,286043648.0,4565387776.0
2015-01-06,15.85,15.78,16.39,15.55,216642144.0,3453446144.0
2015-01-07,15.56,15.48,15.83,15.3,170012064.0,2634796288.0
2015-01-08,15.5,14.96,15.57,14.9,140771424.0,2128003456.0
2015-01-09,14.9,15.08,15.87,14.71,250850016.0,3835378176.0
2015-01-12,14.87,14.77,15.05,14.5,155329088.0,2293104640.0
2015-01-13,14.65,14.68,14.9,14.61,81687480.0,1204987136.0
2015-01-14,14.78,14.81,15.2,14.7,126302960.0,1889296640.0
2015-01-15,14.85,15.35,15.35,14.71,124217032.0,1868795904.0
2015-01-16,15.4,15.37,15.62,15.18,155584640.0,2403346176.0
2015-01-19,14.01,13.83,14.57,13.83,213712368.0,3016203008.0
2015-01-20,13.83,13.83,14.06,13.56,149101808.0,2064280576.0
2015-01-21,13.88,14.42,14.6,13.75,194053040.0,2758192640.0
2015-01-22,14.34,14.3,14.52,14.16,125501608.0,1801436288.0
2015-01-23,14.36,14.4,14.63,14.3,145918192.0,2108746752.0
2015-01-26,14.36,14.34,14.44,14.16,105760576.0,1508446592.0
2015-01-27,14.35,13.99,14.37,13.83,133949464.0,1881058944.0
2015-01-28,13.87,14.06,14.3,13.8,124087752.0,1742175744.0
2015-01-29,13.82,13.9,14.01,13.75,101675328.0,1408825344.0
2015-01-30,13.93,13.93,14.12,13.76,93011672.0,1298735744.0
"""
    day_columns = 'open close high low volume money pre_close high_limit low_limit paused avg factor'.split()
    assert round_df(get_price('000002.XSHE', fields=day_columns, start_date='2014-12-30',
                              end_date='2015-01-06', fq=None), 12).to_csv().replace('\r', '') == \
        """,open,close,high,low,volume,money,pre_close,high_limit,low_limit,paused,avg,factor
2014-12-30,12.45,12.64,13.15,12.19,386124416.0,4894974976.0,12.43,13.67,11.19,0.0,12.68,1.0
2014-12-31,12.6,13.9,13.9,12.46,489954464.0,6494929920.0,12.64,13.9,11.38,0.0,13.26,1.0
2015-01-05,14.39,14.91,15.29,14.22,656083584.0,9700711424.0,13.9,15.29,12.51,0.0,14.79,1.0
2015-01-06,14.6,14.36,14.99,14.05,334634688.0,4839616000.0,14.91,16.4,13.42,0.0,14.46,1.0
"""
    assert get_price(['000001.XSHE', '000002.XSHE'], fields='close', start_date='2014-12-30',
                     end_date='2015-01-06', fq=None, panel=False).to_csv().replace('\r', '') == \
        """,time,code,close
0,2014-12-30,000001.XSHE,15.5
1,2014-12-31,000001.XSHE,15.84
2,2015-01-05,000001.XSHE,16.02
3,2015-01-06,000001.XSHE,15.78
4,2014-12-30,000002.XSHE,12.64
5,2014-12-31,000002.XSHE,13.9
6,2015-01-05,000002.XSHE,14.91
7,2015-01-06,000002.XSHE,14.36
"""
    df = get_price('000001.XSHE', frequency='5d', start_date='2014-12-01', end_date='2015-01-20', fq=None)
    assert df.to_csv().replace('\r', '') == \
        """,open,close,high,low,volume,money
2014-12-05,12.6,14.53,15.23,12.08,1981703360.0,26377940992.0
2014-12-12,14.21,13.94,15.53,13.02,1538351152.0,22132453632.0
2014-12-19,13.75,15.0,15.67,13.27,1307583232.0,19036847360.0
2014-12-26,14.9,15.1,16.16,13.68,1170986224.0,17439384832.0
2015-01-06,15.61,15.78,16.39,14.75,1237915024.0,19400459776.0
2015-01-13,15.56,14.68,15.87,14.5,798650072.0,12096269696.0
2015-01-20,14.78,13.83,15.62,13.56,768918808.0,11241922304.0
"""

    fields = ['open', 'close', 'low', 'high', 'volume', 'money', 'factor',
              'high_limit','low_limit', 'avg', 'pre_close', 'paused']
    data = get_price('000300.XSHG', fields=fields)
    print(data.dtypes)


def test_get_price2():
    df = get_price("502000.XSHG", start_date='2016-04-01',
                   end_date='2016-04-21', frequency='daily', fields=None)
    # 所有cell都应该不是nan
    assert np.array_equal(df.isnull().values, np.full(df.shape, False))
    df = get_price("161207.XSHE", start_date='2016-04-01',
                   end_date='2016-04-21', frequency='daily', fields=None)
    # 所有cell都应该是nan
    assert np.array_equal(df.isnull().values, np.full(df.shape, True))

    df = get_price('000001.XSHG', start_date='2000-01-01', end_date='2018-01-01')
    assert len(df.index) == len(get_trade_days(end_date="2018-01-01", count=10000))

    assert get_price('000001.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq=None).iloc[[0, -2, -1]].to_csv().replace('\r', '') == """\
,open,close,high,low,volume,money
2005-01-04,6.59,6.52,6.59,6.46,1760832.0,11465603.0
2015-12-30,12.09,12.1,12.11,11.95,53266704.0,641277248.0
2015-12-31,12.1,11.99,12.13,11.98,49125892.0,591643584.0
"""

    assert get_price('000001.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq=None).iloc[[0, -2, -1]].to_csv().replace('\r', '') == """\
,open,close,high,low,volume,money
2005-01-04,6.59,6.52,6.59,6.46,1760832.0,11465603.0
2015-12-30,12.09,12.1,12.11,11.95,53266704.0,641277248.0
2015-12-31,12.1,11.99,12.13,11.98,49125892.0,591643584.0
"""

    assert get_price('000001.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq='post').iloc[[0, -2, -1]].to_csv().replace('\r', '') == """\
,open,close,high,low,volume,money
2005-01-04,179.52,177.62,179.52,175.98,64637.0,11465603.0
2015-12-30,1132.34,1133.27,1134.21,1119.23,568730.0,641277248.0
2015-12-31,1133.27,1122.97,1136.08,1122.03,524519.0,591643584.0
"""

    # 2015-12-18停牌了
    assert get_price('000002.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq=None).iloc[[0, -2, -1]].to_csv().replace('\r', '') == """\
,open,close,high,low,volume,money
2005-01-04,5.22,5.27,5.31,5.17,10353811.0,54514225.0
2015-12-17,20.38,22.21,22.21,20.35,258339264.0,5616476672.0
2015-12-18,22.4,24.43,24.43,21.66,223898400.0,5288950784.0
"""

    assert get_price('000002.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=False, fq=None).iloc[[0, -2, -1]].to_csv().replace('\r', '') == """\
,open,close,high,low,volume,money
2005-01-04,5.22,5.27,5.31,5.17,10353811.0,54514225.0
2015-12-30,24.43,24.43,24.43,24.43,0.0,0.0
2015-12-31,24.43,24.43,24.43,24.43,0.0,0.0
"""

    # 2015-11-02退市了
    assert get_price('000033.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq=None).iloc[[0, -2, -1]].to_csv().replace('\r', '') == """\
,open,close,high,low,volume,money
2005-01-04,3.68,3.71,3.74,3.63,221902.0,815076.0
2015-04-28,9.89,9.89,9.89,9.89,837617.0,8284032.0
2015-04-29,10.38,10.38,10.38,10.38,8184168.0,84951664.0
"""

    assert get_price('000033.XSHE', start_date='2000-01-01', end_date='2015-11-3', skip_paused=False, fq=None).iloc[[0, -2, -1]].to_csv().replace('\r', '') == """\
,open,close,high,low,volume,money
2005-01-04,3.68,3.71,3.74,3.63,221902.0,815076.0
2015-11-02,10.38,10.38,10.38,10.38,0.0,0.0
2015-11-03,10.38,10.38,10.38,10.38,0.0,0.0
"""

    #       display_name    name    start_date  end_date    type
    # 600472.XSHG 包头铝业    BTLY    2005-05-09  2007-12-26  stock
    assert get_price('600472.XSHG', start_date='2000-01-01', end_date='2007-12-27', skip_paused=False, fq=None).iloc[[0, -2, -1]].to_csv().replace('\r', '') == """\
,open,close,high,low,volume,money
2005-01-04,,,,,,
2007-12-26,51.82,51.82,51.82,51.82,0.0,0.0
2007-12-27,,,,,,
"""

    print(get_price('000002.XSHE', end_date='2016-12-31', skip_paused=False)[-2:])

    # print(get_price([], end_date='2016-12-31', skip_paused=False)['open'][-2:])


def test_get_price3():
    codes = ["600000.XSHG", "000001.XSHG", "A2205.XDCE"]
    df = get_price(codes, start_date='2022-01-01', end_date=u'2022-01-15',
                   panel=False)
    print(df)
    assert len(df) == 27
    fields = ['open', 'close']
    df = get_price(codes, start_date='2022-01-04 14:30:00',
                   end_date=u'2022-01-05 09:45:00', frequency="1m",
                   fields=fields, panel=False)
    print(df)
    assert len(df.time.dt.date) == 288 and len(set(df.time.dt.date)) == 2


def test_get_price4():
    df = get_price('600000.XSHG', end_date='2022-01-15', count=3, round=False)
    round_df = get_price('600000.XSHG', end_date='2022-01-15', count=3, round=True)
    res = round_df.values - df.values
    assert res.sum() != 0


def test_get_price_minute():
    p = get_price('000001.XSHE', start_date='2015-01-01', end_date=u'2015-02-01',
                  frequency=u'60m', fields=(u'open', 'close'))
    print(p)

    p = get_price('000001.XSHE', '2014-01-10 09:30:00', '2014-01-11 10:30:00', fields=['close'])
    assert len(p.index) == 1
    p = get_price('000001.XSHE', '2014-01-09 09:30:00',
                  '2014-01-10 15:00:00', frequency='minute', fields=['close'])
    assert len(p.index) == 480

    p = get_price('000001.XSHE', '2014-01-09 09:30:00', '2014-01-10 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    assert len(p.index) == 480

    p = get_price('000001.XSHE', '2014-01-09 00:00:00',
                  '2014-01-09 09:31:00', frequency='minute', fields=['close'])
    assert len(p.index) == 1

    p = get_price('000001.XSHE', '2014-01-09 15:00:00',
                  '2014-01-09 23:00:00', frequency='minute', fields=['close'])
    assert len(p.index) == 1

    p = get_price('000001.XSHE', '2014-01-09 15:00:00',
                  '2014-01-10 09:00:00', frequency='minute', fields=['close'])
    assert len(p.index) == 1
    pass


def test_get_price_minute2():
    p = get_price('000002.XSHE', '2015-12-17 09:30:00', '2015-12-21 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    assert len(p.index) == 480

    p = get_price('000002.XSHE', '2015-12-17 09:30:00', '2015-12-21 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=False)
    assert len(p.index) == 720

    p = get_price('000002.XSHE', '2015-12-21 09:30:00', '2015-12-21 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    assert len(p.index) == 0


def test_get_price_minute3():
    p = get_price(['000001.XSHE', '000002.XSHE'], '2015-12-17',
                  '2015-12-21 23:00:00', frequency='minute', skip_paused=False, panel=False)
    assert len(p['close'].index) == 1440
    p = get_price(['000001.XSHE', '000002.XSHE'], '2015-12-22 09:30:00',
                  '2015-12-21 15:00:00', frequency='minute', skip_paused=False)
    assert len(p['close'].index) == 0


def test_finance_basic():
    df = get_fundamentals(query(income.day).limit(10))
    assert len(df.index) == 10


def test_pd_datetime():
    df = get_all_securities()
    assert 2875 == df[df['start_date'] < "2016-01-01"].shape[0]

    df = get_price('000001.XSHE', start_date="2015-01-05", end_date="2015-12-31")
    assert 5 == df[df.index < '2015-01-10'].shape[0]


def test_log():
    log.debug('debug')
    log.info('info')
    log.warning('warn')
    log.error('error')


def test_get_fundamentals():
    df = get_fundamentals(query(income.day).limit(10), date='2016-07-01')
    assert isinstance(df, pd.DataFrame)
    assert len(df.index) == 10
    df = get_fundamentals(query(income.day).limit(10))
    assert(len(df.index)) == 10
    with pytest.raises(Exception) as e:
        get_fundamentals(query(income.day).limit(10), date='2016-07-01', statDate='2016-07-01')


def test_get_fundamentals2():
    q = query(
        valuation.code,
        indicator.statDate,
        indicator.roe,
        balance.total_assets / balance.total_owner_equities,
        income.total_operating_revenue / balance.total_assets,
        indicator.net_profit_margin,
        indicator.gross_profit_margin,
        valuation.pe_ratio,
        indicator.inc_net_profit_year_on_year,
        indicator.inc_total_revenue_year_on_year,
        indicator.inc_operation_profit_year_on_year,
        indicator.inc_revenue_year_on_year,
        indicator.operating_expense_to_total_revenue,
        indicator.ga_expense_to_total_revenue,
        indicator.financing_expense_to_total_revenue,
        valuation.pb_ratio
    ).filter(
        valuation.code == '000895.XSHE'
    )
    df = get_fundamentals(q, statDate='2017')
    print(df)
    assert df.shape == (1, 16)
    assert "roe" in df.columns
    assert "pe_ratio" in df.columns
    assert "pb_ratio" in df.columns


def test_get_fundamentals3():
    cli = jqdatasdk.JQDataClient.instance()
    sql = "select * from income_statement"
    with pytest.raises(Exception):
        cli.get_fundamentals(sql=sql)
    sql = "select * from income_statement where statDate='2022-08-25'"
    with pytest.raises(Exception):
        cli.get_fundamentals(sql=sql + " limit 10005")
    df = cli.get_fundamentals(sql=sql + " limit 10")
    assert len(df) <= 10
    with pytest.raises(Exception):
        cli.get_fundamentals(sql="select * from a limit 1")

    q = query(
        income.statDate, income.code, income.basic_eps,
        balance.cash_equivalents,
        cash_flow.goods_sale_and_service_render_cash
    ).filter(income.code == '000001.XSHE')
    sql = get_fundamentals_sql(q, statDate='2018q1')
    cli.get_fundamentals(sql=sql)


def test_get_fundamentals_continuously():
    # with date
    df = get_fundamentals_continuously(
        query(income.pubDate).filter(income.code == '000001.XSHE'), datetime.date(2015, 1, 1), 10, panel=False)
    # assert isinstance(df, pd.Panel)
    # assert len(df.major_axis) == 10
    # assert '000001.XSHE' in list(df['pubDate'])
    # assert list(df.major_axis) == ['2014-12-18', '2014-12-19', '2014-12-22', '2014-12-23', '2014-12-24',
    #                                '2014-12-25', '2014-12-26', '2014-12-29', '2014-12-30', '2014-12-31']
    assert len(df) == 10

    # yearly
    df = get_fundamentals_continuously(query(valuation.day, balance.code, cash_flow.code, income.code,
                                             indicator.code).
                                       filter(cash_flow.code.in_(['000001.XSHE', '000002.XSHE'])),
                                              datetime.date(2015, 1, 1), 60, panel=False)
    # assert isinstance(df, pd.Panel)
    # assert len(df.major_axis) == 60
    # assert list(df.minor_axis) == ['000001.XSHE', '000002.XSHE']
    assert len(df) == 120

    # indicator
    df = get_fundamentals_continuously(query(indicator).filter(indicator.code == '000001.XSHE'), '2015-10-15', 10, panel=False)
    # assert isinstance(df, pd.Panel)
    # assert len(df.major_axis) == 10
    # assert list(df['inc_net_profit_to_shareholders_annual']) == ['000001.XSHE']
    # assert list(df['inc_net_profit_to_shareholders_annual']['000001.XSHE']) == [5.81 for i in range(0, 10)]
    assert len(df) == 10


def test_get_industries():
    df = get_industries('sw_l1')
    assert len(df.index) > 0


def test_get_industry():
    dic = get_industry("000001.XSHE", date="2018-12-03")
    assert set(dic["000001.XSHE"].keys()) == set(['sw_l1', 'sw_l2', 'sw_l3', 'zjw', 'jq_l2', 'jq_l1',])
    df = get_industry("000001.XSHE", date="2018-12-03", df=True)
    assert set(dic["000001.XSHE"].keys()) == set(df['type'])


def test_get_concepts():
    df = get_concepts()
    assert len(df.index) > 0


def test_get_margincash_stocks():
    get_margincash_stocks()
    assert len(get_margincash_stocks('2016-12-01')) > 0


def test_get_marginsec_stocks():
    get_marginsec_stocks()
    assert len(get_marginsec_stocks('2016-12-01')) > 0


def test_get_index_weights():
    data = get_index_weights("000001.XSHG", "2018-05-09")
    assert len(data) > 0


def test_get_dominant_future():
    if_ = get_dominant_future('IF', datetime.datetime(2016, 9, 12, 10, 0))
    assert if_ == 'IF1609.CCFX'
    c = get_dominant_future('C', datetime.datetime(2016, 9, 12, 10, 0))
    a = get_dominant_future('A', datetime.datetime(2016, 9, 12, 10, 0))
    b = get_dominant_future('B', datetime.datetime(2016, 9, 12, 10, 0))
    m = get_dominant_future('M', datetime.datetime(2016, 9, 12, 10, 0))
    p = get_dominant_future('P', datetime.datetime(2016, 9, 12, 10, 0))
    i = get_dominant_future('I', datetime.datetime(2016, 9, 12, 10, 0))
    assert c == 'C1701.XDCE'
    assert a == 'A1701.XDCE'
    assert b == 'B1703.XDCE'
    assert m == 'M1701.XDCE'
    assert p == 'P1701.XDCE'
    assert i == 'I1701.XDCE'

    if_2 = get_dominant_future('IF', datetime.datetime(2016, 9, 12, 10, 0))
    assert 'IF' in if_2
    c_ = get_dominant_future('C', '2017-10-23')
    a_ = get_dominant_future('A')
    b_ = get_dominant_future('B')
    m_ = get_dominant_future('M')
    p_ = get_dominant_future('P')
    i_ = get_dominant_future('I')
    assert len(c_) == 10 and 'C' in c_
    assert len(a_) == 10 and 'A' in a_
    assert len(b_) == 10 and 'B' in b_
    assert len(m_) == 10 and 'M' in m_
    assert len(p_) == 10 and 'P' in p_
    assert len(i_) == 10 and 'I' in i_

    res = get_dominant_future(
        underlying_symbol="ag", date='2020-05-08', end_date="2020-05-08 21:00:00"
    )
    assert res.equals(pd.Series({
        '2020-05-08': 'AG2006.XSGE', '2020-05-11': 'AG2012.XSGE'
    }).sort_index())

    with pytest.raises(Exception):
        get_dominant_future("AG", date="2004-06-30")
    assert len(get_dominant_future("AG", end_date="2004-06-30")) == 0


def test_get_future_contracts():
    fc = get_future_contracts('IF', datetime.datetime(2016, 9, 12, 10, 0))
    fc_ = get_future_contracts('IF')
    print(fc_)
    assert len(fc) > 0
    cu = get_future_contracts('cu', datetime.datetime(2016, 9, 12, 10, 0))
    cu_u = get_future_contracts('CU', datetime.datetime(2016, 9, 12, 10, 0))
    if_u = get_future_contracts('IF', datetime.datetime(2016, 9, 12, 10, 0))
    i_u = get_future_contracts('I', datetime.datetime(2016, 9, 12, 10, 0))
    assert cu == cu_u
    assert set(cu) == set(['CU1708.XSGE', 'CU1707.XSGE', 'CU1701.XSGE', 'CU1703.XSGE', 'CU1611.XSGE',
                           'CU1609.XSGE', 'CU1704.XSGE', 'CU1702.XSGE', 'CU1705.XSGE', 'CU1612.XSGE',
                           'CU1706.XSGE', 'CU1610.XSGE'])
    assert set(if_u) == set(['IF1609.CCFX', 'IF1610.CCFX', 'IF1612.CCFX', 'IF1703.CCFX'])
    assert set(i_u) == set(['I1704.XDCE', 'I1703.XDCE', 'I1707.XDCE', 'I1705.XDCE', 'I1708.XDCE',
                            'I1610.XDCE', 'I1706.XDCE', 'I1609.XDCE', 'I1701.XDCE', 'I1702.XDCE',
                            'I1612.XDCE', 'I1611.XDCE'])
    pass


def test_alpha101():
    assert len(alpha101.alpha_001('2017-03-10', '000001.XSHG')) > 0
    assert len(alpha101.alpha_101('2017-03-10', index='all')) > 0


def test_alpha191():
    assert len(alpha191.alpha_001("000001.XSHE", end_date="2017-03-10")) > 0
    time.sleep(1)
    assert len(alpha191.alpha_010("000001.XSHE", end_date="2017-03-10")) > 0

    data = alpha191.alpha_018("000001.XSHE", end_date="2017-03-10")
    print(data.dtypes, type(data.dtypes))


def test_ta():
    security_list = "000001.XSHE"
    check_date = "2017-10-30"
    timeperiod = 20
    assert security_list in technical_analysis.ACCER(security_list, check_date, N=10).keys()
    assert len(technical_analysis.BIAS_QL(security_list, check_date, N=4, M=8)) == 2
    assert len(technical_analysis.Bollinger_Bands(security_list, check_date, timeperiod, nbdevup=2, nbdevdn=2)) == 3

    security_list = ["000001.XSHE", "600000.XSHG"]
    data = technical_analysis.BIAS_36(security_list, check_date,  M=12)
    assert len(data) == 3
    assert isinstance(data, tuple)
    assert isinstance(data[0], dict) and sorted([i for i in data[0].keys()]) == security_list

    assert_dict_equal(
        technical_analysis.CCI("000001.XSHE", datetime.date(2018, 10, 8)),
        {'000001.XSHE': 54.081}
    )


@pytest.mark.parametrize(['func', 'kwargs', 'security', 'expected'],
    [
        ('WR', dict(security_list='000001.XSHE', check_date='2018-12-12', N=10, N1=6,
                    fq_ref_date='2005-01-01', ),
            '000001.XSHE', 79.23558696001311),
        ('WVAD', dict(security_list='000001.XSHE', check_date='2018-12-12', N=24, M=6,
                        fq_ref_date='2005-01-01', ),
            '000001.XSHE', -0.5768863858129046),
        ('XDT', dict(index_stock='000300.XSHG', security_list='000001.XSHE',
                        check_date='2018-12-12', P1=5, P2=10, fq_ref_date='2005-01-01', ),
            '000001.XSHE', 379.44748802280947),
        ('XS', dict(security_list='000001.XSHE', check_date='2018-12-12', timeperiod=13,
                    fq_ref_date='2005-01-01', ),
            '000001.XSHE', 1303.2773793474373),
        ('ZBCD', dict(security_list='000001.XSHE', check_date='2018-12-12', timeperiod=10,
                        fq_ref_date='2005-01-01', ),
            '000001.XSHE', -2.344178255010414),
        ('ZLMM', dict(security_list='000001.XSHE', check_date='2018-12-12',
                        fq_ref_date='2005-01-01', ),
            '000001.XSHE', 37.85041146887006),
        ('ZSDB', dict(index_stock='000300.XSHG', check_date='2018-12-12',
                        fq_ref_date='2005-01-01', ),
            '000300.XSHG', 3159.82),
        ('ZX', dict(security_list='000001.XSHE', check_date='2018-12-12',
                    fq_ref_date='2005-01-01', ),
            '000001.XSHE', 1203.8162155436694),
        ('LB', dict(security_list='000001.XSHE', check_date='2018-12-12',
                    fq_ref_date='2005-01-01', ),
            '000001.XSHE', 0.79837266844305),
        ('Bollinger_Bands', dict(security_list='RB1909.XSGE', check_date='2019-06-18',
                                 fq_ref_date='2005-01-01', ),
            'RB1909.XSGE', 4032.0281122428546),
    ]
)
def test_ta_fq_ref_date1(func, kwargs, security, expected):
    # DT-2225: Jqdatasdk 技术指标库增加复权基准日参数
    ans = eval(func)(**kwargs)
    if isinstance(ans, tuple):
        np.testing.assert_almost_equal(ans[0][security], expected, decimal=4,
                                        err_msg=func, verbose=True)
    else:
        np.testing.assert_almost_equal(ans[security], expected, decimal=4,
                                        err_msg=func, verbose=True)


def test_ta_fq_ref_date2():
    # DT-2225: Jqdatasdk 技术指标库增加复权基准日参数
    security_list = ["000001.XSHE", "600000.XSHG"]
    check_date = "2021-08-17"
    timeperiod = 20
    index_stock = "000300.XSHG"
    today = datetime.date.today()

    # 这几个技术指标不需要 fq_ref_date 参数：'CYF','HSL','FSL','CCL'
    assert ATR(security_list, check_date, timeperiod, fq_ref_date="2020-08-09")
    assert BIAS(security_list, check_date, N1=10, N2=20, N3=60, fq_ref_date="2020-08-09")
    assert CCI(security_list, check_date, N=20, fq_ref_date="2020-08-09")
    assert KDJ(security_list, check_date, N=20, M1=6, M2=9, fq_ref_date="2020-08-09")
    assert MFI(security_list, check_date, timeperiod, fq_ref_date="2020-08-09")
    assert MTM(security_list, check_date, timeperiod, fq_ref_date=today)
    assert ROC(security_list, check_date, timeperiod=12, fq_ref_date=today)
    assert RSI(security_list, check_date, N1=6, fq_ref_date=today)
    assert ACCER(security_list, check_date, N=10, fq_ref_date=today)
    assert ADTM(security_list, check_date, N=28, M=1, fq_ref_date=today)
    assert BIAS_QL(security_list, check_date, N=4, M=8, fq_ref_date='2005-01-01')
    assert BIAS_36(security_list, check_date, M=12, fq_ref_date='2005-01-01')
    assert DKX(security_list, check_date, M=20, fq_ref_date='2005-01-01')
    assert KD(security_list, check_date, N=12, M1=6, M2=3, fq_ref_date='2005-01-01')
    assert LWR(security_list, check_date, N=12, M1=6, M2=3, fq_ref_date=today)
    assert MARSI(security_list, check_date, M1=20, M2=12, fq_ref_date=today)
    assert OSC(security_list, check_date, N=20, M=6, fq_ref_date=today)
    assert SKDJ(security_list, check_date, N=9, M=3, fq_ref_date=today)
    assert UDL(security_list, check_date, N1=3, N2=5, N3=10, N4=20, M=6, fq_ref_date=today)
    assert WR(security_list, check_date, N=10, N1=6, fq_ref_date=None)
    assert TAPI(index_stock, security_list, check_date, M=6, fq_ref_date=None)
    assert CHO(security_list, check_date, N1=10, N2=20, M=6, fq_ref_date=None)
    assert CYE(security_list, check_date, fq_ref_date=None)
    assert DBQR(index_stock, security_list, check_date, N=5, M1=10, M2=20, M3=60, fq_ref_date=None)
    assert DMA(security_list, check_date, N1=10, N2=50, M=10, fq_ref_date=None)
    assert DMI(security_list, check_date, N=14, MM=6, fq_ref_date=None)
    assert DPO(security_list, check_date, N=20, M=6, fq_ref_date=None)
    assert EMV(security_list, check_date, N=14, M=9, fq_ref_date=None)
    assert GDX(security_list, check_date, N=30, M=9, fq_ref_date=None)
    assert JLHB(security_list, check_date, N=7, M=5, fq_ref_date=None)
    assert JS(security_list, check_date, N=5, M1=5, M2=10, M3=20, fq_ref_date=None)
    assert MACD(security_list, check_date, SHORT=12, LONG=26, MID=9, fq_ref_date=None)
    assert QACD(security_list, check_date, N1=12, N2=26, M=9, fq_ref_date=None)
    assert QR(index_stock, security_list, check_date, N=21, fq_ref_date=None)
    assert TRIX(security_list, check_date, N=12, M=9, fq_ref_date=None)
    assert UOS(security_list, check_date, N1=7, N2=14, N3=28, M=6, fq_ref_date=None)
    assert VMACD(security_list, check_date, SHORT=12, LONG=26, MID=9, fq_ref_date=None)
    assert VPT(security_list, check_date, N=51, M=6, fq_ref_date=None)
    assert WVAD(security_list, check_date, N=24, M=6, fq_ref_date=None)
    assert PSY(security_list, check_date, timeperiod=12, fq_ref_date=None)
    assert VR(security_list, check_date, N=26, M=6, fq_ref_date=None)
    assert BRAR(security_list, check_date, N=26, fq_ref_date=None)
    assert CR(security_list, check_date, N=26, M1=10, M2=20, M3=40, M4=62, fq_ref_date=None)
    assert CYR(security_list, check_date, N=13, M=5, fq_ref_date=None)
    assert MASS(security_list, check_date, N1=9, N2=25, M=6, fq_ref_date=None)
    assert PCNT(security_list, check_date, M=5, fq_ref_date=None)
    assert OBV(security_list, check_date, timeperiod=30, fq_ref_date=None)
    assert AMO(security_list, check_date, M1=5, M2=10, fq_ref_date=None)
    assert DBLB(index_stock, security_list, check_date, N=5, M=5, fq_ref_date=None)
    assert DBQRV(index_stock, security_list, check_date, N=5, fq_ref_date=None)
    assert VOL(security_list, check_date, M1=5, M2=10, fq_ref_date=None)
    assert VRSI(security_list, check_date, N1=6, N2=12, N3=24, fq_ref_date=None)
    assert BBI(security_list, check_date, timeperiod1=3, timeperiod2=6, timeperiod3=12,
               timeperiod4=24, fq_ref_date=None)
    assert MA(security_list, check_date, timeperiod, fq_ref_date=None)
    assert EXPMA(security_list, check_date, timeperiod, fq_ref_date=None)
    assert HMA(security_list, check_date, timeperiod, fq_ref_date=None)
    assert LMA(security_list, check_date, timeperiod, fq_ref_date=None)
    assert VMA(security_list, check_date, timeperiod, fq_ref_date=None)
    assert ALLIGAT(security_list, check_date, timeperiod, fq_ref_date=None)
    assert AMV(security_list, check_date, timeperiod, fq_ref_date=None)
    assert BBIBOLL(security_list, check_date, N=11, M=6, fq_ref_date=None)
    assert Bollinger_Bands(security_list, check_date, timeperiod, nbdevup=2,
                           nbdevdn=2, fq_ref_date=None)
    assert ENE(security_list, check_date, N=25, M1=6, M2=6, fq_ref_date=None)
    assert MIKE(security_list, check_date, fq_ref_date=None)
    assert PBX(security_list, check_date, timeperiod, fq_ref_date=None)
    assert XS(security_list, check_date, timeperiod, fq_ref_date=None)
    assert XS2(security_list, check_date, N=102, M=7, fq_ref_date=None)
    assert EMA(security_list, check_date, timeperiod, fq_ref_date=None)
    assert SMA(security_list, check_date, N=7, M=1, fq_ref_date=None)
    assert BDZX(security_list, check_date, fq_ref_date=None)
    assert CDP_STD(security_list, check_date, timeperiod, fq_ref_date=None)
    assert CJDX(security_list, check_date, timeperiod, fq_ref_date=None)
    assert CYHT(security_list, check_date, fq_ref_date=None)
    assert JAX(security_list, check_date, timeperiod, fq_ref_date=None)
    assert JFZX(security_list, check_date, timeperiod, fq_ref_date=None)
    assert JYJL(security_list, check_date, N=120, M=5, fq_ref_date=None)
    assert LHXJ(security_list, check_date, fq_ref_date=None)
    assert LYJH(security_list, check_date, M=80, M1=50, fq_ref_date=None)
    assert TBP_STD(security_list, check_date, timeperiod, fq_ref_date=None)
    assert ZBCD(security_list, check_date, timeperiod, fq_ref_date=None)
    assert SG_SMX(index_stock, security_list, check_date, N=50, fq_ref_date=None)
    assert XDT(index_stock, security_list, check_date, P1=5, P2=10, fq_ref_date=None)
    assert SG_LB(index_stock, security_list, check_date, fq_ref_date=None)
    assert SG_PF(index_stock, security_list, check_date, fq_ref_date=None)
    assert ZLMM(security_list, check_date, fq_ref_date=None)
    assert RAD(index_stock, security_list, check_date, D=3, S=30, M=30, fq_ref_date=None)
    assert SHT(security_list, check_date, N=5, fq_ref_date=today)
    assert CYW(security_list, check_date, fq_ref_date=today)
    assert CYS(security_list, check_date, fq_ref_date="2021-08-09")
    assert ZSDB(index_stock, check_date, fq_ref_date="2021-08-09")
    assert AROON(security_list, check_date, N=25, fq_ref_date="2021-08-09")
    assert CFJT(security_list, check_date, MM=200, fq_ref_date="2021-08-09")
    assert ZX(security_list, check_date, fq_ref_date=today)
    assert PUCU(security_list, check_date, N=24, fq_ref_date=today)


def test_macro():
    q = query(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR).filter(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR.stat_year=='2014')
    df = macro.run_query(q)
    assert len(df) == 33


def test_ticks():
    assert len(get_ticks("CU1901.XSGE", end_dt="2018-03-16", count=100)) == 100
    assert get_ticks(
        "CU1901.XSGE", end_dt="2018-03-16", count=10,
        fields=["time", "current", "volume", "position", "a1_v", "a1_p", "b1_v", "b1_p"]
    ).shape == (10, 8)
    assert len(get_ticks("000001.XSHE", end_dt="2018-03-16", count=10)) == 10
    assert str(get_ticks("SM1809.XZCE", '2018-07-06', '2018-07-07').iloc[3, 0]) == '2018-07-06 09:00:01'
    df = get_ticks(
        "000001.XSHE", end_dt="2018-03-16", count=10, df=True,
        fields=["a1_v", "a2_v", "a3_v", "a4_v", "a5_v", "b1_v", "b2_v", "b3_v", "b4_v", "b5_v"],
    )
    assert df.shape[0] == 10 and df.shape[1] >= 10


def test_get_ticks_rl():
    end_dt = datetime.datetime.now()
    df = get_ticks('000001.XSHE', end_dt=end_dt, count=10, skip=False)
    assert len(df) == 10
    df = get_ticks('600000.XSHG', end_dt=end_dt, count=10, skip=False)
    assert len(df) == 10
    df = get_ticks('399001.XSHE', end_dt=end_dt, count=10, skip=False)
    assert len(df) == 10
    df = get_ticks('000001.XSHG', end_dt=end_dt, count=10, skip=False)
    assert len(df) == 10


def test_billboard_list():
    hs_300 = get_index_stocks('000300.XSHG', '2016-01-10')
    assert len(get_billboard_list(stock_list="300738.XSHE", end_date="2018-03-26", count=5)) == 22
    df = get_billboard_list(hs_300, '2016-01-10', '2017-5-10', None)
    assert len(df) > 0
    stock_list = set(list(df['code']))
    assert len(stock_list) > 71
    assert '000776.XSHE' in stock_list
    assert '300017.XSHE' in stock_list
    df = get_billboard_list(hs_300, None, '2017-5-10', 100)
    assert len(df) > 500
    df = get_billboard_list(None, None, '2017-5-10', 100)
    assert len(df) > 30000
    with pytest.raises(Exception, match="get_billboard_list 不能同时指定 start_date 和 count 两个参数"):
        get_billboard_list(hs_300, '2016-01-10', '2017-5-10', 100)
    with pytest.raises(Exception, match="get_billboard_list 必须指定 start_date 或 count 之一"):
        get_billboard_list(hs_300, None, '2017-5-10', None)


def test_get_locked_shares():
    hs_300 = get_index_stocks('000300.XSHG', '2016-01-10')
    assert len(get_locked_shares(stock_list=['000001.XSHE', '000002.XSHE'], start_date="2018-03-26", forward_count=500)) == 1
    assert len(get_locked_shares(stock_list='000001.XSHE', start_date="2018-03-26", forward_count=500)) == 1
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=500)
    df1 = get_locked_shares(hs_300, start_date, end_date, None)
    df2 = get_locked_shares(hs_300, start_date, None, 500)
    assert len(df1) == len(df2)
    assert len(df1) > 0
    with pytest.raises(Exception, match="get_locked_shares 不能同时指定 end_date 和 forward_count 两个参数"):
        get_locked_shares(hs_300, '2017-01-10', '2018-5-10', 200)
    with pytest.raises(Exception, match="get_locked_shares 必须指定 end_date 或 forward_count 之一"):
        get_locked_shares(hs_300, '2017-01-10', None, None)


def test_finance_tables():
    # lazy load table of finance
    # assert len(finance.__dict__) == 2
    finance.STK_LIST
    # finance查询不全是object类型
    data = finance.run_query(query(finance.STK_LIST))
    assert float in list(finance.run_query(query(finance.STK_LIST)).dtypes)
    assert len(finance.__dict__) > 30
    assert finance.STK_LIST != None
    assert finance.STK_MONEY_FLOW != None
    with pytest.raises(Exception, match="no table 'STK'"):
        finance.STK
    df = finance.run_query(query(finance.STK_STATUS_CHANGE))
    stk_status_change_columns = ["id", "company_id", "code", "name",
                                 "pub_date", "change_date", "change_reason",
                                 "change_type_id", "change_type", "comments",
                                 "public_status_id", "public_status"]
    assert set(stk_status_change_columns) - set(df.columns) == set()
    df = finance.run_query(query(finance.STK_FIN_FORCAST))
    stk_fin_forcast_columns = ["id", "company_id", "code", "name",
                               "end_date", "report_type_id", "report_type",
                               "pub_date", "type_id", "type", "profit_min",
                               "profit_max", "profit_last", "profit_ratio_min",
                               "profit_ratio_max", "content",]
    assert set(stk_fin_forcast_columns) - set(df.columns) == set()
    df = finance.run_query(query(finance.STK_LIST))
    stk_list_columns = ["id", "code", "name", "short_name",
                        "category", "exchange", "start_date",
                        "end_date", "company_id", "company_name",
                        "ipo_shares", "book_price", "par_value",
                        "state_id", "state", "status"]
    assert set(stk_list_columns) - set(df.columns) == set(["status"])


def test_finance_tables2():
    # 测试连表查询的情况
    with pytest.raises(Exception):
        fin = DBTable("finance", disable_join=False)
        data = fin.run_query(query(
            fin.FUND_FIN_INDICATOR.code,
            fin.FUND_FIN_INDICATOR.name,
            fin.FUND_DIVIDEND.event,
            fin.FUND_DIVIDEND.distribution_date
        ).filter(
            fin.FUND_FIN_INDICATOR.code == '000001'
        ))
        print(data)

    from jqdatasdk.utils import get_tables_from_sql
    tables = get_tables_from_sql("select * from tx")
    assert tables == {"tx"}
    tables = get_tables_from_sql("select * from tx, ty, tz")
    assert tables == {"tx", "ty", "tz"}
    tables = get_tables_from_sql("select * from ta join tb where id=1")
    assert tables == {"ta", "tb"}

    with pytest.raises(Exception):
        finance.run_query(query(
            finance.FUND_FIN_INDICATOR.code,
            finance.FUND_FIN_INDICATOR.name,
            finance.FUND_DIVIDEND.event,
            finance.FUND_DIVIDEND.distribution_date
        ).filter(
            finance.FUND_FIN_INDICATOR.code == '000001'
        ))


def test_get_factor_values():
    assert len(get_factor_values("000001.XSHE", "AR", end_date="2017-03-04", count=10)) == 1
    assert len(get_factor_values(["000001.XSHE", "000001.XSHE"], "AR", end_date="2017-03-04", count=10)) == 1
    dct = get_factor_values(["000001.XSHE", "000002.XSHE"],
                            ["AR", "Skewness60"],
                            start_date="2017-03-01",
                            end_date="2017-03-03")["Skewness60"]
    assert dct.to_csv().replace('\r', '') == ",000001.XSHE,000002.XSHE\n2017-03-01,-0.033712,0.017125\n"\
                           "2017-03-02,-0.032092,0.014074\n2017-03-03,0.024989,0.031561\n"
    with pytest.raises(Exception, match="Invalid factors"):
        get_factor_values("000001.XSHE", "asdf", end_date="2017-03-04", count=10)
    with pytest.raises(Exception):
        get_factor_values("000001.XSHE", "asdf", start_date="2017-01-01", end_date="2017-03-04", count=10)
    with pytest.raises(Exception):
        get_factor_values("000001.XSHE", "alpha_001", end_date="2022-02-16", count=10)
    with pytest.raises(Exception):
        get_factor_values("000001.XSHE", ["alpha_001", "alpha_002"], end_date="2022-02-16", count=10)


def test_trade_days():
    data1 = get_trade_days("2015-06-30")
    assert str(data1.dtype) == "object"
    assert type(data1) == np.ndarray
    data2 = get_all_trade_days()
    assert str(data2.dtype) == "object"
    assert type(data2) == np.ndarray


def test_get_bars():
    df = get_bars(['000001.XSHG', '000002.XSHG'], end_dt="2018-10-19", count=5, df=True)
    assert isinstance(df.index, pd.MultiIndex)
    assert len(df) == 10
    assert get_bars("000001.XSHE", count=5, end_dt="2018-10-15").to_csv().replace('\r', '') == (
        ',date,open,high,low,close\n0,2018-10-08,10.7,10.79,10.45,10.45\n1,2018-10-09,10.46,10.7,10.39,10.56\n2,2018-10-10,10.54,10.66,10.38,10.45\n3,2018-10-11,10.05,10.16,9.7,9.86\n4,2018-10-12,9.97,10.34,9.87,10.3\n'
    )
    df = get_bars(["000688.XSHG"], count=6, unit="1M", end_dt="2020-03-10", include_now=False)
    assert df.empty

    df = get_bars('600000.XSHG', end_dt='2022-05-18', count=10, fields=['close'])
    print(df)
    assert not df.empty


def test_get_bars2():
    codes = ["600000.XSHG", "000001.XSHG", "A2205.XDCE"]
    df = get_bars(codes, end_dt="2022-04-01", count=2)
    df = df.reset_index(level=1, drop=True)
    assert len(df) == 6
    assert set(codes) == set(df.index)

    df = get_bars(codes, count=6, unit="1m", end_dt="2022-04-01", include_now=True)
    print(df)
    df = df.reset_index(level=1, drop=True)
    assert len(df) == 6 * 3
    assert set(codes) == set(df.index)


def test_get_bars3():
    df = get_bars('000001.XSHE', start_dt='2024-03-01', end_dt="2024-03-04")
    assert len(df) == 1

    df = get_bars('000001.XSHE', start_dt='2024-03-01',
                  end_dt="2024-03-04 15:00:00", include_now=True)
    assert len(df) == 2
    assert df.date.iloc[-1] == pd.to_datetime('2024-03-04').date()
    assert np.isclose(df.close.iloc[-1], 10.33)

    df = get_bars('000001.XSHE', start_dt='2024-03-01',
                  end_dt="2024-03-04 15:00:00", include_now=True)
    assert len(df) == 2
    assert df.date.iloc[-1] == pd.to_datetime('2024-03-04').date()
    assert np.isclose(df.close.iloc[-1], 10.33)

    df = get_bars('002002.XSHE', end_dt="2024-03-04", count=10,
                  skip_paused=True)
    assert len(df) == 10
    assert df.date.iloc[-1] == pd.to_datetime('2024-01-18').date()

    df = get_bars('002002.XSHE', end_dt="2024-03-04", count=10,
                  skip_paused=False)
    assert len(df) == 10
    assert df.date.iloc[-1] == pd.to_datetime('2024-03-01').date()

    df = get_bars('002002.XSHE', start_dt='2024-03-01', end_dt="2024-03-04",
                  skip_paused=True)
    assert df.empty

    df = get_bars('002002.XSHE', start_dt='2024-03-01', end_dt="2024-03-04",
                  skip_paused=False)
    assert len(df) == 1


def test_get_fund_info():
    assert get_fund_info("000001.OF")
    # df = get_fund_info("518880.OF")
    # df.pop("fund_share")
    # assert df == {
    #     'fund_establishment_day': '2013-07-18',
    #     'fund_manager': u'\u534e\u5b89\u57fa\u91d1\u7ba1\u7406\u6709\u9650\u516c\u53f8',
    #     'fund_name': u'\u534e\u5b89\u6613\u5bcc\u9ec4\u91d1\u4ea4\u6613\u578b\u5f00\u653e\u5f0f\u8bc1\u5238\u6295\u8d44\u57fa\u91d1',
    #     'fund_type': u'\u8d35\u91d1\u5c5e',
    #     'heavy_hold_bond': [],
    #     'heavy_hold_bond_proportion': '',
    #     'heavy_hold_stocks': [],
    #     'heavy_hold_stocks_proportion': ''
    # }

def test_get_futures_info():
    data = get_futures_info('SN2107.XSGE')
    assert data == {'SN2107.XSGE':
                        {'tick_size': 10.0,
                         'trade_time': [['2020-07-16', '2021-07-15', '21:00~01:00',
                                         '09:00~10:15', '10:30~11:30', '13:30~15:00']],
                         'contract_multiplier': 1.0}}
    data = get_futures_info(['SN2107.XSGE', 'SN2207.XSGE'])
    assert data == {'SN2207.XSGE':
                        {'tick_size': 10.0,
                         'trade_time': [['2021-07-16', '2022-07-15',
                                         '21:00~01:00', '09:00~10:15',
                                         '10:30~11:30', '13:30~15:00']],
                         'contract_multiplier': 1.0},
                    'SN2107.XSGE': {'tick_size': 10.0,
                                    'trade_time': [['2020-07-16', '2021-07-15',
                                                    '21:00~01:00', '09:00~10:15',
                                                    '10:30~11:30', '13:30~15:00']],
                                    'contract_multiplier': 1.0}}

def test_get_current_tick():
    today = datetime.date.today()
    is_tradeday = (today in get_trade_days(start_date=today))
    if is_tradeday:
        assert type(get_current_tick('000002.XSHE')) == pd.DataFrame
        assert len(get_current_tick('000001.XSHE')) == 1
        assert get_current_tick('600535.XSHG').columns.tolist() == [
            'datetime', 'current', 'high', 'low', 'volume', 'money',
            'a1_p', 'a1_v', 'a2_p', 'a2_v', 'a3_p', 'a3_v', 'a4_p',
            'a4_v', 'a5_p', 'a5_v', 'b1_p', 'b1_v', 'b2_p', 'b2_v',
            'b3_p', 'b3_v', 'b4_p', 'b4_v', 'b5_p', 'b5_v'
        ]
        assert get_current_tick(get_dominant_future('AP')).columns.tolist() == [
            'datetime', 'current', 'high', 'low', 'volume', 'money', 'position',
            'a1_p', 'a1_v', 'b1_p', 'b1_v'
        ]
    else:
        assert get_current_tick('000002.XSHE').isnull().all().all()
    trade_codes = get_future_contracts("IF")
    print(trade_codes)
    df = get_current_tick(trade_codes)
    assert len(df) == len(trade_codes)
    assert set(df.index.tolist()) == set(trade_codes)
    assert get_current_tick(["000001.XSHE", "000006.XSHE"]).index.tolist() == ["000001.XSHE", "000006.XSHE"]
    assert get_current_tick("000001.XSHE").index.tolist() == [0]
    with pytest.raises(Exception, match="not support future"):
        get_current_tick(trade_codes + ["AU8888.XSGE"])


def del_test_get_price_engine():
    df = get_price_engine(["000001.XSHE", "000002.XSHE"], end_date='2018-10-01', count=1, fq=None)
    assert type(df) == pd.core.panel.Panel
    assert df.minor_xs("000001.XSHE").to_json() == ('{"close":{"1538092800000":11.05},"high":{"1538092800000":11.27},'
                                    '"low":{"1538092800000":10.78},"money":{"1538092800000":2331358288.9600000381},'
                                    '"open":{"1538092800000":10.78},"volume":{"1538092800000":211024267.0}}')
    assert get_price_engine(["000001.XSHE", "000002.XSHE"], end_date='2018-10-01', count=1, fq='post',
                            pre_factor_ref_date='2018-10-01').minor_xs("000001.XSHE").to_csv() == (
',close,high,low,money,open,volume\n2018-09-28,1298.24,1324.09,1266.52,2331358288.96,1266.52,1796135.0\n')


def del_test_history_engine():
    assert history_engine("2018-10-01",5, security_list=["000001.XSHE", "600360.XSHG"],
                          pre_factor_ref_date='2018-10-01').to_csv() == (
',000001.XSHE,600360.XSHG\n2018-09-21,10.51,''6.09\n2018-09-25,10.55,6.12\n2018-09-26,10.74,6.15\n2018-09-27,10.7,5.99\n2018-09-28,11.05,5.95\n')


def del_test_attribute_history_engine():
    assert attribute_history_engine("2018-10-01","600360.XSHG",5,pre_factor_ref_date='2018-10-01').to_csv() == (
',open,close,high,low,volume,money\n2018-09-21,6.07,6.12,6.14,6.02,8063165.0,49144137.0\n2018-09-25,6.11,6.12,6.17,'
'6.07,5200100.0,31811127.0\n2018-09-26,6.12,6.14,6.2,6.1,7534100.0,46317036.0\n2018-09-27,6.13,5.91,6.13,5.84,11052'
'861.0,66220858.0\n2018-09-28,5.91,5.97,5.99,5.91,4979800.0,29647440.0\n')


def del_test_get_bars_engine():
    df = get_bars_engine('000006.XSHE',end_dt='2018-10-26',count=5, fq_ref_date='2018-11-07')
    assert type(df) == np.ndarray
    assert df.tolist() == [(4.6, 4.92, 4.51, 4.88),
                           (4.92, 5.18, 4.91, 5.07),
                           (5.11, 5.24, 5.0, 5.05),
                           (5.06, 5.12, 4.97, 5.08),
                           (4.86, 5.04, 4.8, 5.02)]
    assert df.tolist() == get_bars_engine(
        '000006.XSHE',end_dt='2018-10-26',count=5, fq_ref_date=datetime.date(2018, 11, 7)).tolist()


def del_test_get_ticks_engine():
    df = get_ticks_engine('600535.XSHG', end_dt='2018-10-10', count=1)
    assert type(df) == np.ndarray
    assert df.tolist() == [(20181009150001.0, 21.83, 22.54, 21.72, 4898100.0,
                            107742440.0, 21.83, 1600.0, 21.85, 36000.0, 21.86, 1000.0,
                            21.87, 21000.0, 21.89, 500.0, 21.82, 7400.0, 21.81, 11500.0,
                            21.8, 1500.0, 21.79, 14300.0, 21.78, 4800.0)]
    df1 =  get_ticks_engine(['600535.XSHG','000007.XSHE'], end_dt='2018-10-10', count=1)
    assert type(df1) == dict
    assert df1["600535.XSHG"] == df


def del_test_get_current_tick_engine():
    today = datetime.date.today()
    is_tradeday = (today in get_trade_days(start_date=today))
    df = get_current_tick_engine(['000002.XSHE', '600358.XSHG'])
    if is_tradeday:
        assert type(df) == dict
        assert str(type(df["000002.XSHE"])) == "<class 'jqdata.models.tick.Tick'>"
    else:
        assert df['000002.XSHE'] == None
        assert df['600358.XSHG'] == None


def del_test_get_daily_info_engine():
    assert get_daily_info_engine("164810.XSHE", "2018-11-20") == {
        'factor': {'164810.XSHE': 1.0},
        'high_limit': {'164810.XSHE': 1.089},
        'is_trading': {'164810.XSHE': True},
        'low_limit': {'164810.XSHE': 0.891},
    }
    assert get_daily_info_engine(("000001.XSHE", "TF1906.CCFX"), "2018-10-23") == {
        'factor': {'000001.XSHE': 117.488, 'TF1906.CCFX': 1.0},
        'high_limit': {'000001.XSHE': 12.27, 'TF1906.CCFX': 100.315},
        'is_trading': {'000001.XSHE': True, 'TF1906.CCFX': True},
        'low_limit': {'000001.XSHE': 10.04, 'TF1906.CCFX': 95.615},
    }


def test_get_query_count():
    assert type(get_query_count()) == dict
    data = get_query_count(None)
    assert "total" in data and "spare" in data
    if type(get_query_count("total")) == int:
        req = get_query_count("spare")
        print(req)
        data = get_trade_days(count=1)
        assert get_query_count("spare") == req - 1
        print("after query 1 row, %s" % get_query_count("spare"))
    else:
        assert type(get_query_count("total")) == float
        assert type(get_query_count("spare")) == int


def test_opt_tables():
    assert opt.run_query(query(opt.OPT_DAILY_PRICE).limit(10)).columns.tolist() == [
        'id', 'code', 'exchange_code', 'date', 'pre_settle', 'pre_close',
        'open', 'high', 'low', 'close', 'change_pct_close', 'settle_price',
        'change_pct_settle', 'volume', 'money', 'position'
    ]
    assert len(opt.run_query(query(opt.OPT_ADJUSTMENT).limit(10))) == 10
    assert opt.run_query(query(
            opt.OPT_EXERCISE_INFO
        ).filter(
            opt.OPT_EXERCISE_INFO.underlying_symbol=='510050.XSHG'
        ).filter(
            opt.OPT_EXERCISE_INFO.exercise_date=='2015-05-27'
        )).to_csv().replace('\r', '') == (',id,underlying_symbol,underlying_name,exercise_date,contract_type,exercise_number\n'
        '0,3,510050.XSHG,50ETF,2015-05-27,CO,7333\n1,4,510050.XSHG,50ETF,2015-05-27,PO,1897\n')
    assert opt.run_query(query(opt.OPT_CONTRACT_INFO.code).limit(10)).columns.tolist() == ["code"]


def test_get_factor_effect():
    df = get_factor_effect("000001.XSHG", start_date="2015-01-01", end_date="2018-01-01", period="3M", factor="net_profit_growth_rate")
    print(df)
    assert_dict_equal(df[1].to_dict(), {
        datetime.date(2015, 1, 5): 0.0,
        datetime.date(2015, 3, 31): 0.2911737010850679,
        datetime.date(2015, 6, 30): 0.6774030318149995,
        datetime.date(2015, 9, 30): 0.12540945276743498,
        datetime.date(2015, 12, 31): 0.4827570435926156,
        datetime.date(2016, 3, 31): 0.2134204934053765,
        datetime.date(2016, 6, 30): 0.21345157034224815,
        datetime.date(2016, 9, 30): 0.2923701525614304,
        datetime.date(2016, 12, 31): 0.38180433529720026,
        datetime.date(2017, 3, 31): 0.3677375473696791,
        datetime.date(2017, 6, 30): 0.25566522532293967,
        datetime.date(2017, 9, 30): 0.30284329696764223,
        datetime.date(2017, 12, 31): 0.18990079481373812
    }
    ,error=1e-2)

    df1 = get_factor_effect('000300.XSHG', '2019-01-01', '2019-03-14', '1W', 'operating_revenue_ttm', group_num = 3)
    print(df1)
    assert len(df1.iloc[0,:]) == 3


def test_get_data():
    df = get_data("get_price", security=['000001.XSHE', '000002.XSHE'], fields='close', start_date='2014-12-30',
                        end_date='2015-01-06', fq=None, panel=False)
    df.to_csv().replace('\r', '') == \
""",time,code,close
0,2014-12-30,000001.XSHE,15.5
1,2014-12-31,000001.XSHE,15.84
2,2015-01-05,000001.XSHE,16.02
3,2015-01-06,000001.XSHE,15.78
4,2014-12-30,000002.XSHE,12.64
5,2014-12-31,000002.XSHE,13.9
6,2015-01-05,000002.XSHE,14.91
7,2015-01-06,000002.XSHE,14.36
"""
    for code in (1, '000001', 'SZ000001', '000001SZ', '000001.sz', '000001.XSHE'):
        assert '000001.XSHE' == get_data("normalize_code", code=code)


def test_get_all_factors():
    df = get_all_factors()
    assert re.split(r'\s+', df.iloc[3].to_string()) == [u'factor', u'circulating_market_cap', u'factor_intro', u'\u6d41\u901a\u5e02\u503c', u'category', u'basics', u'category_intro', u'\u57fa\u7840\u79d1\u76ee\u53ca\u884d\u751f\u7c7b\u56e0\u5b50']


def pass_test_timeout_error():
    stocks = get_all_securities().index.tolist()
    with pytest.raises(Exception) as e:
        get_price(stocks, end_date="2019-04-01", count=10000)
        pytest.fail("查询超时，请缩小查询范围后重试")


def test_get_mtss():
    stocks = get_all_securities(date='2012-05-28').index.tolist()
    fields = ['sec_code', 'fin_value', 'fin_buy_value',
              'fin_refund_value', 'sec_value', 'sec_sell_value',
              'sec_refund_value', 'fin_sec_value']
    df = get_mtss(stocks, start_date='2012-05-28', end_date='2012-06-01', fields=fields)
    print(len(stocks))
    print(len(df))
    assert not df.empty

    date = '2020-03-12'
    securities = get_all_securities(types=['stock'], date=date)
    stocks = securities.index.tolist()
    df = get_mtss(stocks, start_date=date, end_date=date)
    print(df)
    assert not df.empty


def test_get_valuation():
    # DT-2302
    res = get_valuation(('000001.XSHE', '000002.XSHE'), end_date='2019-07-24',
                        fields=('code', 'day', 'pe_ratio', 'pb_ratio', 'market_cap'), count=2)
    print(res)
    assert len(res) == 4
    assert set(res['code']) == {'000001.XSHE', '000002.XSHE'}
    assert list(res[res['code'] == '000001.XSHE']['market_cap']) == [2362.6486, 2383.2531]
    assert list(res[res['code'] == '000002.XSHE']['market_cap']) == [3390.6429, 3387.2523]

    res = get_valuation('000001.XSHE', end_date='2019-07-24', fields='market_cap', count=5)
    assert len(res) == 5
    assert list(res['market_cap']) == [2347.1952, 2402.1406, 2378.102, 2362.6486, 2383.2531]
    assert list(res[res['code']=='000001.XSHE']['day']) \
           == [datetime.date(2019, 7, 18), datetime.date(2019, 7, 19), datetime.date(2019, 7, 22),
               datetime.date(2019, 7, 23), datetime.date(2019, 7, 24)]

    res = get_valuation(('000001.XSHE', '000002.XSHE'), start_date='2019-07-20', end_date='2019-07-24',
                        fields=('code', 'day', 'pe_ratio', 'pb_ratio', 'market_cap'))
    assert len(res) == 6
    assert list(res[res['code'] == '000001.XSHE']['pe_ratio']) == [9.2645, 9.2043, 9.2846]
    assert list(res[res['code'] == '000002.XSHE']['pe_ratio']) == [10.3386, 9.9729, 9.963]

    res = get_valuation('000001.XSHE', start_date='2019-07-20', end_date='2019-07-24', fields='market_cap')
    assert len(res) == 3
    assert list(res['market_cap']) == [2378.102, 2362.6486, 2383.2531]
    assert list(res['day']) == [datetime.date(2019, 7, 22),
                                datetime.date(2019, 7, 23),
                                datetime.date(2019, 7, 24)]


def test_get_history_fundamentals():
    # DT-2302
    # 多标的、跨表、指定watch_date、1q
    fields = [balance.statDate, income.net_profit,
              balance.cash_equivalents,
              cash_flow.dividend_interest_payment]
    df = get_history_fundamentals(['000001.XSHE', '000002.XSHE'], fields,
                                   watch_date='2019-03-31', count=10)
    print(df)
    assert not df.empty
    # 多标的、跨表、指定watch_date、1y
    fields = [balance.statDate, income.net_profit,
              balance.cash_equivalents,
              cash_flow.net_operate_cash_flow]
    df = get_history_fundamentals(['000001.XSHE', '000002.XSHE'], fields,
                                   watch_date='2019-07-01', interval='1y', count=10)
    print(df)
    assert not df.empty
    # 多标的、跨表、指定stat_date、1q
    df = get_history_fundamentals(['000001.XSHE', '000002.XSHE'], fields,
                                  stat_date='2019q1', count=10)
    print(df)
    assert not df.empty
    # 多标的、跨表、指定stat_date、年表
    df = get_history_fundamentals(['000001.XSHE', '000002.XSHE'], fields, stat_date='2019',
                                  interval='1y', count=10, stat_by_year=True)
    print(df)
    assert not df.empty
    # 官网示例
    df = get_history_fundamentals(['000001.XSHE', '600000.XSHG'],
                                  fields=[balance.cash_equivalents,
                                          cash_flow.net_deposit_increase,
                                          income.total_operating_revenue],
                                  watch_date=None,
                                  stat_date='2019q1',
                                  count=5,
                                  interval='1q',
                                  stat_by_year=False)
    print(df)
    assert not df.empty
    # 银行业专项测试
    df = get_history_fundamentals(['600015.XSHG', '600926.XSHG'],
                                  fields=[bank_indicator.total_loan,
                                          bank_indicator.non_interest_income,
                                          bank_indicator.Nonperforming_loan_rate],
                                  stat_date='2019',
                                  interval='1y',
                                  stat_by_year=True)
    print(df)
    assert not df.empty
    # 保险业专项测试
    df = get_history_fundamentals(['601336.XSHG'],
                                  fields=[insurance_indicator.payoff_cost],
                                  stat_date='2019',
                                  interval='1y',
                                  stat_by_year=True)
    print(df)
    assert not df.empty
    # 券商业专项测试
    df = get_history_fundamentals(['002500.XSHE', '002673.XSHE'],
                                  fields=[security_indicator.net_assets],
                                  stat_date='2019',
                                  interval='1y',
                                  stat_by_year=True)
    print(df)
    assert not df.empty
    # 测试异常抛出情况
    with pytest.raises(AssertionError):
        get_history_fundamentals(['000002.XSHE'], fields=[balance.cash_equivalents])
    with pytest.raises(Exception):
        get_history_fundamentals(['000001.XSHE'],
                                 fields=income.total_operating_revenue,
                                 stat_date='2019q1')


def test_get_call_auction():
    data = get_call_auction('000001.XSHE', start_date='2021-09-15', end_date='2021-09-15')
    print(data)
    assert len(data) > 0

    data2 = get_call_auction('000001.XSHE', start_date='2021-09-15',
                             end_date='2021-09-15 09:30:00')
    assert len(data) == len(data2)
    print(data)

    with pytest.raises(TypeError):
        get_call_auction('000001.XSHE', start_date='2021-09-15')


def test_get_factor_kanban_values():
    kbv = get_factor_kanban_values(
        universe='zz800', bt_cycle='year_1', skip_paused=False,
        commision_slippage=1, category='emotion', model='long_short'
    )
    print(kbv)
    assert set(kbv['universe']) == set(['zz800'])
    assert set(kbv['bt_cycle']) == set(['year_1'])
    assert set(kbv['category']) == set(['emotion'])
    assert kbv['commision_slippage'].any() == 1
    with pytest.raises(AssertionError):
        kbv = get_factor_kanban_values(model='hhh')
    zz1000 = get_factor_kanban_values(
        universe='zz1000', bt_cycle='year_1', skip_paused=False,
        commision_slippage=1, category='style_pro', model='long_short'
    )
    assert set(zz1000.category) == set(['style_pro'])


def test_get_factor_style_returns():
    data = get_factor_style_returns()
    print(data)
    assert not data.empty
    data2 = get_factor_style_returns(
        factors=['beta', 'growth', 'HY001'],
        start_date='2021-01-01',
        end_date='2021-01-10'
    )
    print(data2)
    assert not data2.empty

    factors = ["size", "801010", "HY001"]
    data3 = get_factor_style_returns(factors=factors,
                                     start_date='2022-08-05',
                                     end_date='2022-08-16',
                                     universe=None,
                                     industry='sw_l1')
    print(data3)
    assert not data3.empty

    with pytest.raises(Exception):
        style_pro_factors = ['financial_leverage', 'size']
        get_factor_style_returns(factors=style_pro_factors,
                                 start_date='2023-09-01',
                                 end_date='2023-09-10',
                                 universe='zz2000',
                                 industry='sw_l1')


def test_get_factor_specific_returns():
    data = get_factor_specific_returns(security='000001.XSHE',
                                       end_date='2022-08-16',
                                       count=7)
    print(data)
    assert not data.empty


def test_get_factor_stats():
    # 测试默认值
    data = get_factor_stats()
    print(data)
    assert len(data['beta']) >= 9
    # 测试 factor_names
    with pytest.raises(Exception):
        data = get_factor_stats(factor_names='hhh')
    # 测试多因子
    data1 = get_factor_stats(
        factor_names=['beta', 'size', 'growth'],
        universe_type='zzqz',
        start_date='2021-01-01',
        end_date='2021-01-10',
    )
    print(data1)
    assert set(data1.keys()) == set({'beta', 'size', 'growth'})
    assert len(data1['beta'])
    assert len(data1['size'])
    assert len(data1['growth'])
    # 测试 count
    data2 = get_factor_stats(factor_names=['growth'],
                             end_date=datetime.date(2021,9,1), count=20)
    assert len(data2['growth']) == 20
    print(data2)
    # 测试手续费, 跳过停牌
    data3 = get_factor_stats(
        factor_names=['net_profit_to_total_operate_revenue_ttm'],
        skip_paused=True,
        commision_fee=0.0008
    )
    print(data3)
    assert len(data3['net_profit_to_total_operate_revenue_ttm']) >= 9
    data4 = get_factor_stats(
        factor_names=['net_profit_to_total_operate_revenue_ttm'],
        skip_paused=True,
        commision_fee=0.0018
    )
    print(data4)
    assert len(data4['net_profit_to_total_operate_revenue_ttm']) >= 9
    with pytest.raises(Exception):
        get_factor_stats(commision_fee=0.0001)
    # 测试 start_date
    data5 = get_factor_stats(
        factor_names=['growth'],
        start_date='2021-08-30',
        end_date='2021-09-03'
    )
    print(data5)
    assert len(data5['growth']) == 5
    # 测试 股票池
    with pytest.raises(AssertionError, match='^股票池应为.*$'):
        get_factor_stats(universe_type='沪深300')
    # 测试 start_date count
    with pytest.raises(ParamsError, match='^.*only.one.param.is.required$'):
        get_factor_stats(start_date='2021-08-30', count=10)
    # 测试 date
    with pytest.raises(Exception):
        get_factor_stats(start_date='2021-08-30', end_date='2021-08-20')


def test_get_factor_cov():
    data = get_factor_cov('2022-01-01', '2023-10-01',
                          ['sw_l1_801010'], ['sw_l1_growth'], 'jq_l1')
    assert data.empty
    df1 = get_factor_cov('2022-01-01', '2022-02-01')
    assert set(df1.factors.tolist()) == set(
        ["size", 'beta', 'momentum', 'residual_volatility',
         'non_linear_size', 'book_to_price_ratio', 'liquidity',
         'earnings_yield', 'growth', 'leverage'])
    df2 = get_factor_cov('2022-01-01', '2022-05-01',
                         ['size', 'beta', 'momentum'], ['801180', '801730'])
    assert set(df2.factors.tolist()) == set(['size', 'beta', 'momentum'])
    assert set(['801180', '801730']).issubset(set(df2.columns))


def test_get_all_alpha():
    date = '2022-10-10'
    alpha = ['alpha_001', 'alpha_002', 'alpha_003', 'alpha_004']
    codes = ['000001.XSHE', '000002.XSHE', '000004.XSHE']

    alpha101_sub = get_all_alpha_101(date, codes, alpha)
    alpha191_sub = get_all_alpha_191(date, codes, alpha)
    alpha101_all = get_all_alpha_101(date)
    alpha191_all = get_all_alpha_191(date)

    assert len(alpha101_sub) > 0
    assert len(alpha191_sub) > 0
    assert len(alpha101_all) == len(alpha191_all) == 4830


def test_acc_info():
    info = get_account_info()
    print(info)
    assert set(info.keys()) == {
        'license', 'date_range_start', 'query_count_limit',
        'date_range_end', 'expire_time', 'mob'
    }


def test_get_empty_data():
    ret = get_price(["000001.XSHE"], end_date='2001-01-01')
    print(ret)
    assert ret.empty

    ret = get_price('000001.XSHE', end_date='2001-01-01', count=1)
    print(ret)
    assert ret.empty


def test_get_money_flow_pro():
    start_date_1 = datetime.datetime(2015, 1, 1, 16, 0)
    end_date_1 = datetime.datetime(2015, 1, 10, 16, 0)
    count_1 = 10
    fields = ['inflow_xl',
            'inflow_l',
            'inflow_m',
            'inflow_s',
            'outflow_xl',
            'outflow_l',
            'outflow_m',
            'outflow_s',
            'netflow_xl']
    security_list = ['000001.XSHE', '600519.XSHG', '600360.XSHG', '888888.AAA']
    res_1_1 = get_money_flow_pro(security_list,
                                 start_date_1,
                                 end_date_1,
                                 fields=fields)
    print(res_1_1)
    assert not res_1_1[(start_date_1 < res_1_1.time) & (res_1_1.time < end_date_1)].empty
    assert '888888.AAA' not in res_1_1.code

    res_1_2 = get_money_flow_pro(security_list,
                                 None,
                                 end_date_1,
                                 fields=fields,
                                 count=count_1)
    print(res_1_2)
    assert res_1_1.equals(res_1_2)

    # 测试取分钟级别的历史资金流向数据
    start_date_2 = datetime.datetime(2023, 9, 1, 16, 0)
    end_date_2 = datetime.datetime(2023, 9, 10, 16, 0)
    res_2_1 = get_money_flow_pro(security_list,
                                 start_date_2,
                                 end_date_2,
                                 frequency='1m',
                                 fields=fields)
    print(res_2_1)
    assert not res_2_1[(start_date_2 < res_2_1.time) & (res_2_1.time < end_date_2)].empty
    assert len(res_2_1) == 3600
    res_2_2 = get_money_flow_pro(security_list,
                                 None,
                                 end_date_2,
                                 frequency='1m',
                                 fields=fields,
                                 count=10)
    print(res_2_2)
    assert res_2_2[res_2_2.time > datetime.datetime(2023, 9, 8, 14, 50)].equals(res_2_2)
    # end_date_2 = datetime.datetime(2023, 7, 10, 16, 0), count=241，应该返回两天的数据
    res_2_3 = get_money_flow_pro(security_list,
                                 None,
                                 end_date_2,
                                 frequency='1m',
                                 fields=fields,
                                 count=241)
    print(res_2_3)
    assert res_2_3[res_2_3.time >= datetime.datetime(2023, 9, 7, 15, 00)].equals(res_2_3)

    # 测试取不规则的跨日历史数据
    start_date_3 = datetime.datetime(2023, 12, 25, 12)
    end_date_3 = datetime.datetime(2024, 1, 5, 14, 30)
    res_3_1 = get_money_flow_pro(security_list,
                                 start_date_3,
                                 end_date_3,
                                 frequency='1m',
                                 fields=fields)
    print(res_3_1)
    assert res_3_1[(res_3_1.time > datetime.datetime(2023, 12, 23, 13)) & (res_3_1.time <= end_date_3)].equals(res_3_1)
    res_3_2 = get_money_flow_pro(security_list,
                                 None,
                                 end_date_3,
                                 frequency='1m',
                                 fields=fields,
                                 count=240)
    print(res_3_2)
    assert res_3_2[res_3_2.time >= datetime.datetime(2024, 1, 3, 14, 31)].equals(res_3_2)

    # # 测试取实时数据
    end_date_4 = datetime.datetime.today()
    start_date_4 = end_date_4 - datetime.timedelta(3)
    res_4_1 = get_money_flow_pro(security_list,
                                 start_date_4,
                                 end_date_4,
                                 frequency='1m',
                                 fields=fields)
    print(res_4_1)
    assert end_date_4.date() in set(dt.date() for dt in res_4_1.time)

    # 测试取交易日当天不存在的标的数据
    res_non_exits_m = get_money_flow_pro(['688981.XSHG'],
                                         datetime.datetime(2020, 7, 12, 8),
                                         datetime.datetime(2020, 7, 14, 8),
                                         frequency='1m',
                                         fields=fields)
    assert res_non_exits_m.empty
