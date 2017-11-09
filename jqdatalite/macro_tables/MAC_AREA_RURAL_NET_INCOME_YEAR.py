# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_RURAL_NET_INCOME_YEAR(Base):
    """
    各地区按来源分农村居民家庭人均纯收入(年度)
    """
    __tablename__ = "MAC_AREA_RURAL_NET_INCOME_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    income = Column(DECIMAL(20, 4))
    wage_income = Column(DECIMAL(20, 4))
    business_income = Column(DECIMAL(20, 4))
    property_income = Column(DECIMAL(20, 4))
    transfer_income = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)