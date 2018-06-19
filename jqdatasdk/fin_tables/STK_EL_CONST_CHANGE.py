# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EL_CONST_CHANGE(Base):

    __tablename__ = "STK_EL_CONST_CHANGE"

    id = Column(Integer, primary_key=True)
    link_id = Column(Integer, nullable=False, comment="市场通编码")
    link_name = Column(String(32), nullable=False, comment="市场通名称")
    code = Column(String(12), nullable=False, comment="证券代码")
    name_ch = Column(String(30), comment="中文简称")
    name_en = Column(String(120), comment="英文简称")
    exchange = Column(String(12), nullable=False, comment="该股票锁在交易所")
    change_date = Column(Date, nullable=False, comment="变更日期")
    direction = Column(String(6), nullable=False, comment="变更方向")
