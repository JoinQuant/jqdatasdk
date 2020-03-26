# coding=utf-8
import sys
import os
sys.modules["ROOT_DIR"] = os.path.abspath(os.path.dirname(__file__))

from .api import *
from .finance_service import *
from . import alpha101
from . import alpha191
from . import technical_analysis
from .table import *
from .client import JQDataClient, AnalysisDNS, is_pandas_version_25

__version__ = "1.8.0"

def auth(username, password, host="39.107.190.114", port=7000):
    JQDataClient.set_auth_params(host=host, port=port, username=username, password=password, version=__version__)

def auth_by_token(token, host="39.107.190.114", port=7000):
    JQDataClient.set_auth_params(host=host, port=port, token=token)

def logout():
    JQDataClient.instance().logout()

def is_auth():
    if not JQDataClient.instance():
        return False
    return not JQDataClient.instance().not_auth

if is_pandas_version_25():
    print("提示：当前环境pandas版本为0.25，get_price与get_fundamentals_continuously接口panel参数将固定为False\n注意：0.25以上版本pandas不支持panel，如使用该数据结构和相关函数请注意修改")

analysis_dns = AnalysisDNS()
analysis_dns.start()

__all__ = ["auth", "auth_by_token", "logout", "is_auth", "alpha101", "alpha191", "technical_analysis", "__version__"]
__all__.extend(api.__all__)
__all__.extend(finance_service.__all__)
__all__.extend(table.__all__)
