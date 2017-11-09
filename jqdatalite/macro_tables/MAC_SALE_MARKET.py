# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SALE_MARKET(Base):
    """
    亿元以上商品交易市场基本情况
    """

    __tablename__ = "MAC_SALE_MARKET"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    market_id = Column(Integer, nullable=False)
    market_name = Column(String(128), nullable=False)
    market_num = Column(DECIMAL(20, 4))
    stall_num = Column(DECIMAL(20, 4))
    operation_area = Column(DECIMAL(20, 4))
    turnover = Column(DECIMAL(20, 4))
    turnover_wholesale = Column(DECIMAL(20, 4))
    turnover_retail = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)