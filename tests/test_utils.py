from __future__ import print_function

import datetime
from jqdatasdk.utils import to_date_str, to_date
import pytest

def test_date_convert():

    assert to_date_str(None) == None
    assert to_date_str("0001-01-01") == '0001-01-01'
    assert to_date_str(datetime.date(2015, 1, 1)) == '2015-01-01'
    assert to_date_str(datetime.datetime(2015, 1, 1)) == '2015-01-01 00:00:00'
    assert to_date_str(datetime.datetime(2015, 1, 1, 9, 30)) == '2015-01-01 09:30:00'
    assert to_date_str('2015-1-1') == '2015-01-01'
    assert to_date_str('2015-01-01') == '2015-01-01'
    assert to_date_str('2015-11-11 09:30:00') == '2015-11-11 09:30:00'
    assert to_date_str('20190101') == '2019-01-01'
    assert to_date_str('202307010830') == '2023-07-01 08:30:00'
    assert to_date_str('20230701083059') == '2023-07-01 08:30:59'
    assert to_date_str(20190101) == '2019-01-01'
    assert to_date_str(202307010830) == '2023-07-01 08:30:00'
    assert to_date_str(20230701083059) == '2023-07-01 08:30:59'
    assert to_date_str(b'20230101') == '2023-01-01'

    assert to_date(None) == None
    assert to_date(b'20230101') == datetime.date(2023, 1, 1)
    assert to_date(datetime.date(2015, 1, 1)) == datetime.date(2015, 1, 1)
    assert to_date(datetime.datetime(2015, 1, 1)) == datetime.date(2015, 1, 1)
    assert to_date(datetime.datetime(2015, 1, 1, 9, 30)) == datetime.date(2015, 1, 1)
    assert to_date('2015-01-01 09:30:00') == datetime.date(2015, 1, 1)
    assert to_date('2015-1-1') == datetime.date(2015, 1, 1)
    assert to_date('20190101') == datetime.date(2019, 1, 1)
    assert to_date('202307010830') == datetime.date(2023, 7, 1)
    assert to_date('20230701083059') == datetime.date(2023, 7, 1)
    assert to_date(20190101) == datetime.date(2019, 1, 1)
    assert to_date(202307010830) == datetime.date(2023, 7, 1)
    assert to_date(20230701083059) == datetime.date(2023, 7, 1)

    illegal_dt_list = ["Sep/2/2023 09:30:00", "time", "99999999"]
    for dt in illegal_dt_list:
        with pytest.raises(ValueError):
            to_date(dt)

    illegal_dt_list = ["Sep/2/2023 09:30:00", "time", "99999999"]
    for dt in illegal_dt_list:
        with pytest.raises(ValueError):
            to_date_str(dt)