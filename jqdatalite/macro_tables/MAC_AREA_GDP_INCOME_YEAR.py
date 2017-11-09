# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_GDP_INCOME_YEAR(Base):
    """
    分地区收入法国内生产总值表(年度)
    """

    __tablename__ = "MAC_AREA_GDP_INCOME_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    gdp_income = Column(DECIMAL(20, 4))
    gdp_employee_payment = Column(DECIMAL(20, 4))
    gdp_net_tax_on_product = Column(DECIMAL(20, 4))
    gdp_fix_asset_depreciation = Column(DECIMAL(20, 4))
    gdp_operate_profit = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)