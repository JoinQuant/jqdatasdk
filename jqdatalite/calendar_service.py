# coding=utf-8
from .client import JQDataClient
from .utils import *


class CalendarService(object):

    all_trade_days = None

    @classmethod
    def get_trade_days(cls, start_date=None, end_date=None, count=None):
        if not cls.all_trade_days:
            start_date = to_date_str(start_date)
            end_date = to_date_str(end_date)
            lst = JQDataClient.instance().get_trade_days(**locals())
            return [to_date(item) for item in lst]
        else:
            start_date = to_date(start_date)
            end_date = to_date(end_date)
            start_idx, end_idx = 0, len(cls.all_trade_days)
            if start_date:
                assert start_date in cls.all_trade_days
                start_idx = cls.all_trade_days.index(start_date)
            if end_date:
                assert end_date in cls.all_trade_days
                end_idx = cls.all_trade_days.index(end_date)
            return cls.all_trade_days[start_idx:end_idx]

    @classmethod
    def get_all_trade_days(cls):
        from .api import get_all_trade_days
        return get_all_trade_days()

    @classmethod
    def get_previous_trade_date(cls, date):
        """
        返回指定日期的最近一个交易日
        如果该日期是交易日，返回该日期；
        否则，返回该日期的前一个交易日
        """
        date = to_date(date)
        if date not in cls.get_all_trade_days():
            temp = filter(lambda item: item < date, cls.all_trade_days)
            temp = list(temp)
            return temp[-1]
        return date


get_trade_days = CalendarService.get_trade_days
get_all_trade_days = CalendarService.get_all_trade_days



