# coding=utf-8
from .utils import *


class CalendarService(object):

    all_trade_days = None

    @classmethod
    def get_trade_days(cls, start_date=None, end_date=None, count=None):
        if start_date and count:
            raise ParamsError("start_date 参数与 count 参数只能二选一")
        if not (count is None or count > 0):
            raise ParamsError("count 参数需要大于 0 或者为 None")
        start_date = to_date(start_date)
        end_date = to_date(end_date) or today()
        if start_date:
            return [d for d in cls.get_all_trade_days() if start_date <= d <= end_date]
        elif count:
            return [d for d in cls.get_all_trade_days() if d <= end_date][-count:]
        else:
            raise ParamsError("start_date 参数与 count 参数必须输入一个")

    @classmethod
    def get_all_trade_days(cls):
        if not cls.all_trade_days:
            from .api import get_all_trade_days
            cls.all_trade_days = get_all_trade_days() 
        return cls.all_trade_days
        

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


