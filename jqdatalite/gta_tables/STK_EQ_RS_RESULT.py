

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_RS_RESULT(Base):
    __tablename__ = "STK_EQ_RS_RESULT"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    SECURITYTYPEID = Column(String(12, u'utf8_bin'))
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    SHORTNAME1 = Column(String(40, u'utf8_bin'))
    SHORTNAME1_EN = Column(String(100, u'utf8_bin'))
    PLACINGCODE1 = Column(String(16, u'utf8_bin'))
    SHORTNAME2 = Column(String(40, u'utf8_bin'))
    SHORTNAME2_EN = Column(String(100, u'utf8_bin'))
    PLACINGCODE2 = Column(String(16, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    RIGHTOFFERINGDECLAREDATE = Column(DateTime)
    AVAILABLESHARES = Column(Numeric(20, 0))
    PLACINGSHARES = Column(Numeric(20, 0))
    PLACINGSHARESLIMITED = Column(Numeric(20, 0))
    PLACINGSHARESUNLIMITED = Column(Numeric(20, 0))
    UNDERWRITINGBALANCESHARES = Column(Numeric(20, 0))
    PLACINGSHARESMAJORHOLDERS = Column(Numeric(20, 0))
    PURCHASESHARES = Column(Numeric(20, 2))
    SUBSCRIPTIONSTATESHARESID = Column(String(40, u'utf8_bin'))
    SUBSCRIPTIONSTATESHARES = Column(String(40, u'utf8_bin'))
    SUBSCRIPTIONSTATELEGALENTITYID = Column(String(40, u'utf8_bin'))
    SUBSCRIPTIONSTATELEGALENTITY = Column(String(40, u'utf8_bin'))
    SUBSCRIPTIONLEGALENTITYID = Column(String(40, u'utf8_bin'))
    SUBSCRIPTIONLEGALENTITY = Column(String(40, u'utf8_bin'))
    SUBSCRIPTIONMAJORHOLDERSID = Column(String(40, u'utf8_bin'))
    SUBSCRIPTIONMAJORHOLDERS = Column(String(40, u'utf8_bin'))
    SUCCESSFULSIGN = Column(String(2, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
    UPDATETIME_EN = Column(DateTime)
