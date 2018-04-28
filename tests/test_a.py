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


auth("17600200652", "19950101", "101.200.217.122")


def test_get_fundamentals_continuously():
    df = get_ticks("NI1804.XSGE", end_dt="2018-03-16", count=10,
              fields=["current", "volume", "position", "a1_v", "a1_p", "b1_v", "b1_p"])
    print(df)


def test_ta():
    # security_list = "000001.XSHE"
    check_date = "2017-10-30"
    timeperiod = 20
    security_list = ["000001.XSHE", "600000.XSHG"]
    data = technical_analysis.BIAS_36(security_list, check_date, M=12)
    assert len(data) == 3
    assert isinstance(data, tuple)
    assert isinstance(data[0], dict) and [i for i in data[0].keys()] == security_list

if __name__ == '__main__':
    # test_get_fundamentals_continuously()
    test_ta()