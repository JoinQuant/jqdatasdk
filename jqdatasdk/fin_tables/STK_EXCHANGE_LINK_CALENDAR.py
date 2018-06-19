# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EXCHANGE_LINK_CALENDAR(Base):

    __tablename__ = "STK_EXCHANGE_LINK_CALENDAR"

    id = Column(Integer, primary_key=True)
    day = Column(Date, nullable=False, comment="日期")
    link_id = Column(Integer, nullable=False, comment="市场通编码")
    link_name = Column(String(32), nullable=False, comment="市场通名称")
    type_id = Column(Integer, nullable=False, comment="交易日类型编码")
    type = Column(String(32), nullable=False, comment="交易日类型")
