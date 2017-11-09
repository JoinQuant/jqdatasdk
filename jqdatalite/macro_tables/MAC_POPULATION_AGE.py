# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_POPULATION_AGE(Base):
    """
    按年龄和性别分人口数表
    """
    __tablename__ = "MAC_POPULATION_AGE"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    age = Column(String(30), nullable=False)
    rate = Column(DECIMAL(10, 8))
    population = Column(Integer)
    male = Column(Integer)
    female = Column(Integer)
    gender_ratio = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)