# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_LIST(Base):

    __tablename__ = 'STK_LIST'

    id = Column(Integer, primary_key=True)
    code = Column(String(12), nullable=False, comment="证券代码")
    name = Column(String(40), nullable=False, comment="证券简称")
    short_name = Column(String(20), nullable=False, comment="拼音简写")
    category = Column(String(4), nullable=False, comment="证券类别")
    exchange = Column(String(12), nullable=False, comment="交易所")
    start_date = Column(Date, nullable=False, comment="上市日期")
    end_date = Column(Date, comment="终止上市日期")
    company_id = Column(Integer, nullable=False, comment="公司ID")
    company_name = Column(String(100), comment="公司名称")
    ipo_shares = Column(DECIMAL(20, 2), comment="初始上市数量(股)")
    book_price = Column(DECIMAL(20, 4), comment="发行价格")
    par_value = Column(DECIMAL(20, 4), comment="面值")
    state_id = Column(Integer, comment="上市状态编码")
    state = Column(String(32), comment="上市状态")
