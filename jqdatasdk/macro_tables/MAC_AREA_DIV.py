# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_DIV(Base):
    """
    定义了中国和世界不同地区的划分
    """
    __tablename__ = "MAC_AREA_DIV"

    id = Column(Integer, primary_key=True)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    province_name = Column(String(100), nullable=False)
    city_name = Column(String(100), nullable=False)
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)