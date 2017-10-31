

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSAREAY(Base):
    __tablename__ = "MAC_INSAREAY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    INCOMES = Column(Numeric(22, 4))
    PROPERTYINCOMES = Column(Numeric(22, 4))
    PROPERTYRATE = Column(Numeric(20, 4))
    PERSONALINCOMES = Column(Numeric(22, 4))
    PERSONALRATE = Column(Numeric(20, 4))
    DENSITY = Column(Numeric(20, 2))
    PROPERTYDENSITY = Column(Numeric(20, 2))
    PERSONALDENSITY = Column(Numeric(20, 2))
    DEPTH = Column(Numeric(20, 4))
    PROPERTYDEPTH = Column(Numeric(20, 4))
    PERSONALDEPTH = Column(Numeric(20, 4))
    PREMIUMS = Column(Numeric(22, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
