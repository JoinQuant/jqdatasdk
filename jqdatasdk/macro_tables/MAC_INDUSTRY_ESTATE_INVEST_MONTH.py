# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_ESTATE_INVEST_MONTH(Base):
    """
    房地产开发投资情况表(月度累计)
    """
    __tablename__ = "MAC_INDUSTRY_ESTATE_INVEST_MONTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    invest = Column(DECIMAL(20, 4))
    invest_yoy = Column(DECIMAL(10, 4))
    auxiliary_project = Column(DECIMAL(20, 4))
    auxiliary_project_yoy = Column(DECIMAL(10, 4))
    resident = Column(DECIMAL(20, 4))
    resident_yoy = Column(DECIMAL(10, 4))
    below90_house = Column(DECIMAL(20, 4))
    below90_house_yoy = Column(DECIMAL(10, 4))
    above144_house = Column(DECIMAL(20, 4))
    above144_house_yoy = Column(DECIMAL(10, 4))
    villa_flat = Column(DECIMAL(20, 4))
    villa_flat_yoy = Column(DECIMAL(10, 4))
    office = Column(DECIMAL(20, 4))
    office_yoy = Column(DECIMAL(10, 4))
    business = Column(DECIMAL(20, 4))
    business_yoy = Column(DECIMAL(10, 4))
    other_house = Column(DECIMAL(20, 4))
    other_house_yoy = Column(DECIMAL(10, 4))
    construct = Column(DECIMAL(20, 4))
    construct_yoy = Column(DECIMAL(10, 4))
    install = Column(DECIMAL(20, 4))
    install_yoy = Column(DECIMAL(10, 4))
    equipment_purchase = Column(DECIMAL(20, 4))
    equipment_purchase_yoy = Column(DECIMAL(10, 4))
    other_expense = Column(DECIMAL(20, 4))
    other_expense_yoy = Column(DECIMAL(10, 4))
    land_purchase = Column(DECIMAL(20, 4))
    land_purchase_yoy = Column(DECIMAL(10, 4))
    plan_invest = Column(DECIMAL(20, 4))
    plan_invest_yoy = Column(DECIMAL(10, 4))
    new_fixed_assets = Column(DECIMAL(20, 4))
    new_fixed_assets_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)