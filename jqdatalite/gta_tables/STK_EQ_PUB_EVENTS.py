

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_PUB_EVENTS(Base):
    __tablename__ = "STK_EQ_PUB_EVENTS"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    EVENTTYPEID = Column(String(12, u'utf8_bin'))
    EVENTTYPE = Column(String(40, u'utf8_bin'))
    LISTEDDATE = Column(DateTime)
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    EVENTSTATEID = Column(String(12, u'utf8_bin'))
    DESCRIPTION = Column(String(1000, u'utf8_bin'))
