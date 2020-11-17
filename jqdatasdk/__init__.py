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
from .client import (
    JQDataClient,
    AnalysisDNS,
    is_pandas_version_25,
    get_pandas_notice
)

__version__ = "1.8.3"


def auth(username, password, host=None, port=None):
    """账号认证"""
    JQDataClient.set_auth_params(
        host=host,
        port=port,
        username=username,
        password=password,
        version=__version__
    )


def auth_by_token(token, host=None, port=None):
    """使用 token 认证账号"""
    JQDataClient.set_auth_params(host=host, port=port, token=token)


def logout():
    """退出账号"""
    JQDataClient.instance().logout()


def is_auth():
    """账号是否已经认证"""
    if not JQDataClient.instance():
        return False
    return not JQDataClient.instance().not_auth


def set_params(**params):
    """设置请求参数

    参数说明：
        request_timeout: 请求超时时间，单位为秒，默认为 300 秒，值不能超过 300 秒
                         该值建议在账户认证前设置，否则可能会不生效
        request_attempt_count: 请求的尝试的次数，用于网络异常时重试，默认为 3 次，
                         该次数不能超过 10 次
    """
    JQDataClient.set_request_params(**params)


try:
    if is_pandas_version_25():
        print(get_pandas_notice())

    analysis_dns = AnalysisDNS()
    analysis_dns.start()
except Exception:
    pass

__all__ = [
    "auth",
    "auth_by_token",
    "logout",
    "is_auth",
    "set_params",
    "alpha101",
    "alpha191",
    "technical_analysis",
    "__version__"
]
__all__.extend(api.__all__)
__all__.extend(finance_service.__all__)
__all__.extend(table.__all__)
