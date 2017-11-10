# coding=utf-8
from __future__ import absolute_import

from .api import *
from .finance_service import *
from .gta import gta
from .macro import macro


def init(username, password, host="101.200.217.122", port=7000):
    from .client import JQDataClient
    from . import api
    api.data_client = JQDataClient(host=host, port=port, username=username, password=password)
    api.data_client.ensure_auth()


__all__ = [
    'init',
    "get_price", 
    "history", 
    "attribute_history", 
    "get_trade_days", 
    "get_all_trade_days", 
    "get_extras", 
    "get_index_stocks", 
    "get_industry_stocks", 
    "get_concept_stocks", 
    "get_all_securities",
    "get_security_info", 
    "get_money_flow", 
    "get_fundamentals", 
    "get_mtss", 
    "get_future_contracts", 
    "get_dominant_future", 
    "normalize_code", 
    "read_file", 
    "write_file",
    "query",
    "balance",
    "income",
    "cash_flow",
    "indicator",
    "bank_indicator",
    "security_indicator",
    "insurance_indicator",
    "valuation",
    "gta",
    "macro"
]




if __name__ == "__main__":
    import time, datetime
    init("admin", "admin")
    now = datetime.datetime.now()
    # for i in range(1000):
    print(get_price(security=["000001.XSHE", "000002.XSHE"], start_date="2017-10-01", end_date="2017-10-26"))
    print(get_all_trade_days())
    print("use %s" % (datetime.datetime.now() - now))
