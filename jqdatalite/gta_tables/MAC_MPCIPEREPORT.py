

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MPCIPEREPORT(Base):
    __tablename__ = "MAC_MPCIPEREPORT"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    EXCHANGESGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    INDUSTRYCODE = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AVERAGEPE = Column(Numeric(10, 2))
