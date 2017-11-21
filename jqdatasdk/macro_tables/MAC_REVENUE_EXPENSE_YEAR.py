# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REVENUE_EXPENSE_YEAR(Base):
    """
    居民人均收入支出表(年度)
    """
    __tablename__ = "MAC_REVENUE_EXPENSE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    category = Column(String(100), nullable=False)
    income = Column(DECIMAL(20, 4))
    wage_income = Column(DECIMAL(20, 4))
    business_income = Column(DECIMAL(20, 4))
    property_income = Column(DECIMAL(20, 4))
    transfer_income = Column(DECIMAL(20, 4))
    expense = Column(DECIMAL(20, 4))
    food_alcohol_expense = Column(DECIMAL(20, 4))
    clothes_expense = Column(DECIMAL(20, 4))
    resident_expense = Column(DECIMAL(20, 4))
    living_goods_expense = Column(DECIMAL(20, 4))
    traffic_expense = Column(DECIMAL(20, 4))
    education_recreation_expense = Column(DECIMAL(20, 4))
    healthcare_expense = Column(DECIMAL(20, 4))
    other_expense = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)