# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCAL_CENTRAL_EXPENSE_YEAR(Base):
    """
    中央和地方财政主要支出项目情况表（年度）
    """
    __tablename__ = "MAC_FISCAL_CENTRAL_EXPENSE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    item_id = Column(String(10), nullable=False)
    item_name = Column(String(128), nullable=False)
    expense = Column(DECIMAL(20, 4))
    central_expense = Column(DECIMAL(20, 4))
    local_expense = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)