# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_WAGEIDX_YEAR(Base):
    """
    分地区城镇登记失业率
    """

    __tablename__ = "MAC_AREA_WAGEIDX_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    wage = Column(DECIMAL(20, 4))
    wage_state_owned = Column(DECIMAL(20, 4))
    wage_collective = Column(DECIMAL(20, 4))
    wage_others = Column(DECIMAL(20, 4))
    wage_yoy = Column(DECIMAL(10, 4))
    wage_state_owned_yoy = Column(DECIMAL(10, 4))
    wage_collective_yoy = Column(DECIMAL(10, 4))
    wage_others_yoy = Column(DECIMAL(10, 4))
    wage_avg = Column(DECIMAL(20, 4))
    wage_employ_avg = Column(DECIMAL(20, 4))
    wage_state_owned_avg = Column(DECIMAL(20, 4))
    wage_collective_avg = Column(DECIMAL(20, 4))
    wage_others_avg = Column(DECIMAL(20, 4))
    wage_avg_yoy = Column(DECIMAL(10, 4))
    wage_employ_avg_yoy = Column(DECIMAL(10, 4))
    wage_state_owned_avg_yoy = Column(DECIMAL(10, 4))
    wage_collective_avg_yoy = Column(DECIMAL(10, 4))
    wage_others_avg_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)