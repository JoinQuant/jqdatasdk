

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_INSTITUTIONINFO(Base):
    __tablename__ = "STK_INSTITUTIONINFO"

    INSTITUTIONID = Column(Numeric(20, 0))
    FULLNAME = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    ENNAME = Column(String(400, u'utf8_bin'))
    SYMBOL = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    OWNSHIPID = Column(String(12, u'utf8_bin'))
    ESTABLISHWAYID = Column(String(12, u'utf8_bin'))
    ESTABLISHDATE = Column(DateTime)
    IPODATE = Column(DateTime)
    EXCHANGECODE = Column(String(100, u'utf8_bin'))
    LEGALREPRESENTATIVE = Column(String(100, u'utf8_bin'))
    GENERALMANAGER = Column(String(100, u'utf8_bin'))
    SECRETARY = Column(String(100, u'utf8_bin'))
    SECRETARYTEL = Column(String(100, u'utf8_bin'))
    SECRETARYFAX = Column(String(100, u'utf8_bin'))
    SECRETARYEMAIL = Column(String(200, u'utf8_bin'))
    SECURITYCONSULTANT = Column(String(100, u'utf8_bin'))
    REGISTERCAPITAL = Column(BigInteger)
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    REGISTERADDRESS = Column(String(400, u'utf8_bin'))
    LATESTREGISTERDATE = Column(DateTime)
    OFFICEADDRESS = Column(String(400, u'utf8_bin'))
    ZIPCODE = Column(String(20, u'utf8_bin'))
    BUSINESSLICENSENUMBER = Column(String(100, u'utf8_bin'))
    TAXREGISTRYNO = Column(String(100, u'utf8_bin'))
    WEBSITE = Column(String(200, u'utf8_bin'))
    EMAIL = Column(String(200, u'utf8_bin'))
    DISCLOSEPAPER = Column(String(200, u'utf8_bin'))
    DISCLOSEWEBSITE = Column(String(200, u'utf8_bin'))
    REPORTPLACE = Column(String(200, u'utf8_bin'))
    CITYCODE = Column(String(12, u'utf8_bin'))
    PROVINCECODE = Column(String(12, u'utf8_bin'))
    REGIONCODE = Column(String(6, u'utf8_bin'))
    INDUSTRYCLASSIFICATIONID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    INDUSTRYCODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    CHANGEDATE = Column(DateTime)
    SHORTNAME = Column(String(40, u'utf8_bin'))
    ENSHORTNAME = Column(String(100, u'utf8_bin'))
