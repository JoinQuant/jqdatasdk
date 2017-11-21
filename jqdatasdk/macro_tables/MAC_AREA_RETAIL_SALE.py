# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_RETAIL_SALE(Base):
    """
    分地区消费品零售总额
    """

    __tablename__ = "MAC_AREA_RETAIL_SALE"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    retail = Column(DECIMAL(20, 4))
    retail_yoy = Column(DECIMAL(10, 4))
    city_retail = Column(DECIMAL(20, 4))
    city_county_retail = Column(DECIMAL(20, 4))
    city_county_below_retail = Column(DECIMAL(20, 4))
    city_whole_sale_retail = Column(DECIMAL(20, 4))
    hotels_retail = Column(DECIMAL(20, 4))
    manufacturing_retail = Column(DECIMAL(20, 4))
    agricultural_retail = Column(DECIMAL(20, 4))
    others_retail = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)