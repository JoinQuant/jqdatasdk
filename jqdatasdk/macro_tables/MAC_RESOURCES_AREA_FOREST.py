# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESOURCES_AREA_FOREST(Base):
    """
    各地区森林资源情况表
    """
    __tablename__ = "MAC_RESOURCES_AREA_FOREST"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    forestry_land_area = Column(DECIMAL(20, 4))
    forest_area = Column(DECIMAL(20, 4))
    man_made_forest_area = Column(DECIMAL(20, 4))
    forest_cover_rate = Column(DECIMAL(10, 4))
    standing_forest_stock_volume = Column(DECIMAL(20, 4))
    forest_stand_volume = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)