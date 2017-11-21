# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_URBAN_INCOME_YEAR(Base):
    """
    分地区城镇居民家庭平均每人全年收入来源表(年度)
    """
    __tablename__ = "MAC_AREA_URBAN_INCOME_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    disposable_income = Column(DECIMAL(20, 4))
    income = Column(DECIMAL(20, 4))
    wage_income = Column(DECIMAL(20, 4))
    business_income = Column(DECIMAL(20, 4))
    property_income = Column(DECIMAL(20, 4))
    transfer_income = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)