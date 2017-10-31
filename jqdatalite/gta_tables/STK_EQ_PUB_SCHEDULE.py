

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_PUB_SCHEDULE(Base):
    __tablename__ = "STK_EQ_PUB_SCHEDULE"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    EVENTTYPEID = Column(String(12, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'))
    FULLNAME_EN = Column(String(600, u'utf8_bin'))
    RELATIVEDATE = Column(String(12, u'utf8_bin'))
    ABSOLUTEDATE = Column(DateTime, primary_key=True, nullable=False)
    ISSUESTEP = Column(String(400, u'utf8_bin'))
    ANNOUNCEMENTFILE = Column(String(400, u'utf8_bin'))
    UPDATETIME_EN = Column(DateTime)
