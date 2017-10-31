

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_BONDTRADE(Base):
    __tablename__ = "MAC_BONDTRADE"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    EXCHANGEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TRADEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AMOUNT = Column(Numeric(18, 4))
    TRADEVOLUME = Column(Numeric(18, 4))
