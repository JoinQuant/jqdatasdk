# coding: utf-8
import time
import re
import datetime
import logging
import pytest
import numpy as np
import pandas as pd
from jqdatasdk import *

logging.basicConfig()
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
    assert len(get_industry_stocks('C21', datetime.date(2010, 1, 1))) == 4
    assert len(get_industry_stocks('C21', datetime.date(2015, 1, 1))) == 5
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
    assert len(get_concept_stocks('GN116', datetime.date(2012, 6, 5))) == 0
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

    with pytest.raises(Exception, match="start_date 参数与 count 参数只能二选一"):
        get_extras('is_st', ['000001.XSHE', '000018.XSHE'], '2015-02-02', '2013-12-03', count=10)
    with pytest.raises(Exception, match="start_date 参数与 count 参数只能二选一"):
        get_extras('acc_net_value', 'IC1509.CCFX', start_date='2015-01-01', count=10)
    with pytest.raises(Exception, match="start_date 参数与 count 参数只能二选一"):
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
    # 传入两个重复股票
    get_price(['000001.XSHE', '000001.XSHE'], start_date=datetime.date(2015, 1, 1), end_date=datetime.date(2015, 2, 1), frequency='daily', fields=(u'open', 'close', 'paused'))
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

    df = get_price('000001.XSHE')
    assert 5 == df[df.index < '2015-01-10'].shape[0]


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
    df = get_industry("000001.XSHE", date="2018-12-03")
    assert set(df["000001.XSHE"].keys()) == set(['sw_l1', 'sw_l2', 'sw_l3', 'zjw', 'jq_l2', 'jq_l1',])

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
    assert len(alpha101.alpha_001('2017-03-10', '000001.XSHG')) > 0
    assert len(alpha101.alpha_101('2017-03-10', index='all')) > 0


def test_alpha191():
    assert len(alpha191.alpha_001("000001.XSHE", end_date="2017-03-10")) > 0
    time.sleep(1)
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

    assert technical_analysis.CCI("000001.XSHE", datetime.date(2018, 10, 8)) == {'000001.XSHE': 54.21853388658356}


def test_macro():
    q = query(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR).filter(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR.stat_year=='2014')
    df = macro.run_query(q)
    assert len(df) == 33


def test_ticks():
    assert len(get_ticks("CU1901.XSGE", end_dt="2018-03-16", count=100)) == 100
    assert get_ticks("CU1901.XSGE", end_dt="2018-03-16", count=10, fields=["current", "volume", "position", "a1_v", "a1_p", "b1_v", "b1_p"]).shape == (10, 7)
    assert len(get_ticks("000001.XSHE", end_dt="2018-03-16", count=10)) == 10
    assert str(get_ticks("SM1809.XZCE", '2018-07-06', '2018-07-07').iloc[3][0]) == '2018-07-06 09:00:01.500000'
    assert get_ticks("000001.XSHE", end_dt="2018-03-16", count=10, fields=["a1_v", "a2_v", "a3_v", "a4_v", "a5_v", "b1_v", "b2_v", "b3_v", "b4_v", "b5_v"]).shape == (10, 10)


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


def test_trade_days():
    data1 = get_trade_days("2015-06-30")
    assert str(data1.dtype) == "object"
    assert type(data1) == np.ndarray
    data2 = get_all_trade_days()
    assert str(data2.dtype) == "object"
    assert type(data2) == np.ndarray


def test_get_bars():
    assert len(get_bars("000002.XSHE", end_dt="2018-10-19", count=10)) == 10
    assert get_bars("000001.XSHE", count=5, end_dt="2018-10-15").to_csv().replace('\r', '') == (
        ',date,open,high,low,close\n0,2018-10-08,10.7,10.79,10.45,10.45\n1,2018-10-09,10.46,10.7,10.39,10.56\n2,2018-10-10,10.54,10.66,10.38,10.45\n3,2018-10-11,10.05,10.16,9.7,9.86\n4,2018-10-12,9.97,10.34,9.87,10.3\n'
    )


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
        assert get_current_tick('000002.XSHE') == None
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
    assert df[1].to_dict() == {datetime.date(2015, 1, 5): 0.0,
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
                               datetime.date(2017, 12, 31): 0.18990079481373812}


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
