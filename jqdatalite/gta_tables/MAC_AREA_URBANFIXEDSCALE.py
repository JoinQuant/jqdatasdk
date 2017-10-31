

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_URBANFIXEDSCALE(Base):
    __tablename__ = "MAC_AREA_URBANFIXEDSCALE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    INVESTBELOW5MILLION = Column(Numeric(18, 4))
    INVEST100MILLION = Column(Numeric(18, 4))
    INVEST500MILLION = Column(Numeric(18, 4))
    INVEST1BILLION = Column(Numeric(18, 4))
    INVESTABOVE1BILLION = Column(Numeric(18, 4))
