# coding: utf-8
import sys
from jqdatasdk import *
import unittest
import datetime
import os
import six
import logging
import numpy as np
import pandas as pd
logging.basicConfig()
import pytest
log = logging

with open("/home/server/etc/jqdatasdk/import_debug_account.py") as f:
    exec(f.read())


def test_get_index_stocks():
    assert len(get_index_stocks('000300.XSHG')) == 300
    assert len(get_index_stocks('000300.XSHG', '2015-11-01')) == 300
    assert len(get_index_stocks('000300.XSHG', datetime.date.today())) == 300
    assert len(get_index_stocks('000300.XSHG', datetime.datetime.now())) == 300
    pass


def test_get_industry_stocks():
    assert len(get_industry_stocks('A01')) > 0
    assert len(get_industry_stocks('C21', datetime.date(2010, 1, 1))) == 3
    assert len(get_industry_stocks('C21', datetime.date(2015, 1, 1))) == 6
    assert len(get_industry_stocks("HY450", datetime.date(2015, 1, 1))) > 0
    assert len(get_industry_stocks("HY405", datetime.date(2015, 12, 12))) > 0
    assert len(get_industry_stocks("HY500", datetime.date(2012, 12, 12)))
    assert len(get_industry_stocks("851521", datetime.date(2012, 12, 12)))
    assert len(get_industry_stocks("850333", datetime.date(2014, 12, 12)))
    pass


def test_get_industry_stocks2():
    with pytest.raises(Exception) as e:
        get_industry_stocks('XXX')
    with pytest.raises(Exception) as e:
        get_industry_stocks(123)

    stocks = get_industry_stocks("HY405", datetime.date(2012, 12, 12))
    assert '300132.XSHE' in stocks
    with pytest.raises(ValueError) as e:
        stocks.index("600714.XSHG")
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

    assert get_concept_stocks('GN001').__len__() > 0
    assert len(get_concept_stocks('gn001', date=datetime.date(2015, 5, 5))) > 0
    assert len(get_concept_stocks('GN001', date=datetime.date(2016, 1, 1))) > 0
    assert len(get_concept_stocks('GN075')) > 0
    assert len(get_concept_stocks('GN116', datetime.date(2012, 6, 5)))
    assert len(get_concept_stocks('GN146', datetime.date(2015, 1, 1)))
    assert len(get_concept_stocks('GN201', datetime.date.today()))
    assert get_concept_stocks("GN116", datetime.date(2005, 1, 1)) == []


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

    with pytest.raises(Exception, message="start_date 参数与 count 参数只能二选一"):
        get_extras('is_st', ['000001.XSHE', '000018.XSHE'], '2015-02-02', '2013-12-03', count=10)
    with pytest.raises(Exception, message="start_date 参数与 count 参数只能二选一"):
        get_extras('acc_net_value', 'IC1509.CCFX', start_date='2015-01-01', count=10)
    with pytest.raises(Exception, message="start_date 参数与 count 参数只能二选一"):
        get_extras('acc_net_value', 'IC1509.CCFX', start_date='2015-01-01', df=False, count=10)


def test_sec_info():
    res = {'display_name': u'\u5e73\u5b89\u94f6\u884c',
           'name': u'PAYH',
           'parent': None,
           'end_date': datetime.date(2200, 1, 1),
           'type': 'stock',
           'start_date': datetime.date(1991, 4, 3)}
    info = get_security_info('000001.XSHE')
    for f in res:
        assert getattr(info, f) == res[f]
    assert get_security_info('000001.XSHE').type == 'stock'
    assert get_security_info('510300.XSHG').type == 'etf'
    assert get_security_info('510300.XSHG').parent is None
    assert get_security_info('502050.XSHG').parent == '502048.XSHG'


def test_normalize_code():
    for code in (1, '000001', 'SZ000001', '000001SZ', '000001.sz', '000001.XSHE'):
        assert '000001.XSHE' == normalize_code(code)
    for code in (600000, '600000', 'SH600000', '600000.XSHG'):
        assert '600000.XSHG' == normalize_code(code)
    assert 'IF1607.CCFX' == normalize_code('IF1607.CCFX')
    pass


def round_df(df, decimal):
    return np.round(df, decimal)


def test_get_price():

    day_columns = 'open close high low volume money pre_close high_limit low_limit paused avg factor'.split()

    get_price('000300.XSHG')
    get_price(u'000300.XSHG')
    get_price('000001.XSHE', start_date=datetime.date(2015, 1, 1), end_date=datetime.date(
        2015, 2, 1), frequency='daily', fields=(u'open', 'close', 'paused', 'factor'))
    get_price('000001.XSHE', start_date=datetime.datetime(2015, 1, 1),
              end_date=datetime.datetime(2015, 2, 1), frequency='daily', fields=[u'open', 'close'])
    get_price('000001.XSHE', start_date=datetime.datetime(2015, 1, 1),
              end_date=datetime.datetime(2015, 2, 1), frequency='daily', fields='open')
    assert get_price('000001.XSHE', start_date='2015-01-01', end_date='2015-02-01', frequency='1d',
                     fq=None).to_csv() == \
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
    assert round_df(get_price('000002.XSHE', fields=day_columns, start_date='2014-12-30',
                              end_date='2015-01-06', fq=None), 12).to_csv() == \
        """,open,close,high,low,volume,money,pre_close,high_limit,low_limit,paused,avg,factor
2014-12-30,12.45,12.64,13.15,12.19,386124416.0,4894974976.0,12.43,13.67,11.19,0.0,12.68,1.0
2014-12-31,12.6,13.9,13.9,12.46,489954464.0,6494929920.0,12.64,13.9,11.38,0.0,13.26,1.0
2015-01-05,14.39,14.91,15.29,14.22,656083584.0,9700711424.0,13.9,15.29,12.51,0.0,14.79,1.0
2015-01-06,14.6,14.36,14.99,14.05,334634688.0,4839616000.0,14.91,16.4,13.42,0.0,14.46,1.0
"""
    assert get_price(['000001.XSHE', '000002.XSHE'], fields='close', start_date='2014-12-30',
                     end_date='2015-01-06', fq=None)['close'].to_csv() == \
        """,000001.XSHE,000002.XSHE
2014-12-30,15.5,12.64
2014-12-31,15.84,13.9
2015-01-05,16.02,14.91
2015-01-06,15.78,14.36
"""
    df = get_price('000001.XSHE', frequency='5d', start_date='2014-12-01', end_date='2015-01-20', fq=None)
    assert df.to_csv() == \
        """,open,close,high,low,volume,money
2014-12-05,12.6,14.53,15.23,12.08,1981703360.0,26377940992.0
2014-12-12,14.21,13.94,15.53,13.02,1538351152.0,22132453632.0
2014-12-19,13.75,15.0,15.67,13.27,1307583232.0,19036847360.0
2014-12-26,14.9,15.1,16.16,13.68,1170986224.0,17439384832.0
2015-01-06,15.61,15.78,16.39,14.75,1237915024.0,19400459776.0
2015-01-13,15.56,14.68,15.87,14.5,798650072.0,12096269696.0
2015-01-20,14.78,13.83,15.62,13.56,768918808.0,11241922304.0
"""

    get_price('000300.XSHG', fields='price')
    pass


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

    assert get_price('000001.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq=None).iloc[[0, -2, -1]].to_csv() == """\
,open,close,high,low,volume,money
2005-01-04,6.59,6.52,6.59,6.46,1760832.0,11465603.0
2015-12-30,12.09,12.1,12.11,11.95,53266704.0,641277248.0
2015-12-31,12.1,11.99,12.13,11.98,49125892.0,591643584.0
"""

    assert get_price('000001.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq=None).iloc[[0, -2, -1]].to_csv() == """\
,open,close,high,low,volume,money
2005-01-04,6.59,6.52,6.59,6.46,1760832.0,11465603.0
2015-12-30,12.09,12.1,12.11,11.95,53266704.0,641277248.0
2015-12-31,12.1,11.99,12.13,11.98,49125892.0,591643584.0
"""

    assert get_price('000001.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq='post').iloc[[0, -2, -1]].to_csv() == """\
,open,close,high,low,volume,money
2005-01-04,179.52,177.62,179.52,175.98,64637.0,11465603.0
2015-12-30,1132.34,1133.27,1134.21,1119.23,568730.0,641277248.0
2015-12-31,1133.27,1122.97,1136.08,1122.03,524519.0,591643584.0
"""

    # 2015-12-18停牌了
    assert get_price('000002.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq=None).iloc[[0, -2, -1]].to_csv() == """\
,open,close,high,low,volume,money
2005-01-04,5.22,5.27,5.31,5.17,10353811.0,54514225.0
2015-12-17,20.38,22.21,22.21,20.35,258339264.0,5616476672.0
2015-12-18,22.4,24.43,24.43,21.66,223898400.0,5288950784.0
"""

    assert get_price('000002.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=False, fq=None).iloc[[0, -2, -1]].to_csv() == """\
,open,close,high,low,volume,money
2005-01-04,5.22,5.27,5.31,5.17,10353811.0,54514225.0
2015-12-30,24.43,24.43,24.43,24.43,0.0,0.0
2015-12-31,24.43,24.43,24.43,24.43,0.0,0.0
"""

    # 2015-11-02退市了
    assert get_price('000033.XSHE', start_date='2000-01-01', end_date='2015-12-31', skip_paused=True, fq=None).iloc[[0, -2, -1]].to_csv() == """\
,open,close,high,low,volume,money
2005-01-04,3.68,3.71,3.74,3.63,221902.0,815076.0
2015-04-28,9.89,9.89,9.89,9.89,837617.0,8284032.0
2015-04-29,10.38,10.38,10.38,10.38,8184168.0,84951664.0
"""

    assert get_price('000033.XSHE', start_date='2000-01-01', end_date='2015-11-3', skip_paused=False, fq=None).iloc[[0, -2, -1]].to_csv() == """\
,open,close,high,low,volume,money
2005-01-04,3.68,3.71,3.74,3.63,221902.0,815076.0
2015-11-02,10.38,10.38,10.38,10.38,0.0,0.0
2015-11-03,10.38,10.38,10.38,10.38,0.0,0.0
"""

    #       display_name    name    start_date  end_date    type
    # 600472.XSHG 包头铝业    BTLY    2005-05-09  2007-12-26  stock
    assert get_price('600472.XSHG', start_date='2000-01-01', end_date='2007-12-27', skip_paused=False, fq=None).iloc[[0, -2, -1]].to_csv() == """\
,open,close,high,low,volume,money
2005-01-04,,,,,,
2007-12-26,51.82,51.82,51.82,51.82,0.0,0.0
2007-12-27,,,,,,
"""

    print(get_price('000002.XSHE', end_date='2016-12-31', skip_paused=False)[-2:])

    print(get_price([], end_date='2016-12-31', skip_paused=False)['open'][-2:])


def test_get_price_minute():
    print(get_price('000001.XSHE', start_date='2015-01-01', end_date=u'2015-02-01',
                    frequency=u'60m', fields=(u'open', 'close')))
    pass


def test_get_price_minute1():
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
                  '2015-12-21 23:00:00', frequency='minute', skip_paused=False)
    assert len(p['close'].index) == 720
    p = get_price(['000001.XSHE', '000002.XSHE'], '2015-12-22 09:30:00',
                  '2015-12-21 15:00:00', frequency='minute', skip_paused=False)
    assert len(p['close'].index) == 0


def test_finance_basic():
    df = get_fundamentals(query(income.day).limit(10))
    assert len(df.index) == 10


def test_pd_datetime():
    df = get_all_securities()
    assert 2873 == len(df[df['start_date'] < "2016-01-01"].index)
    assert 2873 == len(df[df['start_date'] < "2016-01-01"].index)

    df = get_price('000001.XSHE')
    assert 5 == len(df[df.index < '2015-01-10'].index)
    assert 5 == len(df[df.index < "2015-01-10"].index)
    pass


def test_log():
    log.debug('debug')
    log.info('info')
    log.warn('warn')
    log.error('error')


def test_get_fundamentals():
    df = get_fundamentals(query(income.day).limit(10), date='2016-07-01')
    assert isinstance(df, pd.DataFrame)
    assert len(df.index) == 10
    df = get_fundamentals(query(income.day).limit(10))
    assert(len(df.index)) == 10
    with pytest.raises(Exception) as e:
        get_fundamentals(query(income.day).limit(10), date='2016-07-01', statDate='2016-07-01')
    pass


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


def test_get_fundamentals_continuously():
    # with date
    df = get_fundamentals_continuously(
        query(income.pubDate).filter(income.code == '000001.XSHE'), datetime.date(2015, 1, 1), 10)
    assert isinstance(df, pd.Panel)
    assert len(df.major_axis) == 10
    assert '000001.XSHE' in list(df['pubDate'])
    assert list(df.major_axis) == ['2014-12-18', '2014-12-19', '2014-12-22', '2014-12-23', '2014-12-24',
                                   '2014-12-25', '2014-12-26', '2014-12-29', '2014-12-30', '2014-12-31']

    # yearly
    df = get_fundamentals_continuously(query(valuation.day, balance.code, cash_flow.code, income.code,
                                             indicator.code).
                                       filter(cash_flow.code.in_(['000001.XSHE', '000002.XSHE'])),
                                              datetime.date(2015, 1, 1), 60)
    assert isinstance(df, pd.Panel)
    assert len(df.major_axis) == 60
    assert list(df.minor_axis) == ['000001.XSHE', '000002.XSHE']

    # indicator
    df = get_fundamentals_continuously(query(indicator).filter(indicator.code == '000001.XSHE'), '2015-10-15', 10)
    assert isinstance(df, pd.Panel)
    assert len(df.major_axis) == 10
    assert list(df['inc_net_profit_to_shareholders_annual']) == ['000001.XSHE']
    assert list(df['inc_net_profit_to_shareholders_annual']['000001.XSHE']) == [5.81 for i in range(0, 10)]


def test_get_industries():
    df = get_industries('sw_l1')
    assert len(df.index) > 0


def test_get_concepts():
    df = get_concepts()
    assert len(df.index) > 0


def test_get_margincash_stocks():
    get_margincash_stocks()
    assert len(get_margincash_stocks('2016-12-01')) > 0


def test_get_marginsec_stocks():
    get_marginsec_stocks()
    assert len(get_marginsec_stocks('2016-12-01')) > 0


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
    pass


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
    assert len(alpha101.alpha_001('2017-03-10', '000300.XSHG')) > 0
    assert len(alpha101.alpha_101('2017-03-10', index='all')) > 0


def test_alpha191():
    assert len(alpha191.alpha_001("000001.XSHE", end_date="2017-03-10")) > 0
    assert len(alpha191.alpha_010("000001.XSHE", end_date="2017-03-10")) > 0


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


def test_macro():
    q = query(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR).filter(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR.stat_year=='2014')
    df = macro.run_query(q)
    assert len(df) == 31


def test_ticks():
    assert len(get_ticks("NI1804.XSGE", end_dt="2018-03-16", count=100)) == 100
    assert get_ticks("NI1804.XSGE", end_dt="2018-03-16", count=10, fields=["current", "volume", "position", "a1_v", "a1_p", "b1_v", "b1_p"]).shape == (10, 7)
    assert len(get_ticks("000001.XSHE", end_dt="2018-03-16", count=10)) == 10
    assert get_ticks("000001.XSHE", end_dt="2018-03-16", count=10, fields=["a1_v", "a2_v", "a3_v", "a4_v", "a5_v", "b1_v", "b2_v", "b3_v", "b4_v", "b5_v"]).shape == (10, 10)


def test_billboard_list():
    hs_300 = get_index_stocks('000300.XSHG', '2016-01-10')
    assert len(get_billboard_list(stock_list="300738.XSHE", end_date="2018-03-26", count=5)) == 22
    df = get_billboard_list(hs_300, '2016-01-10', '2017-5-10', None)
    assert len(df) > 0
    stock_list = set(list(df['code']))
    assert len(stock_list) > 71
    assert '000776' in stock_list
    assert '300017' in stock_list
    df = get_billboard_list(hs_300, None, '2017-5-10', 100)
    assert len(df) > 500
    df = get_billboard_list(None, None, '2017-5-10', 100)
    assert len(df) > 30000
    with pytest.raises(Exception, message="get_billboard_list 不能同时指定 start_date 和 count 两个参数"):
        get_billboard_list(hs_300, '2016-01-10', '2017-5-10', 100)
    with pytest.raises(Exception, message="get_billboard_list 必须指定 start_date 或 count 之一"):
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
    with pytest.raises(Exception, message="get_locked_shares 不能同时指定 end_date 和 forward_count 两个参数"):
        get_locked_shares(hs_300, '2017-01-10', '2018-5-10', 200)
    with pytest.raises(Exception, message="get_locked_shares 必须指定 end_date 或 forward_count 之一"):
        get_locked_shares(hs_300, '2017-01-10', None, None)


def test_baidu_factor():
    import datetime
    dates = datetime.date(2017, 11, 20)
    assert len(get_baidu_factor("csi800", day="2017-11-20", stock="000552", province=620000)) == 1
    assert len(get_baidu_factor("csi800", day="2017-11-20", stock=["000552", "000001"], province=620000)) == 2
    assert len(get_baidu_factor("csi800", day="2017-11-20", stock="000552", province="甘肃")) == 1
    assert get_baidu_factor("csi800", day="2017-11-20", stock="000552")["pc_count"][0] == 104.0
    assert get_baidu_factor("csi800", day="2017-11-20", stock="000552.XSHE")["pc_count"][0] == 104.0
    assert len(get_baidu_factor("csi800", day="2017-11-20", stock=["000552.XSHE", "000001.XSHE"])) == 2
    assert len(get_baidu_factor("csi800", day="2017-11-20")) == 800
    assert len(get_baidu_factor("csi800", day=dates)) == 800
    with pytest.raises(Exception, message="目前只支持中证800的搜索量，代码为csi800"):
        get_baidu_factor(day="2017-11-20")


def test_finance_tables():
    # lazy load table of finance
    assert len(finance.__dict__) == 2
    finance.STK_LIST
    assert len(finance.__dict__) > 30
    assert finance.STK_LIST != None
    assert finance.STK_MONEY_FLOW != None
    with pytest.raises(Exception, message='finance 没有该表'):
        finance.STK


if __name__ == "__main__":

    glo = globals()
    if len(sys.argv) >= 2:
        func = sys.argv[1]
        assert func.startswith("test") and func in glo
        print ('run: %s' % func)
        glo[func]()
    else:
        keys = list(glo.keys())
        for i in keys:
            if i.startswith("test") and callable(glo[i]):
                print ("run: %s" % i)
                glo[i]()
