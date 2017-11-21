#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from jqdatasdk import *

import datetime
import sys

if sys.version_info[0] == 3:
    xrange = range


init("admin", "admin")


s = get_security_info('000001.XSHE')
commoditie = get_security_info('CU1710.XSGE')


def test2():
    st = datetime.date(2014, 1, 1)
    et = datetime.date(2015, 1, 1)
    p = get_price(s, st, et, fields=['open', 'close'])
    assert len(p.index) == 245
    assert len(p.columns) == 2
    p['open']
    p['close']
    # print
    # print(p)
    assert p['close'][datetime.datetime(2014, 1, 10)]
    st = datetime.datetime(2014, 1, 1)
    et = datetime.datetime(2015, 1, 1)
    p = get_price(s, st, et, frequency='1m', fields=[
                  'open', 'close'])
    assert len(p.index) == 58800
    assert len(p.columns) == 2
    p['open']
    p['close']
    # print
    # print(p)


def test3():
    p = get_price(['000001.XSHE', '000300.XSHG'], '2014-01-01',
                  '2015-01-01')
    p['open']
    p['close']
    p['high']
    p['low']
    p['volume']
    p['money']
    df = p['open']
    assert len(df.columns) == 2
    assert len(df.index) == 245
    df['000001.XSHE']
    df['000300.XSHG'][datetime.datetime(2014, 1, 10)]
    pass


def test4():
    get_price('000001.XSHE', '2014-01-01 00:00:00', '2014-02-01',
              fields=['close', 'factor'])
    get_price(['000001.XSHE'], datetime.datetime(2014, 1, 1),
              datetime.date(2014, 2, 1), fields=None)


def test_get_price_minute():
    p = get_price('000001.XSHE', '2014-01-10 09:30:00',
                  '2014-01-11 10:30:00', fields=['price'])
    assert len(p.index) == 1
    p = get_price('000001.XSHE', '2014-01-09 09:30:00', '2014-01-10 15:00:00',
                  frequency='minute', fields=['price'])
    # print p.index
    assert len(p.index) == 480

    p = get_price('000001.XSHE', '2014-01-09 09:30:00', '2014-01-10 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 480

    p = get_price('000001.XSHE', '2014-01-09 00:00:00', '2014-01-09 09:30:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0

    p = get_price('000001.XSHE', '2014-01-09 00:00:00', '2014-01-09 09:31:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 1

    p = get_price('000001.XSHE', '2014-01-09 15:00:00', '2014-01-09 23:00:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 1

    p = get_price('000001.XSHE', '2014-01-09 15:01:00', '2014-01-09 23:00:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0

    p = get_price('000001.XSHE', '2014-01-09 15:00:00', '2014-01-10 09:00:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 1

    p = get_price('000001.XSHE', '2014-01-09 15:01:00', '2014-01-10 09:00:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0


def test_get_price_minute2():
    # 12-17 12-18 有数据 12-21停牌。
    p = get_price('000002.XSHE', '2015-12-17 09:30:00', '2015-12-21 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 480

    p = get_price('000002.XSHE', '2015-12-17 09:30:00', '2015-12-21 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=False)
    # print p.index
    assert len(p.index) == 720

    p = get_price('000002.XSHE', '2015-12-21 09:30:00', '2015-12-21 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 0


def test_get_price_minute3():
    p = get_price(['000001.XSHE', '000002.XSHE'], '2015-12-17',
                  '2015-12-21 23:00:00', frequency='minute', skip_paused=False)
    # print p
    assert len(p['close'].index) == 720
    p = get_price(['000001.XSHE', '000002.XSHE'], '2015-12-22 09:30:00',
                  '2015-12-21 15:00:00', frequency='minute', skip_paused=False)
    # print p
    assert len(p['close'].index) == 0


def test_get_price_minute4():
    p = get_price('000001.XSHE',
                  start_date=datetime.datetime(2016, 6, 6, 10, 0, 0),
                  end_date=datetime.datetime(2016, 6, 6, 11, 0, 0),
                  frequency='1m')

    print(p)
    assert len(p.index) == 61
    p = get_price('000001.XSHE',
                  start_date=str(datetime.datetime(2016, 6, 3, 10, 0, 0)),
                  end_date=str(datetime.datetime(2016, 6, 6, 11, 0, 0)),
                  frequency='1m')
    assert len(p.index) == 301
    pass


def test6():
    p = get_price("000001.XSHE", start_date='2015-12-15',
                  end_date='2015-12-23',
                  frequency='daily', fields='close')
    assert len(p.index) == 7
    pass


def test7():
    # test first day
    p = get_price('000423.XSHE', start_date='2005-01-01',
                  end_date='2005-02-01')
    print (p)
    pass


def test_today():
    get_price("000001.XSHE", start_date='2014-02-01')
    get_price("000300.XSHG", start_date='2014-02-01')


def test_get_price2():
    count = 10
    skip_paused = True
    fq = None
    unit = "1d"
    end_date = datetime.datetime(2005, 1, 18, 10, 30)  # 2015-1-11停牌
    # context.current_dt = end_date
    for count in xrange(1, 3600, 180):
        for skip_paused in (True, False):
            for fq in ('pre', 'post', None):
                for unit in ("1d", "2d", "5d", "30d", "1m", "2m", "5m", "30m"):
                    # print 'end_date=%s, field=%s, count=%s, unit=%s,
                    # skip_paused=%s, fq=%s, df=%s' % (end_date, field, count,
                    # unit, skip_paused, fq, df)
                    get_price('000001.XSHE', end_date=end_date, count=count,
                              frequency=unit,
                              fields=['open', 'close'],
                              skip_paused=skip_paused)
                    # print res


def test_get_price_commoditie_1():
    st = datetime.date(2017, 9, 1)
    et = datetime.date(2017, 9, 14)
    p = get_price(commoditie, st, et, fields=[
                  'open', 'close'])
    assert len(p.index) == 10
    assert len(p.columns) == 2
    p['open']
    p['close']
    # print
    # print(p)
    assert p['close'][datetime.datetime(2017, 9, 12)]
    p = get_price(commoditie, st, et, frequency='1m', fields=[
                  'open', 'close'])
    assert len(p.index) == 4186
    assert len(p.columns) == 2
    p['open']
    p['close']
    pass


def test_get_price_commoditie_2():
    p = get_price(['CU1710.XSGE', 'IF1709.CCFX'], '2017-09-01', '2017-09-14')
    p['open']
    p['close']
    p['high']
    p['low']
    p['volume']
    p['money']
    df = p['open']
    assert len(df.columns) == 2
    assert len(df.index) == 10
    df['CU1710.XSGE']
    df['IF1709.CCFX'][datetime.datetime(2017, 9, 12)]
    pass


def test_get_price_commoditie_3():
    get_price('CU1710.XSGE', '2017-09-01 00:00:00', '2017-09-14',
              fields=['close', 'factor'])
    get_price(['IF1709.CCFX'], datetime.datetime(2017, 9, 1),
              datetime.date(2017, 9, 14), fields=None)
    pass


def test_get_price_commoditie_4():
    p = get_price("CU1710.XSGE", start_date='2017-09-01',
                  end_date='2017-09-14',
                  frequency='daily', fields='close')
    assert len(p.index) == 10
    pass


def test_get_price_commoditie_5():
    get_price('CU1710.XSGE', start_date='2016-01-01', end_date='2017-09-14')
    pass


def test_get_price_commoditie_minute_1():
    p = get_price('IF1709.CCFX', '2017-09-12 09:15:00', '2017-09-12 11:30:00',
                  fields=['price'])
    assert len(p.index) == 1
    p = get_price('IF1709.CCFX', '2017-09-12 09:15:00', '2017-09-12 15:15:00',
                  frequency='minute', fields=['price'])
    # print p.index
    assert len(p.index) == 240

    p = get_price('IF1709.CCFX', '2017-09-12 09:15:00', '2017-09-12 15:15:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 240

    p = get_price('IF1709.CCFX', '2017-09-12 00:00:00', '2017-09-12 09:15:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0

    p = get_price('IF1709.CCFX', '2017-09-12 00:00:00', '2017-09-12 09:16:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0

    p = get_price('IF1709.CCFX', '2017-09-12 15:15:00', '2017-09-12 23:00:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0

    p = get_price('IF1709.CCFX', '2017-09-12 15:16:00', '2017-09-12 23:00:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0

    p = get_price('IF1709.CCFX', '2017-09-12 15:15:00', '2017-09-13 09:15:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0

    p = get_price('IF1709.CCFX', '2017-09-12 15:16:00', '2017-09-13 09:15:00',
                  frequency='minute', fields=['close'])
    # print p.index
    assert len(p.index) == 0
    pass


def test_get_price_commoditie_minute_2():
    p = get_price('CU1710.XSGE', '2017-09-12 00:00:00', '2017-09-12 09:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    assert len(p.index) == 61
    p = get_price('CU1710.XSGE', '2017-09-12 02:30:00', '2017-09-12 09:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 0
    p = get_price('CU1710.XSGE', '2017-09-12 09:00:00', '2017-09-12 10:15:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 75

    p = get_price('CU1710.XSGE', '2017-09-12 10:15:00', '2017-09-12 10:30:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 1

    p = get_price('CU1710.XSGE', '2017-09-12 10:30:00', '2017-09-12 11:30:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 60

    p = get_price('CU1710.XSGE', '2017-09-12 11:30:00', '2017-09-12 13:30:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 1

    p = get_price('CU1710.XSGE', '2017-09-12 13:30:00', '2017-09-12 15:00:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 90

    p = get_price('CU1710.XSGE', '2017-09-12 15:00:00', '2017-09-12 21:00:00',
                  frequency='minute', fields=['close'], skip_paused=False)
    # print p.index
    assert len(p.index) == 1

    p = get_price('CU1710.XSGE', '2017-09-12 21:00:00', '2017-09-13 02:30:00',
                  frequency='minute', fields=['close'], skip_paused=True)
    # print p.index
    assert len(p.index) == 240
    pass


def test_get_price_commoditie_minute_3():
    p = get_price(['CU1710.XSGE'], '2017-09-01 23:00:00',
                  '2017-09-13 23:00:00',
                  frequency='minute', skip_paused=False)
    # print p
    assert len(p['close'].index) == 3721
    p = get_price(['CU1710.XSGE', 'IF1709.CCFX'], '2017-09-13 09:30:00',
                  '2017-09-01 15:00:00', frequency='minute', skip_paused=False)
    # print p
    assert len(p['close'].index) == 0
    pass


def test_get_price_commoditie_minute_4():
    p = get_price('CU1710.XSGE',
                  start_date=datetime.datetime(2017, 9, 13, 10, 0, 0),
                  end_date=datetime.datetime(2017, 9, 13, 11, 0, 0),
                  frequency='1m')

    # print p
    assert len(p.index) == 46
    p = get_price('CU1710.XSGE',
                  start_date=str(datetime.datetime(2017, 9, 1, 10, 0, 0)),
                  end_date=str(datetime.datetime(2017, 9, 13, 11, 0, 0)),
                  frequency='1m')
    assert len(p.index) == 3766
    pass


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
