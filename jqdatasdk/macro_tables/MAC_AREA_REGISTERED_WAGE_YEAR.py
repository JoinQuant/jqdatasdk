# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_REGISTERED_WAGE_YEAR(Base):
    """
    分地区按注册类型分城镇单位就业人员工资情况表(年度)
    """

    __tablename__ = "MAC_AREA_REGISTERED_WAGE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    wage_avg = Column(DECIMAL(20, 4))
    wage_avg_state_owned = Column(DECIMAL(20, 4))
    wage_avg_collective = Column(DECIMAL(20, 4))
    wage_avg_stock_cooperate = Column(DECIMAL(20, 4))
    wage_avg_joint_ownership = Column(DECIMAL(20, 4))
    wage_avg_limited = Column(DECIMAL(20, 4))
    wage_avg_stock = Column(DECIMAL(20, 4))
    wage_avg_private = Column(DECIMAL(20, 4))
    wage_avg_hkmt = Column(DECIMAL(20, 4))
    wage_avg_foreign = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)