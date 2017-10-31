

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_OTHERPARTY(Base):
    __tablename__ = "STK_MA_OTHERPARTY"

    EVENTID = Column(Numeric(20, 0))
    INSTITUTIONID = Column(Numeric(20, 0))
    INSTITUTIONFULLNAME = Column(String(1000, u'utf8_bin'))
    RELATIONSHIP = Column(String(200, u'utf8_bin'))
    RELATIONSHIPID = Column(String(100, u'utf8_bin'))
    TRADINGPOSITION = Column(String(100, u'utf8_bin'))
    TRADINGPOSITIONID = Column(String(40, u'utf8_bin'))
    LISTINGSIGN = Column(String(4, u'utf8_bin'))
    SYMBOL = Column(String(20, u'utf8_bin'))
    SHORTNAME = Column(String(100, u'utf8_bin'))
    COMPANYPROPERTY = Column(String(40, u'utf8_bin'))
    COMPANYPROPERTYID = Column(String(100, u'utf8_bin'))
    INDUSTRYNAME = Column(String(200, u'utf8_bin'))
    INDUSTRYCODE = Column(String(40, u'utf8_bin'))
    COUNTRYCODE = Column(String(40, u'utf8_bin'))
    REGISTEREDADDRESS = Column(String(400, u'utf8_bin'))
    OFFICEADDRESS = Column(String(400, u'utf8_bin'))
    OFFICEZIPCODE = Column(String(40, u'utf8_bin'))
    TEL = Column(String(200, u'utf8_bin'))
    FAX = Column(String(200, u'utf8_bin'))
    WEBSITE = Column(String(200, u'utf8_bin'))
    EMAIL = Column(String(200, u'utf8_bin'))
    RANK = Column(BigInteger)
    UPDATEID = Column(BigInteger, primary_key=True)
    UPDATEID1 = Column(BigInteger)
    UPDATEID2 = Column(BigInteger)
