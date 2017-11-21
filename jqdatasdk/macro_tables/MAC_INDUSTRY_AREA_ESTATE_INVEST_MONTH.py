# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_AREA_ESTATE_INVEST_MONTH(Base):
    """
    分地区房地产开发投资情况表(月度累计)
    """
    __tablename__ = "MAC_INDUSTRY_AREA_ESTATE_INVEST_MONTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    invest = Column(DECIMAL(20, 4))
    invest_yoy = Column(DECIMAL(10, 4))
    resident = Column(DECIMAL(20, 4))
    resident_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)