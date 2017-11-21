# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_CURRENCY_STATE_YEAR(Base):
    """
    货币当局资产负债表(年度)
    """

    __tablename__ = "MAC_CURRENCY_STATE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    total_assets = Column(DECIMAL(20, 4))
    foreign_assets = Column(DECIMAL(20, 4))
    foreign_exchange = Column(DECIMAL(20, 4))
    money_gold = Column(DECIMAL(20, 4))
    other_foreign_assets = Column(DECIMAL(20, 4))
    government_claim = Column(DECIMAL(20, 4))
    bank_claim = Column(DECIMAL(20, 4))
    other_finance_claim = Column(DECIMAL(20, 4))
    non_finance_claim = Column(DECIMAL(20, 4))
    other_assets = Column(DECIMAL(20, 4))
    total_liability = Column(DECIMAL(20, 4))
    reserve_money = Column(DECIMAL(20, 4))
    currency_issue = Column(DECIMAL(20, 4))
    finance_deposit = Column(DECIMAL(20, 4))
    bank_deposit = Column(DECIMAL(20, 4))
    other_finance_deposit = Column(DECIMAL(20, 4))
    non_reserve_finance_deposit = Column(DECIMAL(20, 4))
    bond_issue = Column(DECIMAL(20, 4))
    foreign_liability = Column(DECIMAL(20, 4))
    government_deposit = Column(DECIMAL(20, 4))
    owned_capital = Column(DECIMAL(20, 4))
    other_liability = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)