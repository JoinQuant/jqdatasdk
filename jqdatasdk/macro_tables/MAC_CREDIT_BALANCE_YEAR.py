# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_CREDIT_BALANCE_YEAR(Base):
    """
    金融机构信贷资金平衡表(年度)
    """

    __tablename__ = "MAC_CREDIT_BALANCE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    total_source = Column(DECIMAL(20, 4))
    total_deposit = Column(DECIMAL(20, 4))
    corporate_deposit = Column(DECIMAL(20, 4))
    personal_deposit = Column(DECIMAL(20, 4))
    fiscal_deposit = Column(DECIMAL(20, 4))
    temporary_deposit = Column(DECIMAL(20, 4))
    designated_deposit = Column(DECIMAL(20, 4))
    finance_bond = Column(DECIMAL(20, 4))
    m0 = Column(DECIMAL(20, 4))
    finance_liability = Column(DECIMAL(20, 4))
    total_use = Column(DECIMAL(20, 4))
    total_loan = Column(DECIMAL(20, 4))
    domestic_loan = Column(DECIMAL(20, 4))
    short_term_loan = Column(DECIMAL(20, 4))
    medium_long_term_loan = Column(DECIMAL(20, 4))
    finance_lease = Column(DECIMAL(20, 4))
    finance_bill = Column(DECIMAL(20, 4))
    advance = Column(DECIMAL(20, 4))
    oversea_loan = Column(DECIMAL(20, 4))
    security = Column(DECIMAL(20, 4))
    othershare = Column(DECIMAL(20, 4))
    bullion_purchase = Column(DECIMAL(20, 4))
    forex_purchase = Column(DECIMAL(20, 4))
    finance_assets = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)