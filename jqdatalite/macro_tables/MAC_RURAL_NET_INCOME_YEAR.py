# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RURAL_NET_INCOME_YEAR(Base):
    """
    农村居民家庭平均每人纯收入(年度)
    """
    __tablename__ = "MAC_RURAL_NET_INCOME_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    income = Column(DECIMAL(20, 4))
    wage_income = Column(DECIMAL(20, 4))
    business_income = Column(DECIMAL(20, 4))
    property_income = Column(DECIMAL(20, 4))
    transfer_income = Column(DECIMAL(20, 4))
    farming_income = Column(DECIMAL(20, 4))
    forestry_income = Column(DECIMAL(20, 4))
    animal_husbandry_income = Column(DECIMAL(20, 4))
    fishery_income = Column(DECIMAL(20, 4))
    industry_income = Column(DECIMAL(20, 4))
    construction_income = Column(DECIMAL(20, 4))
    traffic_income = Column(DECIMAL(20, 4))
    wholesale_income = Column(DECIMAL(20, 4))
    service_income = Column(DECIMAL(20, 4))
    education_culture_income = Column(DECIMAL(20, 4))
    other_income = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)