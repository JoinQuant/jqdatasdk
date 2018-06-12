# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EMPLOYEE_INFO(Base):

    __tablename__ = 'STK_EMPLOYEE_INFO'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    code = Column(String(12), nullable=False, comment="公司主证券代码")
    name = Column(String(64), comment="证券名称")
    end_date = Column(Date, nullable=False, comment="截止日期")
    pub_date = Column(Date, comment="公告日期")
    employee = Column(Integer, comment="在职员工总数(人)")
    retirement = Column(Integer, comment="离退休人员(人)")
    graduate_rate = Column(DECIMAL(10, 4), comment="研究生以上人员比例(%)")
    college_rate = Column(DECIMAL(10, 4), comment="大学专科以上人员比例(%)")
    middle_rate = Column(DECIMAL(10, 4), comment="中专及以下人员比例(%)")
