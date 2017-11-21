# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCAL_EXTERNAL_DEBT_YEAR(Base):
    """
    外债余额表（年度）
    """
    __tablename__ = "MAC_FISCAL_EXTERNAL_DEBT_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    debt = Column(DECIMAL(20, 4))
    government_loan = Column(DECIMAL(20, 4))
    financial_organization_loan = Column(DECIMAL(20, 4))
    commerce_loan = Column(DECIMAL(20, 4))
    trade_credit = Column(DECIMAL(20, 4))
    long_term_debt = Column(DECIMAL(20, 4))
    short_term_debt = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)