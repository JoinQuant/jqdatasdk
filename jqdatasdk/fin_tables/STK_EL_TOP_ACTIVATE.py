# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EL_TOP_ACTIVATE(Base):

    __tablename__ = "STK_EL_TOP_ACTIVATE"

    id = Column(Integer, primary_key=True)
    day = Column(Date, nullable=False, comment="日期")
    link_id = Column(Integer, nullable=False, comment="市场通编码")
    link_name = Column(String(32), nullable=False, comment="市场通名称")
    rank = Column(Integer, nullable=False, comment="排名")
    code = Column(String(12), nullable=False, comment="股票代码")
    name = Column(String(100), nullable=False, comment="股票名称")
    exchange = Column(String(12), nullable=False, comment="交易所名称")
    buy = Column(DECIMAL(20, 4), comment="买入金额(元)")
    sell = Column(DECIMAL(20, 4), comment="卖出金额(元)")
    total = Column(DECIMAL(20, 4), comment="买入及卖出金额(元)")
