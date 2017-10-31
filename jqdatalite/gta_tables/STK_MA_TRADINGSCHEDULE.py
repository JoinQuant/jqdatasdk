

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_TRADINGSCHEDULE(Base):
    __tablename__ = "STK_MA_TRADINGSCHEDULE"

    EVENTID = Column(Numeric(20, 0))
    SCHEDULEDATE = Column(DateTime)
    PROGRAMSCHEDULE = Column(String(100, u'utf8_bin'))
    PROGRAMSCHEDULEID = Column(String(100, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
