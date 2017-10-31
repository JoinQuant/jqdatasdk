

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_RS_INFO(Base):
    __tablename__ = "STK_EQ_RS_INFO"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    SECURITYTYPEID = Column(String(12, u'utf8_bin'))
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    SIGNDATE = Column(DateTime)
    PUBLICATIONS = Column(String(200, u'utf8_bin'))
    PUBLICATIONS_EN = Column(String(400, u'utf8_bin'))
    WEBSITE = Column(String(200, u'utf8_bin'))
    TRUSTEESHIPENDDATE = Column(DateTime)
    TRUSTEESHIPTRANSFERDATE = Column(DateTime)
    LASTTRADINGDATE = Column(DateTime)
    REGISTERDATE = Column(DateTime)
    EXRIGHTDATE = Column(DateTime)
    UNDERWRITEDSTARTDATE = Column(DateTime)
    UNDERWRITEDENDDATE = Column(DateTime)
    PAYMENTSTARTDATE = Column(DateTime)
    PAYMENTENDDATE = Column(DateTime)
    LISTEDDECLAREDATE = Column(DateTime)
    LISTEDDATE = Column(DateTime)
    OFFERINGTYPE = Column(String(20, u'utf8_bin'))
    PE = Column(Numeric(12, 6))
    EXRIGHTPRICE = Column(Numeric(10, 2))
    UNDERWRITEDMETHODSID = Column(String(12, u'utf8_bin'))
    UNDERWRITEDMETHODS = Column(String(12, u'utf8_bin'))
    TARGETINVESTORS = Column(String(400, u'utf8_bin'))
    TARGETINVESTORS_EN = Column(String(400, u'utf8_bin'))
    PARVALUE = Column(Numeric(10, 2))
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    PRICE = Column(Numeric(10, 4))
    PLACINGRATIO = Column(Numeric(12, 6))
    EXPENSE = Column(Numeric(20, 2))
    SUBSCRIPTIONNONCURRENCY = Column(Numeric(20, 2))
    RAISEFUND = Column(Numeric(20, 2))
    FEEPERSHARE = Column(Numeric(10, 4))
    EPS = Column(Numeric(10, 4))
    EQUITYPERSHARESBEFORE = Column(Numeric(10, 4))
    EQUITYPERSHARESAFTER = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
    UPDATETIME_EN = Column(DateTime)
