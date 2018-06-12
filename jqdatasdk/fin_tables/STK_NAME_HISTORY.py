# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_NAME_HISTORY(Base):

    __tablename__ = "STK_NAME_HISTORY"

    id = Column(Integer, primary_key=True)
    code = Column(String(12), nullable=False, comment="股票代码")
    company_id = Column(Integer, comment="公司ID")
    new_name = Column(String(40), comment="新股票简称")
    new_spelling = Column(String(40), comment="新拼音简称")
    org_name = Column(String(40), comment="原股票简称")
    org_spelling = Column(String(40), comment="原股票拼音简称")
    start_date = Column(Date, comment="开始日期")
    pub_date = Column(Date, comment="公布日期")
    reason = Column(String(255), comment="变更原因")
