

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_AF_RATINGCHANGE(Base):
    __tablename__ = "STK_AF_RATINGCHANGE"

    REPORTID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    SHORTNAME = Column(String(20, u'utf8_bin'))
    REPORTDATE = Column(DateTime)
    RATERESULT = Column(String(100, u'utf8_bin'))
    STANDARDRATING = Column(String(12, u'utf8_bin'))
    RATERESULTID = Column(String(20, u'utf8_bin'))
    RATINGCHANGEID = Column(String(20, u'utf8_bin'))
