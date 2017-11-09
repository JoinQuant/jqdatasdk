# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_GDP_YEAR(Base):
    """
    分地区国内生产总值表（年度）
    """
    __tablename__ = "MAC_AREA_GDP_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    gni = Column(DECIMAL(20, 4))
    gdp = Column(DECIMAL(20, 4))
    gdp_primary = Column(DECIMAL(20, 4))
    gdp_agro = Column(DECIMAL(20, 4))
    gdp_secondary = Column(DECIMAL(20, 4))
    gdp_industry = Column(DECIMAL(20, 4))
    gdp_construction = Column(DECIMAL(20, 4))
    gdp_tertiary = Column(DECIMAL(20, 4))
    gdp_transport = Column(DECIMAL(20, 4))
    gdp_sale = Column(DECIMAL(20, 4))
    gdp_hotel = Column(DECIMAL(20, 4))
    gdp_financial = Column(DECIMAL(20, 4))
    gdp_estate = Column(DECIMAL(20, 4))
    gdp_others = Column(DECIMAL(20, 4))
    primary_percent = Column(DECIMAL(10, 4))
    secondary_percent = Column(DECIMAL(10, 4))
    tertiary_percent = Column(DECIMAL(10, 4))
    gpd_per_capita = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)