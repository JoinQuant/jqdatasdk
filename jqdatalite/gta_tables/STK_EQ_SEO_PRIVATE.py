

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_SEO_PRIVATE(Base):
    __tablename__ = "STK_EQ_SEO_PRIVATE"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    SECURITYTYPEID = Column(String(12, u'utf8_bin'))
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    REGISTERDATE = Column(DateTime)
    CHANGEDATE = Column(DateTime)
    LISTEDDATE = Column(DateTime)
    UNDERWRITEDMETHODSID = Column(String(12, u'utf8_bin'))
    UNDERWRITEDMETHODS = Column(String(20, u'utf8_bin'))
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    PRICE = Column(Numeric(8, 2))
    ISSUESHARES = Column(Numeric(20, 0))
    RAISEFUND = Column(Numeric(20, 2))
    EXPENSE = Column(Numeric(20, 2))
    FEEPERSHARE = Column(Numeric(10, 4))
    RAISENETFUND = Column(Numeric(20, 2))
    PE1 = Column(Numeric(10, 4))
    PE2 = Column(Numeric(10, 4))
    PB = Column(Numeric(10, 4))
    EPS = Column(Numeric(10, 4))
    EQUITYPERSHAREBEFORE = Column(Numeric(10, 4))
    EQUITYPERSHAREAFTER = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
