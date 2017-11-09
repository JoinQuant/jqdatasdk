# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MONEY_SUPPLY_YEAR(Base):
    """
    货币供应量(年度)
    """

    __tablename__ = "MAC_MONEY_SUPPLY_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    m2 = Column(DECIMAL(20, 4))
    m1 = Column(DECIMAL(20, 4))
    m0 = Column(DECIMAL(20, 4))
    demond_deposit = Column(DECIMAL(20, 4))
    quosi = Column(DECIMAL(20, 4))
    time_deposit = Column(DECIMAL(20, 4))
    saving_deposit = Column(DECIMAL(20, 4))
    other_deposit = Column(DECIMAL(20, 4))
    m2_yoy = Column(DECIMAL(10, 4))
    m1_yoy = Column(DECIMAL(10, 4))
    m0_yoy = Column(DECIMAL(10, 4))
    demond_deposit_yoy = Column(DECIMAL(10, 4))
    quosi_yoy = Column(DECIMAL(10, 4))
    time_deposit_yoy = Column(DECIMAL(10, 4))
    saving_deposit_yoy = Column(DECIMAL(10, 4))
    other_deposit_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)