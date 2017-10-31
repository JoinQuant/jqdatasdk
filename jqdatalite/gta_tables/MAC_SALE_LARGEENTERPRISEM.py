

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SALE_LARGEENTERPRISEM(Base):
    __tablename__ = "MAC_SALE_LARGEENTERPRISEM"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    RETAILID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SALES = Column(Numeric(18, 4))
    SALESYOY = Column(Numeric(10, 4))
    WHOLESALE = Column(Numeric(18, 4))
    WHOLESALEYOY = Column(Numeric(10, 4))
    RETAIL = Column(Numeric(18, 4))
    RETAILYOY = Column(Numeric(10, 4))
    RETAILNAME = Column(String(100, u'utf8_bin'))
    RETAILNAME_EN = Column(String(400, u'utf8_bin'))
