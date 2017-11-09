# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FIXED_INVESTMENT(Base):
    """
    固定资产投资情况
    """
    __tablename__ = "MAC_FIXED_INVESTMENT"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    fixed_assets_investment = Column(DECIMAL(20, 4))
    state_owned = Column(DECIMAL(20, 4))
    real_estate = Column(DECIMAL(20, 4))
    primary = Column(DECIMAL(20, 4))
    secondary = Column(DECIMAL(20, 4))
    tertiary = Column(DECIMAL(20, 4))
    centre_project = Column(DECIMAL(20, 4))
    local_project = Column(DECIMAL(20, 4))
    new_construct = Column(DECIMAL(20, 4))
    expand = Column(DECIMAL(20, 4))
    reconstruct = Column(DECIMAL(20, 4))
    construct_install = Column(DECIMAL(20, 4))
    equipment_purchase = Column(DECIMAL(20, 4))
    other_expense = Column(DECIMAL(20, 4))
    construct_area = Column(DECIMAL(20, 4))
    resident_complete_area = Column(DECIMAL(20, 4))
    new_fixed_assets = Column(DECIMAL(20, 4))
    fixed_assets_investment_yoy = Column(DECIMAL(10, 4))
    state_owned_yoy = Column(DECIMAL(10, 4))
    real_estate_yoy = Column(DECIMAL(10, 4))
    primary_yoy = Column(DECIMAL(10, 4))
    secondary_yoy = Column(DECIMAL(10, 4))
    tertiary_yoy = Column(DECIMAL(10, 4))
    centre_project_yoy = Column(DECIMAL(10, 4))
    local_project_yoy = Column(DECIMAL(10, 4))
    new_construct_yoy = Column(DECIMAL(10, 4))
    expand_yoy = Column(DECIMAL(10, 4))
    reconstruct_yoy = Column(DECIMAL(10, 4))
    construct_install_yoy = Column(DECIMAL(10, 4))
    equipment_purchase_yoy = Column(DECIMAL(10, 4))
    other_expense_yoy = Column(DECIMAL(10, 4))
    construct_area_yoy = Column(DECIMAL(10, 4))
    resident_complete_area_yoy = Column(DECIMAL(10, 4))
    new_fixed_assets_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)