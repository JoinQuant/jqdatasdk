

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PARAMETER_AREA(Base):
    __tablename__ = "MAC_PARAMETER_AREA"

    AREACODE = Column(String(20, u'utf8_bin'))
    AREANAME = Column(String(100, u'utf8_bin'))
    ENINDUSTRYNAME = Column(String(200, u'utf8_bin'))
    PROVINCENAME = Column(String(100, u'utf8_bin'))
    CITYNAME = Column(String(100, u'utf8_bin'))
    CONTINENT = Column(String(20, u'utf8_bin'))
    COUNTRYCODE3 = Column(String(20, u'utf8_bin'))
    COUNTRYCODE2 = Column(String(20, u'utf8_bin'))
    CURRENCYCODE = Column(String(20, u'utf8_bin'))
    ENCURRENCYCODE = Column(String(20, u'utf8_bin'))
    CURRENCYNAME = Column(String(100, u'utf8_bin'))
    ENCURRENCYNAME = Column(String(200, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
