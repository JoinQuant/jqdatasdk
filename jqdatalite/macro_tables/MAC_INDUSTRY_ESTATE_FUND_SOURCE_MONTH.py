# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_ESTATE_FUND_SOURCE_MONTH(Base):
    """
    房地产开发投资资金来源情况表(月度累计)
    """
    __tablename__ = "MAC_INDUSTRY_ESTATE_FUND_SOURCE_MONTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    total_invest = Column(DECIMAL(20, 4))
    total_invest_yoy = Column(DECIMAL(10, 4))
    surplus = Column(DECIMAL(20, 4))
    surplus_yoy = Column(DECIMAL(10, 4))
    invest = Column(DECIMAL(20, 4))
    invest_yoy = Column(DECIMAL(10, 4))
    domestic_loan = Column(DECIMAL(20, 4))
    domestic_loan_yoy = Column(DECIMAL(10, 4))
    foreign_capital = Column(DECIMAL(20, 4))
    forfeign_capital_yoy = Column(DECIMAL(10, 4))
    self_financing = Column(DECIMAL(20, 4))
    self_financing_yoy = Column(DECIMAL(10, 4))
    other_capital = Column(DECIMAL(20, 4))
    other_capital_yoy = Column(DECIMAL(10, 4))
    payment = Column(DECIMAL(20, 4))
    payment_yoy = Column(DECIMAL(10, 4))
    project_funds = Column(DECIMAL(20, 4))
    project_funds_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)