# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_ESTATE_70CITY_INDEX_MONTH(Base):
    """
    70个大中城市房屋销售价格指数(月度)
    """
    __tablename__ = "MAC_INDUSTRY_ESTATE_70CITY_INDEX_MONTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    fixed_base_type = Column(String(100), nullable=False)
    resident_idx = Column(DECIMAL(10, 4))
    commodity_house_idx = Column(DECIMAL(10, 4))
    second_hand_idx = Column(DECIMAL(10, 4))
    commodity_house_below90_idx = Column(DECIMAL(10, 4))
    second_hand_below90_idx = Column(DECIMAL(10, 4))
    commodity_house_between_90_140_idx = Column(DECIMAL(10, 4))
    second_hand_between_90_140_idx = Column(DECIMAL(10, 4))
    commodity_house_above140_idx = Column(DECIMAL(10, 4))
    second_house_above140_idx = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)