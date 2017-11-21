# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_ENGEL_COEFFICIENT_YEAR(Base):
    """
    城乡居民家庭人均收入及恩格尔系数(年度)
    """
    __tablename__ = "MAC_ENGEL_COEFFICIENT_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    urban_income = Column(DECIMAL(20, 4))
    urban_income_index = Column(DECIMAL(10, 4))
    rural_income = Column(DECIMAL(20, 4))
    rural_income_index = Column(DECIMAL(10, 4))
    urban_engel_coefficient = Column(DECIMAL(10, 4))
    rural_engel_coefficient = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)