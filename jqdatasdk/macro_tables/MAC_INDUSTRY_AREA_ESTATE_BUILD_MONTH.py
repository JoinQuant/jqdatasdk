# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_AREA_ESTATE_BUILD_MONTH(Base):
    """
    各地区房地产开发规模与开、竣工面积增长情况表(月度累计)
    """
    __tablename__ = "MAC_INDUSTRY_AREA_ESTATE_BUILD_MONTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    construct_area = Column(DECIMAL(20, 4))
    construct_area_yoy = Column(DECIMAL(10, 4))
    new_start_area = Column(DECIMAL(20, 4))
    new_start_area_yoy = Column(DECIMAL(10, 4))
    complete_area = Column(DECIMAL(20, 4))
    complete_area_yoy = Column(DECIMAL(10, 4))
    resident_construct_area = Column(DECIMAL(20, 4))
    resident_construct_area_yoy = Column(DECIMAL(10, 4))
    resident_new_start_area = Column(DECIMAL(20, 4))
    resident_new_start_area_yoy = Column(DECIMAL(10, 4))
    resident_complete_area = Column(DECIMAL(20, 4))
    resident_complete_area_yoy = Column(DECIMAL(10, 4))
    office_construct_area = Column(DECIMAL(20, 4))
    office_construct_area_yoy = Column(DECIMAL(10, 4))
    office_new_start_area = Column(DECIMAL(20, 4))
    office_new_start_area_yoy = Column(DECIMAL(10, 4))
    office_complete_area = Column(DECIMAL(20, 4))
    office_complete_area_yoy = Column(DECIMAL(10, 4))
    business_construct_area = Column(DECIMAL(20, 4))
    business_construct_area_yoy = Column(DECIMAL(10, 4))
    business_new_start_area = Column(DECIMAL(20, 4))
    business_new_start_area_yoy = Column(DECIMAL(10, 4))
    business_complete_area = Column(DECIMAL(20, 4))
    business_complete_area_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)