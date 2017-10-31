

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSAGENCYY(Base):
    __tablename__ = "MAC_INSAGENCYY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0))
    FULLNAME = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    FOUNDDATE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    REGISTEREDCAPITAL = Column(Numeric(22, 4))
    HOLDERS = Column(Numeric(20, 0))
    STAFFS = Column(Numeric(20, 0))
    LEGALPERSON = Column(String(40, u'utf8_bin'))
    ASSET = Column(Numeric(22, 4))
    LIABILITY = Column(Numeric(22, 4))
    OWNERSEQUITY = Column(Numeric(22, 4))
    INSURANCEREVENUE = Column(Numeric(22, 4))
    OPERATINGREVENUE = Column(Numeric(22, 4))
    OPERATINGEXPENSE = Column(Numeric(22, 4))
    OPERATINGPROFIT = Column(Numeric(22, 4))
    PROFITBEFORETAX = Column(Numeric(22, 4))
    NETPROFIT = Column(Numeric(22, 4))
    CURRENTASSETS = Column(Numeric(22, 4))
    TOTALFIXEDASSETS = Column(Numeric(22, 4))
    INTANGIBLEASSETS = Column(Numeric(22, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
