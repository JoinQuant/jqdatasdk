# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_POPULATION_YEAR(Base):
    """
    人口基本情况表(年度)
    """
    __tablename__ = "MAC_POPULATION_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    population = Column(DECIMAL(20, 4))
    male = Column(DECIMAL(20, 4))
    female = Column(DECIMAL(20, 4))
    urban = Column(DECIMAL(20, 4))
    rural = Column(DECIMAL(20, 4))
    birth_rate = Column(DECIMAL(10, 4))
    death_rate = Column(DECIMAL(10, 4))
    growth_rate = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)