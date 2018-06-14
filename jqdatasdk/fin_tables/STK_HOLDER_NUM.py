# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_HOLDER_NUM(Base):

    __tablename__ = 'STK_HOLDER_NUM'

    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False, comment="股票代码")
    end_date = Column(Date, nullable=False, comment="截止日期")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    share_holders = Column(Integer, nullable=False, comment="股东总户数")
    a_share_holders = Column(Integer, nullable=False, comment="A股东总户数")
    b_share_holders = Column(Integer, nullable=False, comment="B股东总户数")
    h_share_holders = Column(Integer, nullable=False, comment="H股东总户数")
