# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_ML_QUOTA(Base):

    __tablename__ = "STK_ML_QUOTA"

    id = Column(Integer, primary_key=True)
    day = Column(Date, nullable=False, comment="日期")
    link_id = Column(Integer, nullable=False, comment="市场通编码(与公共编码表相对应)")
    link_name = Column(String(32), nullable=False, comment="市场通名称")
    currency_id = Column(Integer, nullable=False, comment="货币编码")
    currency_name = Column(String(16), nullable=False, comment="货币名称")
    buy_amount = Column(DECIMAL(20, 4), comment="买入成交额(亿)")
    buy_volume = Column(DECIMAL(20, 4), comment="买入成交数(笔)")
    sell_amount = Column(DECIMAL(20, 4), comment="卖出成交额(亿)")
    sell_volume = Column(DECIMAL(20, 4), comment="卖出成交数(笔)")
    sum_amount = Column(DECIMAL(20, 4), comment="累计成交额(亿) 买入成交额+卖出成交额")
    sum_volume = Column(DECIMAL(20, 4), comment="累计成交数(笔) 买入成交数+卖出成交数")
    quota = Column(DECIMAL(20, 4), comment="总额度(亿)")
    quota_balance = Column(DECIMAL(20, 4), comment="总额度余额(亿)")
    quota_daily = Column(DECIMAL(20, 4), comment="每日额度(亿)")
    quota_daily_balance = Column(DECIMAL(20, 4), comment="每日额度余额(亿)")
