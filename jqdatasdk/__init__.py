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
from .client import JQDataClient


def auth(username, password, host="39.107.190.114", port=7000):
    JQDataClient.set_auth_params(host=host, port=port, username=username, password=password)


def auth_by_token(token, host="39.107.190.114", port=7000):
    JQDataClient.set_auth_params(host=host, port=port, token=token)


def logout():
    JQDataClient.instance().logout()


__version__ = "1.6.7"


__all__ = ["auth", "auth_by_token", "logout", "alpha101", "alpha191", "technical_analysis", "__version__"]
__all__.extend(api.__all__)
__all__.extend(finance_service.__all__)
__all__.extend(table.__all__)
