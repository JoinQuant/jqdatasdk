# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSURANCE_REVENUE_EXPENSE_YEAR(Base):
    """
    保险公司原保费收入和赔付支出情况
    """
    __tablename__ = "MAC_INSURANCE_REVENUE_EXPENSE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    original_revenue = Column(DECIMAL(20, 4))
    property_revenue = Column(DECIMAL(20, 4))
    life_revenue = Column(DECIMAL(20, 4))
    original_expense = Column(DECIMAL(20, 4))
    property_expense = Column(DECIMAL(20, 4))
    life_expense = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)