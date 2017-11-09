# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSURANCE_ASSETS_YEAR(Base):
    """
    保险公司资产情况
    """
    __tablename__ = "MAC_INSURANCE_ASSETS_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    total = Column(DECIMAL(20, 4))
    assets = Column(DECIMAL(20, 4))
    life = Column(DECIMAL(20, 4))
    reinsurance = Column(DECIMAL(20, 4))
    china_invested = Column(DECIMAL(20, 4))
    foreign_invested = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)