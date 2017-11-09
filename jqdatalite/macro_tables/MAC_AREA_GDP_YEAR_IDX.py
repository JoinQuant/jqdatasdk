# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_GDP_YEAR_IDX(Base):
    """
    分地区国内生产总值指数表(上年=100)
    """

    __tablename__ = "MAC_AREA_GDP_YEAR_IDX"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    gni_idx = Column(DECIMAL(10, 4))
    gdp_idx = Column(DECIMAL(10, 4))
    gdp_primary_idx = Column(DECIMAL(10, 4))
    gdp_agro_idx = Column(DECIMAL(10, 4))
    gdp_secondary_idx = Column(DECIMAL(10, 4))
    gdp_industry_idx = Column(DECIMAL(10, 4))
    gdp_construction_idx = Column(DECIMAL(10, 4))
    gdp_tertiary_idx = Column(DECIMAL(10, 4))
    gdp_sale_idx = Column(DECIMAL(10, 4))
    gdp_transport_idx = Column(DECIMAL(10, 4))
    gdp_hotel_idx = Column(DECIMAL(10, 4))
    gdp_financial_idx = Column(DECIMAL(10, 4))
    gdp_estate_idx = Column(DECIMAL(10, 4))
    gdp_others_idx = Column(DECIMAL(10, 4))
    gdp_per_capita_idx = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)