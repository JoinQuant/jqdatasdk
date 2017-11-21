# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESOURCES_AREA_WATER_RESOURCES(Base):
    """
    水资源情况表
    """
    __tablename__ = "MAC_RESOURCES_AREA_WATER_RESOURCES"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    total_amount = Column(DECIMAL(20, 4))
    surface = Column(DECIMAL(20, 4))
    ground = Column(DECIMAL(20, 4))
    duplicated_measurement = Column(DECIMAL(10, 4))
    per_amount = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)