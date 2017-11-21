# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_RURAL_HOUSE_YEAR(Base):
    """
    分地区农村居民家庭住房情况表(年度)
    """
    __tablename__ = "MAC_AREA_RURAL_HOUSE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    house_area = Column(DECIMAL(20, 4))
    house_value = Column(DECIMAL(20, 4))
    concrete_structure = Column(DECIMAL(20, 4))
    brick_wood_structure = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)