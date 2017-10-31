

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_EMPLOYWAGEQ(Base):
    __tablename__ = "MAC_AREA_EMPLOYWAGEQ"

    SGNQUARTER = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    OBJECTID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    EMPLOY = Column(Numeric(18, 4))
    EMPLOYCHANGE = Column(Numeric(18, 4))
    REWARD = Column(Numeric(18, 4))
    REWARDYOY = Column(Numeric(10, 4))
    AVGEMPLOYWAGE = Column(Numeric(18, 4))
    AVGEMPLOYWAGEYOY = Column(Numeric(10, 4))
    STAFF = Column(Numeric(18, 4))
    STAFFCHANGE = Column(Numeric(18, 4))
    STAFFWAGE = Column(Numeric(18, 4))
    STAFFWAGEYOY = Column(Numeric(10, 4))
    AVGSTAFFWAGE = Column(Numeric(18, 4))
    AVGSTAFFWAGEYOY = Column(Numeric(10, 4))
