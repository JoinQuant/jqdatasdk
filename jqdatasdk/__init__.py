# coding=utf-8

from .api import *  # noqa
from .table import *  # noqa
from .finance_service import *  # noqa
from . import alpha101
from . import alpha191
from . import technical_analysis
from .client import JQDataClient
from .version import __version__, version_info  # noqa


def auth(username, password, host=None, port=None):
    """账号认证"""
    JQDataClient.set_auth_params(
        host=host,
        port=port,
        username=username,
        password=password,
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
        request_username: 请求的用户名
        request_password: 请求的用户密码
        request_host: 请求的服务器地址
        request_port: 请求的服务器端口
        enable_auth_prompt: 是否输出登录提示信息，默认为 True
    """
    JQDataClient.set_request_params(**params)


__all__ = [
    "auth",
    "logout",
    "is_auth",
    "set_params",
    "alpha101",
    "alpha191",
    "technical_analysis",
    "__version__"
]
__all__.extend(api.__all__)  # noqa
__all__.extend(finance_service.__all__) # noqa
__all__.extend(table.__all__)  # noqa
