

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_EQUITYTRANSFER(Base):
    __tablename__ = "STK_MA_EQUITYTRANSFER"

    EVENTID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    SELLER = Column(String(1000, u'utf8_bin'))
    SINSTITUTIONID = Column(Numeric(20, 0))
    BUYER = Column(String(1000, u'utf8_bin'))
    BINSTITUTIONID = Column(Numeric(20, 0))
    EQUITYNATUREBEFORE = Column(String(100, u'utf8_bin'))
    EQUITYNATUREAFTER = Column(String(100, u'utf8_bin'))
    PROPORTION = Column(Numeric(10, 4))
    CHANGETYPEID = Column(String(100, u'utf8_bin'))
    CHANGETYPE = Column(String(200, u'utf8_bin'))
    PRICE = Column(Numeric(10, 3))
    AMOUNT = Column(Numeric(20, 4))
    VOLUME = Column(BigInteger)
    PRICEUNITS = Column(String(200, u'utf8_bin'))
    MAINSCHANGEORNOT = Column(SmallInteger)
    MARKETVALUE = Column(Numeric(20, 4))
    TOTALSHARE = Column(BigInteger)
    MAINSEQUITYRATIOB = Column(Numeric(10, 4))
    TSHARESRATIO = Column(Numeric(10, 4))
    MAINSEQUITYRATIOA = Column(Numeric(10, 4))
