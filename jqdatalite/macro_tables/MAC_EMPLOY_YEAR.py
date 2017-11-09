# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_EMPLOY_YEAR(Base):
    """
    就业情况基本表(年度)
    """

    __tablename__ = "MAC_EMPLOY_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    population = Column(DECIMAL(20, 4))
    employ = Column(DECIMAL(20, 4))
    employ_primary = Column(DECIMAL(20, 4))
    employ_secondary = Column(DECIMAL(20, 4))
    employ_tertiary = Column(DECIMAL(20, 4))
    employ_urban = Column(DECIMAL(20, 4))
    employ_urban_state_owned = Column(DECIMAL(20, 4))
    employ_urban_collective = Column(DECIMAL(20, 4))
    employ_urban_stock_cooperate = Column(DECIMAL(20, 4))
    employ_urban_joint_ownership = Column(DECIMAL(20, 4))
    employ_urban_limited = Column(DECIMAL(20, 4))
    employ_urban_stock = Column(DECIMAL(20, 4))
    employ_urban_private = Column(DECIMAL(20, 4))
    employ_urban_hkmt = Column(DECIMAL(20, 4))
    employ_urban_foreign = Column(DECIMAL(20, 4))
    employ_urban_individual = Column(DECIMAL(20, 4))
    employ_rural = Column(DECIMAL(20, 4))
    employ_rural_private = Column(DECIMAL(20, 4))
    employ_rural_individual = Column(DECIMAL(20, 4))
    unemploy_num = Column(DECIMAL(20, 4))
    unemploy_rate = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)