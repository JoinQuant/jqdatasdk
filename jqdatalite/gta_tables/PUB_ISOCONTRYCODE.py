

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class PUB_ISOCONTRYCODE(Base):
    __tablename__ = "PUB_ISOCONTRYCODE"

    COUNTRYCODE_3 = Column(String(6), primary_key=True)
    COUNTRYCODE_NUM = Column(String(12))
    COUNTRYREGIONNAME = Column(String(100))
    COUNTRYREGIONNAME_EN = Column(String(200))
    COUNTRYCODE_2 = Column(String(12))
    CURRENCYCODE = Column(String(6))
