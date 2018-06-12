# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_STATUS_CHANGE(Base):

    __tablename__ = 'STK_STATUS_CHANGE'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    code = Column(String(12), nullable=False, comment="证券代码")
    name = Column(String(40), comment="证券简称")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    public_status_id = Column(Integer, nullable=False, comment="上市状态编码")
    public_status = Column(String(32), comment="上市状态")
    change_date = Column(Date, nullable=False, comment="变更日期")
    change_reason = Column(String(500), comment="变更原因")
    change_type_id = Column(Integer, comment="变更类型编码")
    change_type = Column(String(60), comment="变更类型")
    comments = Column(String(255), comment="备注")
