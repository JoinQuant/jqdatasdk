

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_SEO_PUBLICRESULT(Base):
    __tablename__ = "STK_EQ_SEO_PUBLICRESULT"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    SECURITYTYPEID = Column(String(12, u'utf8_bin'))
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    SEO1DECLAREDATE = Column(DateTime)
    SEO2DECLAREDATE = Column(DateTime)
    SUBSCRIPTIONCODE1 = Column(String(20, u'utf8_bin'))
    SHORTNAME1 = Column(String(20, u'utf8_bin'))
    SHORTNAME1_EN = Column(String(100, u'utf8_bin'))
    SUBSCRIPTIONCODE2 = Column(String(20, u'utf8_bin'))
    SHORTNAME2 = Column(String(20, u'utf8_bin'))
    SHORTNAME2_EN = Column(String(100, u'utf8_bin'))
    SHARESUNLIMITED = Column(Numeric(20, 0))
    SHARESOLDER = Column(Numeric(20, 0))
    SHARESOLDERTOISSUE = Column(Numeric(10, 4))
    PURCHASESHARESOLDER = Column(Numeric(20, 0))
    PURCHASEHOUSEHOLDERSOLDER = Column(BigInteger)
    PLACINGOLDER = Column(Numeric(12, 6))
    ONLINEISSUE = Column(Numeric(20, 0))
    ONLINEISSUETOTOTALISSUE = Column(Numeric(10, 4))
    ONLINEPURCHASEHOUSEHOLDERS = Column(BigInteger)
    ONLINEPURCHASESHARES = Column(Numeric(20, 0))
    ONLINESUCCESSRATE = Column(Numeric(12, 6))
    ONLINEOVERSUBSCRIPTIONRATIO = Column(Numeric(10, 4))
    OFFLINEISSUE = Column(Numeric(20, 0))
    OFFLINEISSUETOTOTALISSUE = Column(Numeric(10, 4))
    OFFLINEPURCHASEHOUSEHOLDERS = Column(BigInteger)
    OFFLINEPURCHASESHARES = Column(Numeric(20, 0))
    OFFLINESUCCESSRATE = Column(Numeric(12, 6))
    OFFLINEOVERSUBSCRIPTIONRATIO = Column(Numeric(10, 4))
    UNDERWRITINGBALANCESHARES = Column(Numeric(20, 0))
    CALLBACKSIGN = Column(String(2, u'utf8_bin'))
    CALLBACKTYPEID = Column(String(100, u'utf8_bin'))
    CALLBACKTYPE = Column(String(200, u'utf8_bin'))
    CALLBACKSHARES = Column(Numeric(20, 0))
    PURCHASESHARES = Column(Numeric(20, 0))
    PURCHASEHOUSEHOLDERS = Column(BigInteger)
    OVERSUBSCRIPTIONRATIO = Column(Numeric(10, 4))
    SUCCESSRATE = Column(Numeric(12, 6))
    UPDATEID = Column(BigInteger, primary_key=True)
    UPDATETIME_EN = Column(DateTime)
