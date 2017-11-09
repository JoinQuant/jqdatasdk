# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_URBAN_RURAL_EXPENSE_YEAR(Base):
    """
    分地区城镇及农村居民家庭平均每人全年消费性支出表(年度)
    """
    __tablename__ = "MAC_AREA_URBAN_RURAL_EXPENSE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    expense = Column(DECIMAL(20, 4))
    food_expense = Column(DECIMAL(20, 4))
    clothes_expense = Column(DECIMAL(20, 4))
    resident_expense = Column(DECIMAL(20, 4))
    household_equipment_expense = Column(DECIMAL(20, 4))
    healthcare_expense = Column(DECIMAL(20, 4))
    traffic_expense = Column(DECIMAL(20, 4))
    education_recreation_expense = Column(DECIMAL(20, 4))
    other_expense = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)