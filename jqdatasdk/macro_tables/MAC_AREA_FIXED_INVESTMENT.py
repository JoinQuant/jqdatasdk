# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FIXED_INVESTMENT(Base):
    """
    分地区固定资产投资情况
    """
    __tablename__ = "MAC_AREA_FIXED_INVESTMENT"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    fixed_assets_investment = Column(DECIMAL(20, 4))
    construct_install = Column(DECIMAL(20, 4))
    equipment_purchase = Column(DECIMAL(20, 4))
    other_expense = Column(DECIMAL(20, 4))
    resident_construct = Column(DECIMAL(20, 4))
    construct_area = Column(DECIMAL(20, 4))
    resident_complete = Column(DECIMAL(20, 4))
    construct_num = Column(Integer)
    new_construct_num = Column(Integer)
    fixed_assets_investment_yoy = Column(DECIMAL(10, 4))
    construct_install_yoy = Column(DECIMAL(10, 4))
    equipment_purchase_yoy = Column(DECIMAL(10, 4))
    other_expense_yoy = Column(DECIMAL(10, 4))
    resident_construct_yoy = Column(DECIMAL(10, 4))
    construct_area_yoy = Column(DECIMAL(10, 4))
    resident_complete_yoy = Column(DECIMAL(10, 4))
    construct_num_yoy = Column(DECIMAL(10, 4))
    new_construct_num_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)