# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_WAGE_YEAR(Base):
    """
    分行业城镇单位就业人员工资情况表(年度)
    """

    __tablename__ = "MAC_INDUSTRY_WAGE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    industry_id = Column(Integer, nullable=False)
    industry_name = Column(String(200), nullable=False)
    wage = Column(DECIMAL(20, 4))
    wage_avg = Column(DECIMAL(20, 4))
    employ = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)