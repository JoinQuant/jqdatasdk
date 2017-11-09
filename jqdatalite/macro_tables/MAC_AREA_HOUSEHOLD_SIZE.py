# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_HOUSEHOLD_SIZE(Base):
    """
    各地区户数、人口数、性别比和户规模表
    """
    __tablename__ = "MAC_AREA_HOUSEHOLD_SIZE"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    household = Column(DECIMAL(20, 4))
    family_household = Column(DECIMAL(20, 4))
    collective_household = Column(DECIMAL(20, 4))
    family_household_population = Column(DECIMAL(20, 4))
    male_family = Column(DECIMAL(20, 4))
    female_family = Column(DECIMAL(20, 4))
    collective_household_population = Column(DECIMAL(20, 4))
    male_collective = Column(DECIMAL(20, 4))
    female_collective = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)