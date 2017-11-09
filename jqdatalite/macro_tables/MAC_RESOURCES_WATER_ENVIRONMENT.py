# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESOURCES_WATER_ENVIRONMENT(Base):
    """
    水环境情况信息表
    """
    __tablename__ = "MAC_RESOURCES_WATER_ENVIRONMENT"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    waste_water_discharge = Column(DECIMAL(20, 4))
    COD_discharge = Column(DECIMAL(20, 4))
    NH3_N2_discharge = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)