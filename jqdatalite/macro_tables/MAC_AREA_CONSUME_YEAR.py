# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_CONSUME_YEAR(Base):
    """
    各地区居民消费水平表(年度)
    """
    __tablename__ = "MAC_AREA_CONSUME_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    income = Column(DECIMAL(20, 4))
    income_yoy = Column(DECIMAL(10, 4))
    urban_income = Column(DECIMAL(20, 4))
    urban_income_yoy = Column(DECIMAL(10, 4))
    rural_income = Column(DECIMAL(20, 4))
    rural_income_yoy = Column(DECIMAL(10, 4))
    expense = Column(DECIMAL(20, 4))
    expense_yoy = Column(DECIMAL(10, 4))
    urban_expense = Column(DECIMAL(20, 4))
    urban_expense_yoy = Column(DECIMAL(10, 4))
    rural_expense = Column(DECIMAL(20, 4))
    rural_expense_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)