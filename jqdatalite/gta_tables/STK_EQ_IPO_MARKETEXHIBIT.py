

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_IPO_MARKETEXHIBIT(Base):
    __tablename__ = "STK_EQ_IPO_MARKETEXHIBIT"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    SECURITYTYPEID = Column(String(12, u'utf8_bin'))
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    LISTEDDATE = Column(DateTime, primary_key=True, nullable=False)
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    CURRENCY = Column(String(12, u'utf8_bin'))
    OPENPRICE = Column(Numeric(9, 3))
    HIGHPRICE = Column(Numeric(9, 3))
    LOWPRICE = Column(Numeric(9, 3))
    CLOSEPRICE = Column(Numeric(9, 3))
    VOLUME = Column(BigInteger)
    AMOUNT = Column(Numeric(16, 2))
    RETURN = Column(Numeric(12, 6))
    ADJUSTEDRETURN = Column(Numeric(12, 6))
    PE = Column(Numeric(8, 2))
    PB = Column(Numeric(8, 2))
    TURNOVERRATE = Column(Numeric(10, 5))
    MARKETRETURN = Column(Numeric(12, 6))
