

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_LENDRATE(Base):
    __tablename__ = "MAC_LENDRATE"

    TRADINGDATE = Column(DateTime, primary_key=True, nullable=False)
    CURRENCYCODE = Column(String(6, u'utf8_bin'))
    CURRENCYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    MARKETID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    TERMID = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    INTERSETRATE = Column(Numeric(8, 5))
