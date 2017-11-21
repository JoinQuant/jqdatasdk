# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCAL_TOTAL_YEAR(Base):
    """
    国家财政收支总额及增长速度表（年度）
    """
    __tablename__ = "MAC_FISCAL_TOTAL_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    revenue = Column(DECIMAL(20, 4))
    expense = Column(DECIMAL(20, 4))
    revenue_yoy = Column(DECIMAL(10, 4))
    expense_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)