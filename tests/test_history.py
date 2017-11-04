#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys

import sys
sys.path.append("..")
from jqdatalite import *

import numpy as np

import pandas as pd
DEFAULT_FIELDS = ['open', 'close', 'high', 'low', 'volume', 'money']

if sys.version_info[0] == 3:
    xrange = range

init("admin", "admin")

def test_history2():
    s = '000001.XSHE'
    s2 = '000002.XSHE'
    current_dt = datetime.date(2016, 1, 6)
    for count in (1, 4, 10):
        for unit in ('1d', '400d'):
            for fq in (None, 'pre', 'post'):
                for use_df in (True, False):
                    for field in DEFAULT_FIELDS:
                        for security_list in ((s,), (s, s2)):
                            history(current_dt, count, unit, field,
                                    security_list, df=use_df, fq=fq,
                                    pre_factor_ref_date=current_dt)


def test_history_minute():
    s = '000001.XSHE'
    dt = datetime.datetime(2015, 12, 15, 9, 30)

    h1 = history(dt, 10, '1m', 'close', s)
    close1 = h1[s].values
    h2 = history(dt, 10, '1m', 'close', s)
    close2 = h2[s].values
    assert (close1 == close2).all()

    assert h2.to_csv() == """\
,000001.XSHE
2015-12-14 14:51:00,12.08
2015-12-14 14:52:00,12.07
2015-12-14 14:53:00,12.07
2015-12-14 14:54:00,12.06
2015-12-14 14:55:00,12.05
2015-12-14 14:56:00,12.05
2015-12-14 14:57:00,12.06
2015-12-14 14:58:00,12.07
2015-12-14 14:59:00,12.07
2015-12-14 15:00:00,12.07
"""
    history(dt, 2, '5m', 'close', s)
    history(dt, 10, '1m', 'open', s)
    history(dt, 10, '1m', 'factor', s)
    history(dt, 10, '1m', 'high_limit', s)
    history(dt, 10, '1m', 'paused', s)
    history(dt, 2, '5m', 'close', s, df=False)
    dt = datetime.datetime(2015, 12, 15, 9, 31)
    history(dt, 2, '5m', 'close', s)
    history(dt, 10, '1m', 'factor', s)
    history(dt, 10, '1m', 'paused', s)
    history(dt, 300, '1m', 'high_limit', s)

    for count in (1, 4, 10):
        for unit, fields in (
                ('1m', ('open', 'close', 'high', 'low', 'high_limit', 'paused',
                        'factor', 'money')),
                ('100m', ('open', 'close', 'high', 'low', 'money'))):
            for dt in (datetime.datetime(2015, 12, 15, 9, 30),
                       datetime.datetime(2015, 12, 15, 9, 31),
                       datetime.datetime(2015, 12, 15, 13, 0)):
                for field in fields:
                    h1 = history(dt, count, unit, field, s,
                                 pre_factor_ref_date=dt).to_csv()
                    h2 = history(dt, count, unit, field, s,
                                 pre_factor_ref_date=dt).to_csv()
                    assert (h1 == h2)


def test_history():
    s = '000001.XSHE'
    dt = datetime.datetime(2015, 12, 15, 9, 30)
    index = pd.DatetimeIndex(['2015-12-01', '2015-12-02', '2015-12-03',
                              '2015-12-04', '2015-12-07', '2015-12-08',
                              '2015-12-09', '2015-12-10', '2015-12-11',
                              '2015-12-14'],
                             dtype='datetime64[ns]', freq=None, tz=None)
    opens = np.array([11.7, 11.7, 12.39, 12.31, 12.18, 12.07, 11.92, 11.95,
                      11.91, 11.73])
    closes = np.array([11.75, 12.51, 12.45, 12.12, 12.15, 11.96, 11.99, 11.96,
                       11.83, 12.07])
    highs = np.array([11.86, 12.64, 12.75, 12.38, 12.25, 12.09, 12.12, 12.14,
                      11.92, 12.11])
    lows = np.array([11.51, 11.66, 12.25, 12.08, 12.04, 11.9, 11.9, 11.91,
                     11.73, 11.71])
    volumes = np.array([68025392, 161576080, 142597680, 76453248, 40279264,
                        50310180, 42938436, 41760360, 37950804, 58723664])
    moneys = np.array([7.93118208e+08, 1.97875046e+09, 1.78600896e+09,
                       9.34906560e+08, 4.88370688e+08, 6.02568640e+08,
                       5.15596480e+08, 5.02326080e+08, 4.48800928e+08,
                       6.98792000e+08])
    calced_avgs = moneys / volumes

    h = history(dt, 10, '1d', 'close', s, df=False)
    assert isinstance(h, dict)
    assert list(h.keys()) == [s]
    assert (h[s] == closes).all()

    assert isinstance(history(dt, 10, '1d', 'close', s,
                              pre_factor_ref_date=dt).index[0],
                      datetime.datetime)
    assert isinstance(history(dt, 1, '10d', 'close', s,
                              pre_factor_ref_date=dt).index[0],
                      datetime.datetime)
    assert isinstance(history(dt, 1, '10m', 'close', s,
                              pre_factor_ref_date=dt).index[0],
                      datetime.datetime)

    h = history(dt, 10, '1d', 'close', s)
    assert (h.index == index).all()
    assert (h[s].values == closes).all()
    assert (history(dt, 10, '1d', 'volume', s
                    )[s].values == volumes).all()

    # test avg and deprecated 'price'
    avgs = history(dt, 10, '1d', 'avg', s)[s].values
    prices = history(dt, 10, '1d', 'price', s
                     )[s].values
    assert (avgs == prices).all()
    assert np.isclose(avgs, calced_avgs, atol=0.005).all()

    h = history(dt, 1, '10d', 'close', s)
    assert (h.index == index[-1:]).all()
    assert h[s][0] == closes[-1]
    assert history(dt, 1, '10d', 'open', s
                   )[s][0] == opens[0]
    assert history(dt, 1, '10d', 'high', s
                   )[s][0] == max(highs)
    assert history(dt, 1, '10d', 'low', s
                   )[s][0] == min(lows)
    assert history(dt, 1, '10d', 'volume', s
                   )[s][0] == sum(volumes)
    # assert history(1, '10d', 'money')[s][0] == sum(moneys)

    # minute
    avgs = history(dt, 10, '1m', 'avg', s)[s].values
    prices = history(dt, 10, '1m', 'price', s
                     )[s].values
    assert (avgs == prices).all()


def test_history3():
    dt = datetime.datetime(2015, 12, 14)
    csv = history(dt, 5, '1d', 'close', ["161207.XSHE", "502000.XSHG"], fq=None
                  ).to_csv()
    print(csv)


def test_history_paused2():
    dt = datetime.datetime(2014, 1, 1)
    s = '600817.XSHG'
    assert history(dt, 150, '1d', 'close', s, fq=None).iloc[[0, -1]].to_csv() == """\
,600817.XSHG
2013-05-22,16.01
2013-12-31,7.4
"""


def test_futures_history():
    s = 'TF1612.CCFX'
    dt = datetime.datetime(2016, 4, 14, 10, 0, 0)
    history(dt, 1, '1d', 'close', s)


# def test_2history():
#     count = 10
#     skip_paused = True
#     fq = None
#     df = True
#     unit = "1d"
#     end_date = datetime.datetime(2005, 1, 18, 10, 30)  # 2015-1-11停牌

#     for count in xrange(1, 3600, 180):
#         for skip_paused in (True, False):
#             for fq in ('pre', 'post', None):
#                 for df in (True, False):
#                     for unit in ("1d", "2d", "5d", "30d", "1m", "2m", "5m",
#                                  "30m"):
#                         history(count, unit=unit,
#                                 field='close',
#                                 security_list='000001.XSHE',
#                                 skip_paused=skip_paused,
#                                 fq=fq,
#                                 df=df)


def test_h4():
    jqdata.set_shm_path('/dev/shm')
    d = datetime.date(2017, 9, 7)
    d1 = datetime.date(2017, 9, 6)
    security_list = jqdata.apis.get_index_stocks('000001.XSHG', d)
    for s in security_list:
        res = jqdata.apis.history(d,
                                  150,
                                  unit="1d",
                                  field="close",
                                  security_list=s,
                                  df=True,
                                  skip_paused=False,
                                  fq='pre',
                                  pre_factor_ref_date=d1)
        print(len(res))
        assert len(res) == 150


# def test_history_commoditie_1():
#     s = 'CU1710.XSGE'
#     s2 = 'IF1709.CCFX'
#     for count in (1, 4, 10):
#         for unit in ('1d', '400d'):
#             for fq in (None, 'pre', 'post'):
#                 for use_df in (True, False):
#                     for field in DEFAULT_FIELDS:
#                         for security_list in ((s,), (s, s2)):
#                             history(count, unit, field,
#                                     security_list, df=use_df, fq=fq)


def test_history_commoditie_2():
    s = 'CU1710.XSGE'
    dt = datetime.datetime(2017, 9, 12, 10, 30)

    h1 = history(dt, 10, '1m', 'close', s)
    close1 = h1[s].values
    h2 = history(dt, 10, '1m', 'close', s)
    close2 = h2[s].values
    assert (close1 == close2).all()
    assert h2.to_csv() == """\
,CU1710.XSGE
2017-09-12 10:06:00,51540.0
2017-09-12 10:07:00,51530.0
2017-09-12 10:08:00,51530.0
2017-09-12 10:09:00,51520.0
2017-09-12 10:10:00,51510.0
2017-09-12 10:11:00,51490.0
2017-09-12 10:12:00,51470.0
2017-09-12 10:13:00,51450.0
2017-09-12 10:14:00,51470.0
2017-09-12 10:15:00,51500.0
"""
    history(dt, 2, '5m', 'close', s)
    history(dt, 10, '1m', 'open', s)
    history(dt, 10, '1m', 'factor', s)
    history(dt, 10, '1m', 'high_limit', s)
    history(dt, 10, '1m', 'paused', s)
    history(dt, 2, '5m', 'close', s, df=False)

    dt = datetime.datetime(2017, 9, 12, 9, 31)
    history(dt, 2, '5m', 'close', s)
    history(dt, 10, '1m', 'factor', s)
    history(dt, 10, '1m', 'paused', s)
    history(dt, 300, '1m', 'high_limit', s)

    for count in (1, 4, 10):
        for unit, fields in (
                ('1m', ('open', 'close', 'high', 'low',
                        'high_limit', 'paused', 'factor', 'money')),
                ('100m', ('open', 'close', 'high', 'low', 'money'))):
            for dt in (datetime.datetime(2017, 9, 12, 9, 30),
                       datetime.datetime(2017, 9, 12, 9, 31),
                       datetime.datetime(2017, 9, 12, 13, 0)):
                for field in fields:
                    h1 = history(dt, count, unit, field, s,
                                 pre_factor_ref_date=dt).to_csv()
                    h2 = history(dt, count, unit, field, s,
                                 pre_factor_ref_date=dt).to_csv()
                    assert (h1 == h2)
    pass


def test_history_commoditie_3():
    s = 'CU1710.XSGE'
    # dt = datetime.datetime(2017, 9, 14, 9, 30)
    dt = datetime.date(2017, 9, 14)
    index = pd.DatetimeIndex(['2017-09-01', '2017-09-04', '2017-09-05',
                              '2017-09-06', '2017-09-07', '2017-09-08',
                              '2017-09-11', '2017-09-12', '2017-09-13'],
                             dtype='datetime64[ns]', freq=None, tz=None)
    opens = np.array([52960., 52530., 53080., 53400.,
                      53030., 52730., 51620., 51700., 51000.])
    closes = np.array([52800., 53150., 53610., 53160.,
                       52720., 51730., 51470., 51620., 50970.])
    highs = np.array([52960., 53400., 53700., 53480.,
                      53280., 52830., 51760., 51880., 51440.])
    lows = np.array([52560., 52500., 53020., 52650.,
                     52620., 51600., 50870., 51360., 50940.])
    volumes = np.array([176536., 215214., 159896., 178124.,
                        157402., 160584., 125468., 83714., 90312.])
    # moneys = np.array([4.65431840e+10, 5.70508676e+10, 4.26556829e+10,
    #                    4.73086969e+10, 4.16803008e+10, 4.20216233e+10,
    #                    3.21795913e+10, 2.15960505e+10, 2.31220733e+10])

    h = history(9, '1d', 'close', s, df=False)
    assert isinstance(h, dict)
    assert list(h.keys()) == [s]
    assert (h[s] == closes).all()

    assert isinstance(history(dt, 9, '1d', 'close', s).index[0],
                      datetime.datetime)
    assert isinstance(history(dt, 1, '9d', 'close', s).index[0],
                      datetime.datetime)

    h = history(dt, 9, '1d', 'close', s)
    assert (h.index == index).all()
    assert (h[s].values == closes).all()
    assert (history(dt, 9, '1d', 'volume', s)
            [s].values == volumes).all()

    # test avg and deprecated 'price'
    avgs = history(dt, 9, '1d', 'avg', s)[s].values
    prices = history(dt, 9, '1d', 'price', s)[s].values
    assert (avgs == prices).all()

    h = history(dt, 1, '9d', 'close', s)
    assert (h.index == index[-1:]).all()
    assert h[s][0] == closes[-1]
    assert history(dt, 1, '9d', 'open', s)[
        s][0] == opens[0]
    assert history(dt, 1, '9d', 'high', s)[
        s][0] == max(highs)
    assert history(dt, 1, '9d', 'low', s)[
        s][0] == min(lows)
    assert history(dt, 1, '9d', 'volume', s)[
        s][0] == sum(volumes)
    # assert history(1, '10d', 'money')[s][0] == sum(moneys)

    # minute
    dt = datetime.datetime(2017, 9, 14, 9, 30)
    avgs = history(dt, 9, '1m', 'avg', s)[s].values
    prices = history(dt, 9, '1m', 'price', s)[s].values
    print(avgs)
    print(prices)
    assert (avgs == prices).all()
    pass


def test_history_commoditie_4():
    dt = datetime.datetime(2017, 9, 12)
    csv = history(dt, 5, '1d', 'close', [
                  "CU1710.XSGE", "IF1709.CCFX"], fq=None).to_csv()
    assert csv == """\
,CU1710.XSGE,IF1709.CCFX
2017-09-05,53610.0,3854.2
2017-09-06,53160.0,3846.6
2017-09-07,52720.0,3828.2
2017-09-08,51730.0,3820.8
2017-09-11,51470.0,3831.4
"""
    pass


def test_history_commoditie_5():
    dt = datetime.datetime(2017, 9, 12)
    s = 'CU1710.XSGE'
    sl = list(history(dt, 15, '1d', 'close', s, fq=None))
    idx = history(dt, 15, '1d', 'close', s, fq=None).iloc[[0, -1]].index.tolist()
    assert sl[0] == 'CU1710.XSGE'
    assert idx[0].date() == datetime.date(2017, 8, 22)
    csv = history(dt, 15, '1d', 'close', s, fq=None).iloc[[0, -1]].to_csv()
    assert csv == """\
,CU1710.XSGE
2017-08-22,52190.0
2017-09-11,51470.0
"""
    pass


def test_history_commoditie_6():
    s = 'CU1710.XSGE'
    dt = datetime.datetime(2017, 9, 12, 10, 0, 0)
    history(dt, 1, '1d', 'close', s)
    pass


def test_history_commoditie_7():
    count = 10
    skip_paused = True
    fq = None
    df = True
    unit = "1d"
    end_date = datetime.datetime(2017, 9, 13, 10, 30)  # 2015-1-11停牌

    for count in xrange(1, 3600, 180):
        for skip_paused in (True, False):
            for fq in ('pre', 'post', None):
                for df in (True, False):
                    for unit in ("1d", "2d", "5d", "30d", "1m", "2m", "5m",
                                 "30m"):
                        history(end_date, count, unit=unit,
                                field='close',
                                security_list='CU1710.XSGE',
                                skip_paused=skip_paused,
                                fq=fq,
                                df=df,
                                pre_factor_ref_date=end_date)
    pass


def test_history_commoditie_8():
    jqdata.set_shm_path('/dev/shm')
    d = datetime.date(2017, 9, 13)
    d1 = datetime.date(2017, 9, 12)
    security_list = ['CU1710.XSGE', 'IF1709.CCFX']
    for s in security_list:
        res = jqdata.apis.history(d,
                                  15,
                                  unit="1d",
                                  field="close",
                                  security_list=s,
                                  df=True,
                                  skip_paused=False,
                                  fq='pre',
                                  pre_factor_ref_date=d1)
        assert len(res) == 15
    pass


if __name__ == "__main__":
    vars = globals()
    if len(sys.argv) >= 2:
        func = sys.argv[1]
        assert func.startswith("test") and func in vars
        print ('run: %s' % func)
        vars[func]()
    else:
        for i in vars.keys():
            if i.startswith("test") and callable(vars[i]):
                print ("run: %s" % i)
                vars[i]()
