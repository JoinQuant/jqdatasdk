

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SALE_RETAILMONTH(Base):
    __tablename__ = "MAC_SALE_RETAILMONTH"

    DECLAREDATE = Column(DateTime)
    SGNMONTH = Column(String(14, u'utf8_bin'))
    DATASIGN = Column(String(4, u'utf8_bin'))
    RETAILSUM = Column(Numeric(18, 4))
    CITY = Column(Numeric(18, 4))
    COUNTY = Column(Numeric(18, 4))
    COUNTYBELOW = Column(Numeric(18, 4))
    WHOLESALERETAIL = Column(Numeric(18, 4))
    HOTELS = Column(Numeric(18, 4))
    MANUFACTURING = Column(Numeric(18, 4))
    AGRICULTURAL = Column(Numeric(18, 4))
    OTHERS = Column(Numeric(18, 4))
    TOWN = Column(Numeric(18, 4))
    RURAL = Column(Numeric(18, 4))
    RETAIL = Column(Numeric(18, 4))
    CATERING = Column(Numeric(18, 4))
    RETAILSUMYOY = Column(Numeric(10, 4))
    CITYYOY = Column(Numeric(10, 4))
    COUNTYYOY = Column(Numeric(10, 4))
    COUNTYBELOWYOY = Column(Numeric(10, 4))
    WHOLESALERETAILYOY = Column(Numeric(10, 4))
    HOTELSYOY = Column(Numeric(10, 4))
    MANUFACTURINGYOY = Column(Numeric(10, 4))
    AGRICULTURALYOY = Column(Numeric(10, 4))
    OTHERSYOY = Column(Numeric(10, 4))
    TOWNYOY = Column(Numeric(10, 4))
    RURALYOY = Column(Numeric(10, 4))
    RETAILYOY = Column(Numeric(10, 4))
    CATERINGYOY = Column(Numeric(10, 4))
    RETAILSUMMOM = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
