# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SOCIAL_SCALE_FINANCE(Base):
    """
    社会融资规模及构成
    """

    __tablename__ = "MAC_SOCIAL_SCALE_FINANCE"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    social_finance_scale = Column(DECIMAL(20, 4))
    rmb_loan = Column(DECIMAL(20, 4))
    foreign_loan = Column(DECIMAL(20, 4))
    entrust_loan = Column(DECIMAL(20, 4))
    trust_loan = Column(DECIMAL(20, 4))
    out_fulfilled_scale = Column(DECIMAL(20, 4))
    corporate_bond_scale = Column(DECIMAL(20, 4))
    non_finance_scale = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)