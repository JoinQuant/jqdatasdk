# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCAL_EXTRAL_BALANCE_YEAR(Base):
    """
    中央财政与地方财政预算外收支表（年度）
    """
    __tablename__ = "MAC_FISCAL_EXTRAL_BALANCE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    revenue = Column(DECIMAL(20, 4))
    central_revenue = Column(DECIMAL(20, 4))
    local_revenue = Column(DECIMAL(20, 4))
    expense = Column(DECIMAL(20, 4))
    central_expense = Column(DECIMAL(20, 4))
    local_expense = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)