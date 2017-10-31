

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_NATIONOFDI(Base):
    __tablename__ = "MAC_NATIONOFDI"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    AREACODE = Column(String(20, u'utf8_bin'))
    INVEST = Column(Numeric(18, 4))
    ACCUMULATION = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
