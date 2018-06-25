# coding=utf-8
import sys
import os
sys.modules["ROOT_DIR"] = os.path.abspath(os.path.dirname(__file__))

from .api import *
from .finance_service import *
from .macro import macro
from . import alpha101
from . import alpha191
from . import technical_analysis
from .finance import finance


def auth(username, password, host="39.107.190.114", port=7000):
    from .client import JQDataClient
    JQDataClient.set_auth_params(host=host, port=port, username=username, password=password)


__all__ = [
    "auth",
    "get_price",
    "get_trade_days",
    "get_all_trade_days",
    "get_extras",
    "get_index_stocks",
    "get_industry_stocks",
    "get_industries",
    "get_concept_stocks",
    "get_concepts",
    "get_all_securities",
    "get_security_info",
    "get_money_flow",
    "get_fundamentals",
    "get_fundamentals_continuously",
    "get_billboard_list",
    "get_locked_shares",
    "get_mtss",
    "get_margincash_stocks",
    "get_marginsec_stocks",
    "get_future_contracts",
    "get_dominant_future",
    "normalize_code",
    "query",
    "balance",
    "income",
    "cash_flow",
    "indicator",
    "bank_indicator",
    "security_indicator",
    "insurance_indicator",
    "valuation",
    "macro",
    "alpha101",
    "alpha191",
    "technical_analysis",
    "get_baidu_factor",
    "get_ticks",
    "finance",
]

# __all__.extend(fin.__all__)



