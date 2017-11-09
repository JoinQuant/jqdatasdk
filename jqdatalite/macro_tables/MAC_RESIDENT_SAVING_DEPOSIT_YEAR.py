# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESIDENT_SAVING_DEPOSIT_YEAR(Base):
    """
    城乡居民人民币储蓄存款表(年度)
    """
    __tablename__ = "MAC_RESIDENT_SAVING_DEPOSIT_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    deposit = Column(DECIMAL(20, 4))
    time_deposit = Column(DECIMAL(20, 4))
    demand_deposit = Column(DECIMAL(20, 4))
    deposit_increase = Column(DECIMAL(20, 4))
    time_deposit_increase = Column(DECIMAL(20, 4))
    demand_deposit_increase = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)