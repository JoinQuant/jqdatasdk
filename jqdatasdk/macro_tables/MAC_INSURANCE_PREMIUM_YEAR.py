# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSURANCE_PREMIUM_YEAR(Base):
    """
    保险公司保费金额表（年）
    """
    __tablename__ = "MAC_INSURANCE_PREMIUM_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    total_income = Column(DECIMAL(20, 4))
    property_income = Column(DECIMAL(20, 4))
    enterprise = Column(DECIMAL(20, 4))
    family = Column(DECIMAL(20, 4))
    vehicle = Column(DECIMAL(20, 4))
    project = Column(DECIMAL(20, 4))
    liability = Column(DECIMAL(20, 4))
    credit = Column(DECIMAL(20, 4))
    guarantee = Column(DECIMAL(20, 4))
    ship = Column(DECIMAL(20, 4))
    freight = Column(DECIMAL(20, 4))
    special_risk = Column(DECIMAL(20, 4))
    farm = Column(DECIMAL(20, 4))
    property_health = Column(DECIMAL(20, 4))
    property_accident = Column(DECIMAL(20, 4))
    other = Column(DECIMAL(20, 4))
    personal_income = Column(DECIMAL(20, 4))
    life = Column(DECIMAL(20, 4))
    health = Column(DECIMAL(20, 4))
    accident = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)