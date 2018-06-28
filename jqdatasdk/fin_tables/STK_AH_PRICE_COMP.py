# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_AH_PRICE_COMP(Base):

    __tablename__ = "STK_AH_PRICE_COMP"

    id = Column(Integer, primary_key=True)
    day = Column(Date, nullable=False, comment="日期")
    name = Column(String(32), nullable=False, comment="股票简称")
    a_code = Column(String(12), nullable=False, comment="A股代码")
    h_code = Column(String(12), nullable=False, comment="H股代码")
    a_price = Column(DECIMAL(10, 4), comment="A股收盘价")
    h_price = Column(DECIMAL(10, 4), comment="H股收盘价")
    a_quote_change = Column(DECIMAL(10, 4), comment="A股涨跌幅(%)")
    h_quote_change = Column(DECIMAL(10, 4), comment="H股涨跌幅(%)")
    h_a_comp = Column(DECIMAL(10, 4), comment="比价(H/A)")
