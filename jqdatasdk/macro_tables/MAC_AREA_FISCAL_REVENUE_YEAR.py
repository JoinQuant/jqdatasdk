# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FISCAL_REVENUE_YEAR(Base):
    """
    各地区财政收入表（年度）
    """
    __tablename__ = "MAC_AREA_FISCAL_REVENUE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    general_budget = Column(DECIMAL(20, 4))
    tax = Column(DECIMAL(20, 4))
    add_value_tax = Column(DECIMAL(20, 4))
    business_tax = Column(DECIMAL(20, 4))
    corporate_income_tax = Column(DECIMAL(20, 4))
    individual_income_tax = Column(DECIMAL(20, 4))
    resource_tax = Column(DECIMAL(20, 4))
    adjustment_tax = Column(DECIMAL(20, 4))
    maintenance_construction_tax = Column(DECIMAL(20, 4))
    house_property_tax = Column(DECIMAL(20, 4))
    stamp_tax = Column(DECIMAL(20, 4))
    land_tax = Column(DECIMAL(20, 4))
    land_increment_tax = Column(DECIMAL(20, 4))
    vehicle_vessel_tax = Column(DECIMAL(20, 4))
    land_occupation_tax = Column(DECIMAL(20, 4))
    contract_tax = Column(DECIMAL(20, 4))
    tobacco_tax = Column(DECIMAL(20, 4))
    other_tax = Column(DECIMAL(20, 4))
    non_tax = Column(DECIMAL(20, 4))
    special = Column(DECIMAL(20, 4))
    administration = Column(DECIMAL(20, 4))
    punishment = Column(DECIMAL(20, 4))
    capital_operation = Column(DECIMAL(20, 4))
    asset_use = Column(DECIMAL(20, 4))
    other_non_tax = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)