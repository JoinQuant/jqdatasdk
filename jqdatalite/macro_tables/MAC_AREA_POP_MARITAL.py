# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_POP_MARITAL(Base):
    """
    各地区按性别和婚姻状况分的人口表
    """
    __tablename__ = "MAC_AREA_POP_MARITAL"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    age_over_15 = Column(DECIMAL(20, 4))
    male_age_over_15 = Column(DECIMAL(20, 4))
    female_age_over_15 = Column(DECIMAL(20, 4))
    never_married = Column(DECIMAL(20, 4))
    male_never_married = Column(DECIMAL(20, 4))
    female_never_married = Column(DECIMAL(20, 4))
    first_married = Column(DECIMAL(20, 4))
    male_first_married = Column(DECIMAL(20, 4))
    female_first_married = Column(DECIMAL(20, 4))
    remarried = Column(DECIMAL(20, 4))
    male_remarried = Column(DECIMAL(20, 4))
    female_remarried = Column(DECIMAL(20, 4))
    divorced = Column(DECIMAL(20, 4))
    male_divorced = Column(DECIMAL(20, 4))
    female_divorced = Column(DECIMAL(20, 4))
    widowed = Column(DECIMAL(20, 4))
    male_widowed = Column(DECIMAL(20, 4))
    female_widowed = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)