# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSURANCE_AREA_YEAR(Base):
    """
    全国各地区保险业务统计表(年）
    """
    __tablename__ = "MAC_INSURANCE_AREA_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    income = Column(DECIMAL(20, 4))
    property_income = Column(DECIMAL(20, 4))
    personal_income = Column(DECIMAL(20, 4))
    expense = Column(DECIMAL(20, 4))
    property_expense = Column(DECIMAL(20, 4))
    personal_expense = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)