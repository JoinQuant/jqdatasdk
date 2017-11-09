# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_STK_MARKET(Base):
    """
    证券市场基本情况(年度)
    """

    __tablename__ = "MAC_STK_MARKET"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    public_company = Column(DECIMAL(20, 4))
    public_b_company = Column(DECIMAL(20, 4))
    public_h_company = Column(DECIMAL(20, 4))
    total_share = Column(DECIMAL(20, 4))
    flow_share = Column(DECIMAL(20, 4))
    total_value = Column(DECIMAL(20, 4))
    flow_value = Column(DECIMAL(20, 4))
    total_trade_volume = Column(DECIMAL(20, 4))
    total_trade_amount = Column(DECIMAL(20, 4))
    xshg_close = Column(DECIMAL(20, 4))
    xshe_close = Column(DECIMAL(20, 4))
    account_num = Column(DECIMAL(20, 4))
    xshg_avg_pe = Column(DECIMAL(10, 4))
    xshe_avg_pe = Column(DECIMAL(10, 4))
    xshg_avg_turnover = Column(DECIMAL(10, 4))
    xshe_avg_turnover = Column(DECIMAL(10, 4))
    treasury_bond_issue = Column(DECIMAL(20, 4))
    company_bond_issue = Column(DECIMAL(20, 4))
    bond_amount = Column(DECIMAL(20, 4))
    treasury_bond_spot_amount = Column(DECIMAL(20, 4))
    treasury_bond_repurchase_amount = Column(DECIMAL(20, 4))
    security_fund_num = Column(DECIMAL(20, 4))
    security_fund_cap = Column(DECIMAL(20, 4))
    security_fund_amount = Column(DECIMAL(20, 4))
    future_volume = Column(DECIMAL(20, 4))
    future_amount = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)