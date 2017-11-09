# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESOURCES_ENVIRONMENT_TREAT_INVEST(Base):
    """
    环境污染治理投资情况信息表
    """
    __tablename__ = "MAC_RESOURCES_ENVIRONMENT_TREAT_INVEST"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    environment_pollution = Column(DECIMAL(20, 4))
    infrastructure = Column(DECIMAL(20, 4))
    fuel_gas = Column(DECIMAL(20, 4))
    centralized_heating = Column(DECIMAL(20, 4))
    drainage = Column(DECIMAL(20, 4))
    gardening = Column(DECIMAL(20, 4))
    sanitation = Column(DECIMAL(20, 4))
    industrial_pollution = Column(DECIMAL(20, 4))
    three_simultaneities = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)