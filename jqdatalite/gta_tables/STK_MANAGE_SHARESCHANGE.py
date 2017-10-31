

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_SHARESCHANGE(Base):
    __tablename__ = "STK_MANAGE_SHARESCHANGE"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    CHANGEDATE = Column(DateTime)
    FILLINGDATE = Column(DateTime)
    SHAREHOLDERNAME = Column(String(400, u'utf8_bin'))
    MANAGENAME = Column(String(100, u'utf8_bin'))
    MANAGEPOSITION = Column(String(200, u'utf8_bin'))
    RELATIONSHIPID = Column(String(12, u'utf8_bin'))
    RELATIONSHIP = Column(String(100, u'utf8_bin'))
    SHARESTYPEID = Column(String(12, u'utf8_bin'))
    SHARESTYPE = Column(String(12, u'utf8_bin'))
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    BEFORECHANGINGSHARES = Column(Numeric(20, 2))
    CHANGINGSHARES = Column(Numeric(20, 2))
    AFTERCHANGINGSHARES = Column(Numeric(20, 2))
    AVGTRADINGPRICE = Column(Numeric(20, 4))
    CHANGEMETHODID = Column(String(12, u'utf8_bin'))
    CHANGEMETHOD = Column(String(200, u'utf8_bin'))
    CHANGEPERCENTAGE = Column(Numeric(20, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
