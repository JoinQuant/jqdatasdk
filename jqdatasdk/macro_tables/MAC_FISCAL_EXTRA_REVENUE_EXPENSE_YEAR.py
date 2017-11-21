# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCAL_EXTRA_REVENUE_EXPENSE_YEAR(Base):
    """
    预算外资金分项目收支表
    """
    __tablename__ = "MAC_FISCAL_EXTRA_REVENUE_EXPENSE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    revenue = Column(DECIMAL(20, 4))
    revenue_administration = Column(DECIMAL(20, 4))
    revenue_fund = Column(DECIMAL(20, 4))
    revenue_pool_fund = Column(DECIMAL(20, 4))
    revenue_local_finance = Column(DECIMAL(20, 4))
    revenue_state_enterprise = Column(DECIMAL(20, 4))
    revenue_other = Column(DECIMAL(20, 4))
    expense = Column(DECIMAL(20, 4))
    expense_pubic_service = Column(DECIMAL(20, 4))
    expense_education = Column(DECIMAL(20, 4))
    expense_security_employment = Column(DECIMAL(20, 4))
    expense_transportation = Column(DECIMAL(20, 4))
    expense_community_affairs = Column(DECIMAL(20, 4))
    expense_other = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)