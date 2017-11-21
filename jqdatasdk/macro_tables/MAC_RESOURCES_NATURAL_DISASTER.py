# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESOURCES_NATURAL_DISASTER(Base):
    """
    自然灾害情况信息表
    """
    __tablename__ = "MAC_RESOURCES_NATURAL_DISASTER"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    geological_disaster_num = Column(DECIMAL(20, 4))
    earthquake_num = Column(DECIMAL(20, 4))
    forest_fire_num = Column(DECIMAL(20, 4))
    forest_fire_area = Column(DECIMAL(20, 4))
    forest_pest_affected_area = Column(DECIMAL(20, 4))
    forest_pest_protected_area = Column(DECIMAL(20, 4))
    forest_pest_protected_rate = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)