# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_POPULATION_DEPENDENCY(Base):
    """
    人口年龄结构和抚养比例表
    """
    __tablename__ = "MAC_POPULATION_DEPENDENCY"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    population = Column(DECIMAL(20, 4))
    age_between_0_and_14 = Column(DECIMAL(20, 4))
    age_between_15_and_64 = Column(DECIMAL(20, 4))
    age_over_65 = Column(DECIMAL(20, 4))
    dependency_ratio = Column(DECIMAL(10, 4))
    children_dependency_ratio = Column(DECIMAL(10, 4))
    old_dependency_ratio = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)