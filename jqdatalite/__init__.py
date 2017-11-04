# coding=utf-8
from __future__ import absolute_import

from .api import *
from .finance_service import *
from .gta import gta


def init(username, password, host="101.200.217.122", port=7000):
    from .client import JQDataClient
    from . import api
    api.data_client = JQDataClient(host=host, port=port, username=username, password=password)
    api.data_client.ensure_auth()


# __all__ = [
#     'attribute_history',
#     'get_all_securities',
#     'get_all_trade_days',
#     'get_concept_stocks',
#     'get_extras',
#     'get_fundamentals',
#     'get_history_name',
#     'get_index_stocks',
#     'get_industry_stocks',
#     'get_ipython',
#     'get_money_flow',
#     'get_mtss',
#     'get_price',
#     'get_security_info',
#     'get_trade_days',
#     'history',
#     'init',
#     "query",
#     "balance",
#     "income",
#     "cash_flow",
#     "indicator",
#     "bank_indicator",
#     "security_indicator",
#     "insurance_indicator",
#     "valuation"
# ]




if __name__ == "__main__":
    import time, datetime
    init("admin", "admin")
    now = datetime.datetime.now()
    # for i in range(1000):
    print(get_price(security=["000001.XSHE", "000002.XSHE"], start_date="2017-10-01", end_date="2017-10-26"))
    print(get_all_trade_days())
    print("use %s" % (datetime.datetime.now() - now))
