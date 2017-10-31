

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_RETAILSALESYEAR(Base):
    __tablename__ = "MAC_AREA_RETAILSALESYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    AREACODE = Column(String(20, u'utf8_bin'))
    RETAILSUM = Column(Numeric(18, 4))
    CITY = Column(Numeric(18, 4))
    COUNTY = Column(Numeric(18, 4))
    COUNTYBELOW = Column(Numeric(18, 4))
    WHOLESALERETAIL = Column(Numeric(18, 4))
    HOTELS = Column(Numeric(18, 4))
    MANUFACTURING = Column(Numeric(18, 4))
    AGRICULTURAL = Column(Numeric(18, 4))
    OTHERS = Column(Numeric(18, 4))
    RETAILSALESYOY = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
