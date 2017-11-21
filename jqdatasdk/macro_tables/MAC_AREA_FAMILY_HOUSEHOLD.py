# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FAMILY_HOUSEHOLD(Base):
    """
    各地区按家庭户规模分的户数表
    """
    __tablename__ = "MAC_AREA_FAMILY_HOUSEHOLD"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    family_household = Column(DECIMAL(20, 4))
    one_persons = Column(DECIMAL(20, 4))
    two_persons = Column(DECIMAL(20, 4))
    three_persons = Column(DECIMAL(20, 4))
    four_persons = Column(DECIMAL(20, 4))
    five_persons = Column(DECIMAL(20, 4))
    six_persons = Column(DECIMAL(20, 4))
    seven_persons = Column(DECIMAL(20, 4))
    eight_persons = Column(DECIMAL(20, 4))
    nine_persons = Column(DECIMAL(20, 4))
    over_ten_persons = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)