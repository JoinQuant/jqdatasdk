# coding=utf-8
import datetime
from sqlalchemy import Date, Column, Integer, String, Table
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class StockExchangeTradeInfoModel(Base):
    """记录沪深两市股票交易的成交情况，包括市值、成交量，市盈率等情况"""

    __tablename__ = 'STK_EXCHANGE_TRADE_INFO'

    id = Column(Integer, primary_key=True)
    exchange_code = Column(String(12), nullable=False, comment="市场编码")
    exchange_name = Column(String(100), nullable=False, comment="市场名称")
    date = Column(Date, nullable=False,comment="交易日期")
    total_market_cap = Column(DECIMAL(20, 8), comment="市价总值")
    circulating_market_cap = Column(DECIMAL(20, 8), comment="流通市值")
    volume = Column(DECIMAL(20, 4), comment="成交量")
    money = Column(DECIMAL(20, 8), comment="成交金额")
    deal_number = Column(DECIMAL(20, 4), comment="成交笔数")
    pe_average = Column(DECIMAL(20, 4), comment="平均市盈率")
    turnover_ratio = Column(DECIMAL(10, 4), comment="换手率")
