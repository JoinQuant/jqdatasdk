# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_QUARTER(Base):
    """
    分地区农林牧渔业总产值表(季度累计)
    """
    __tablename__ = "MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_QUARTER"

    id = Column(Integer, primary_key=True)
    stat_quarter = Column(String(20), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    total = Column(DECIMAL(20, 4))
    farming = Column(DECIMAL(20, 4))
    forestry = Column(DECIMAL(20, 4))
    animal_husbandry = Column(DECIMAL(20, 4))
    fishery = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)

    @property
    def update_keys(self):
        return ["total",
                "farming",
                "forestry",
                "animal_husbandry",
                "fishery"]

    @property
    def filter_keys(self):
        return ["stat_quarter", "area_code"]