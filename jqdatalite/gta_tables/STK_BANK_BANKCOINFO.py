

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_BANK_BANKCOINFO(Base):
    __tablename__ = "STK_BANK_BANKCOINFO"

    INSTITUTIONID = Column(BigInteger, primary_key=True, nullable=False)
    INSTITUTIONFULLNAME = Column(String(400, u'utf8_bin'))
    INSTITUTIONFULLNAME_EN = Column(String(1000, u'utf8_bin'))
    INSTITUTIONNAME = Column(String(100, u'utf8_bin'))
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    SYMBOL = Column(String(400, u'utf8_bin'))
    COUNTRYREGIONCODE = Column(String(6, u'utf8_bin'))
    BANKOFNATURE = Column(String(2, u'utf8_bin'))
    ACCOUNTINGSTANDARDS = Column(String(2, u'utf8_bin'))
    DISCRIPTION = Column(String)
    ESTABLISHDATE = Column(String(20, u'utf8_bin'))
    WEBSITE = Column(String(200, u'utf8_bin'))
    PHONE = Column(String(100, u'utf8_bin'))
    FAX = Column(String(200, u'utf8_bin'))
