# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHARES_PLEDGE(Base):

    __tablename__ = 'STK_SHARES_PLEDGE'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    company_name = Column(String(100), nullable=False, comment="公司名称")
    code = Column(String(12), nullable=False, comment="股票代码")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    pledgor_id = Column(Integer, comment="出质人ID")
    pledgor = Column(String(100), comment="出质人")
    pledgee = Column(String(100), comment="质权人")
    pledge_item = Column(String(500), comment="质押事项")
    pledge_nature_id = Column(Integer, comment="质押股份性质编码")
    pledge_nature = Column(String(120), comment="质押股份性质")
    pledge_number = Column(DECIMAL(20, 4), comment="质押数量")
    pledge_total_ratio = Column(DECIMAL(10, 4), comment="占总股本比例")
    start_date = Column(Date, comment="质押起始日")
    end_date = Column(Date, comment="质押终止日")
    unpledged_date = Column(Date, comment="质押解除日")
    unpledged_number = Column(DECIMAL(20, 4), comment="质押解除数量")
    unpledged_detail = Column(String(1000), comment="解除质押说明")
    is_buy_back = Column(String(1), comment="是否质押式回购交易")
