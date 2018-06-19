# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EXCHANGE_LINK_RATE(Base):

    __tablename__ = 'STK_EXCHANGE_LINK_RATE'

    id = Column(Integer, primary_key=True)
    day = Column(Date, nullable=False, comment="日期")
    link_id = Column(Integer, nullable=False, comment="市场通编码(与公共编码表相对应)")
    link_name = Column(String(32), nullable=False, comment="市场通名称")
    domestic_currency = Column(String(12), nullable=False, default="RMB", comment="本币")
    foreign_currency = Column(String(12), nullable=False, default="HKD", comment="外币")
    refer_bid_rate = Column(DECIMAL(10, 5), comment="买入参考汇率")
    refer_ask_rate = Column(DECIMAL(10, 5), comment="卖出参考汇率")
    settle_bid_rate = Column(DECIMAL(10, 5), comment="买入结算汇率")
    settle_ask_rate = Column(DECIMAL(10, 5), comment="卖出结算汇率")
