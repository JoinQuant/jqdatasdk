# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_FIXED_INVEST(Base):
    """
    分行业固定资产投资情况
    """
    __tablename__ = "MAC_INDUSTRY_FIXED_INVEST"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    item_name = Column(String(100), nullable=False)
    investment_value = Column(DECIMAL(20, 4))
    investment_perc = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)