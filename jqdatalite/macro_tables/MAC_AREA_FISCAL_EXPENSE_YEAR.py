# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FISCAL_EXPENSE_YEAR(Base):
    """
    各地区财政支出表（年度）
    """
    __tablename__ = "MAC_AREA_FISCAL_EXPENSE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    general_budget = Column(DECIMAL(20, 4))
    public_sevice = Column(DECIMAL(20, 4))
    diplomacy = Column(DECIMAL(20, 4))
    defence = Column(DECIMAL(20, 4))
    public_security = Column(DECIMAL(20, 4))
    education = Column(DECIMAL(20, 4))
    science_technology = Column(DECIMAL(20, 4))
    cultural_sports_media = Column(DECIMAL(20, 4))
    social_security_employment = Column(DECIMAL(20, 4))
    public_health = Column(DECIMAL(20, 4))
    environmental_protection = Column(DECIMAL(20, 4))
    community_affairs = Column(DECIMAL(20, 4))
    agriculture_forestry = Column(DECIMAL(20, 4))
    transportation = Column(DECIMAL(20, 4))
    resource_exploration_power = Column(DECIMAL(20, 4))
    business_service = Column(DECIMAL(20, 4))
    financial_supervision = Column(DECIMAL(20, 4))
    earthquake_reconstruction = Column(DECIMAL(20, 4))
    land_resource_meteorology = Column(DECIMAL(20, 4))
    housing_security = Column(DECIMAL(20, 4))
    material_reserve_management = Column(DECIMAL(20, 4))
    debt_interest = Column(DECIMAL(20, 4))
    other = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)