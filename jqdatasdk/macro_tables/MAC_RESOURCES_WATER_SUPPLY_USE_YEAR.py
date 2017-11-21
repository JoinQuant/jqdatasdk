# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESOURCES_WATER_SUPPLY_USE_YEAR(Base):
    """
    供水用水情况表
    """
    __tablename__ = "MAC_RESOURCES_WATER_SUPPLY_USE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    water_supply = Column(DECIMAL(20, 4))
    surface_water = Column(DECIMAL(20, 4))
    ground_water = Column(DECIMAL(20, 4))
    others = Column(DECIMAL(20, 4))
    water_use = Column(DECIMAL(20, 4))
    agriculture = Column(DECIMAL(20, 4))
    industry = Column(DECIMAL(20, 4))
    daily_consumption = Column(DECIMAL(20, 4))
    ecology = Column(DECIMAL(20, 4))
    per_amount = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)