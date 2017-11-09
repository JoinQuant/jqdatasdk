# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_GDP_QUARTER(Base):
    """
    分地区国内生产总值表（季度）
    """
    __tablename__ = "MAC_AREA_GDP_QUARTER"

    id = Column(Integer, primary_key=True)
    stat_quarter = Column(String(14), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    gdp_acc = Column(DECIMAL(20, 4))
    gdp_primary_acc = Column(DECIMAL(20, 4))
    gdp_secondary_acc = Column(DECIMAL(20, 4))
    gdp_tertiary_acc = Column(DECIMAL(20, 4))
    gdp_sin = Column(DECIMAL(20, 4))
    gdp_primary_sin = Column(DECIMAL(20, 4))
    gdp_secondary_sin = Column(DECIMAL(20, 4))
    gdp_tertiary_sin = Column(DECIMAL(20, 4))
    gdp_yoy_acc = Column(DECIMAL(10, 4))
    gdp_primary_yoy_acc = Column(DECIMAL(10, 4))
    gdp_secondary_yoy_acc = Column(DECIMAL(10, 4))
    gdp_tertiary_yoy_acc = Column(DECIMAL(10, 4))
    gdp_yoy_sin = Column(DECIMAL(10, 4))
    gdp_primary_yoy_sin = Column(DECIMAL(10, 4))
    gdp_secondary_yoy_sin = Column(DECIMAL(10, 4))
    gdp_tertiary_yoy_sin = Column(DECIMAL(10, 4))
    gdp_mom = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)