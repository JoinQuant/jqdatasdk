# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FIXED_INVESTMENT_YEAR(Base):
    """
    固定资产投资情况表(年度)
    """
    __tablename__ = "MAC_FIXED_INVESTMENT_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    fixed_investment = Column(DECIMAL(20, 4))
    urban_fixed_investment = Column(DECIMAL(20, 4))
    mainland = Column(DECIMAL(20, 4))
    state_owned = Column(DECIMAL(20, 4))
    collective = Column(DECIMAL(20, 4))
    joint_stock = Column(DECIMAL(20, 4))
    joint_owned = Column(DECIMAL(20, 4))
    limited = Column(DECIMAL(20, 4))
    stock = Column(DECIMAL(20, 4))
    private = Column(DECIMAL(20, 4))
    individual = Column(DECIMAL(20, 4))
    others = Column(DECIMAL(20, 4))
    hkmt = Column(DECIMAL(20, 4))
    foreign = Column(DECIMAL(20, 4))
    state_budget = Column(DECIMAL(20, 4))
    domestic_loan = Column(DECIMAL(20, 4))
    foreign_investment = Column(DECIMAL(20, 4))
    self_raised_fund = Column(DECIMAL(20, 4))
    other_fund = Column(DECIMAL(20, 4))
    construct_install = Column(DECIMAL(20, 4))
    equipment_purchase = Column(DECIMAL(20, 4))
    other_expense = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)