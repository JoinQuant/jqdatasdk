# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_OTHER_DEPOSIT(Base):
    """
    其他存款性公司资产负债表
    """
    __tablename__ = "MAC_OTHER_DEPOSIT"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    total_assets = Column(DECIMAL(20, 4))
    foreign_assets = Column(DECIMAL(20, 4))
    reserve_assets = Column(DECIMAL(20, 4))
    reserve_deposit = Column(DECIMAL(20, 4))
    cash_in_vault = Column(DECIMAL(20, 4))
    government_claim = Column(DECIMAL(20, 4))
    central_bank_claim = Column(DECIMAL(20, 4))
    other_claim = Column(DECIMAL(20, 4))
    other_finance_claim = Column(DECIMAL(20, 4))
    non_finance_claim = Column(DECIMAL(20, 4))
    other_resident_claim = Column(DECIMAL(20, 4))
    other_assets = Column(DECIMAL(20, 4))
    total_liability = Column(DECIMAL(20, 4))
    non_finance_liability = Column(DECIMAL(20, 4))
    non_finance_include_broad_money = Column(DECIMAL(20, 4))
    corporate_demand_deposit = Column(DECIMAL(20, 4))
    corporate_time_deposit = Column(DECIMAL(20, 4))
    personal_deposit = Column(DECIMAL(20, 4))
    exclude_broad_money = Column(DECIMAL(20, 4))
    transfer_deposit = Column(DECIMAL(20, 4))
    other_deposit = Column(DECIMAL(20, 4))
    other_non_finance_liability = Column(DECIMAL(20, 4))
    central_bank_liability = Column(DECIMAL(20, 4))
    other_deposit_liability = Column(DECIMAL(20, 4))
    other_finance_liability = Column(DECIMAL(20, 4))
    include_broad_money = Column(DECIMAL(20, 4))
    foreign_liability = Column(DECIMAL(20, 4))
    bond_issue = Column(DECIMAL(20, 4))
    paid_in_capital = Column(DECIMAL(20, 4))
    other_liability = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)