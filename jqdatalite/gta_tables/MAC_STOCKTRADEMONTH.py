

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_STOCKTRADEMONTH(Base):
    __tablename__ = "MAC_STOCKTRADEMONTH"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    EXCHANGEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    EQUITYFINANCING = Column(Numeric(20, 2))
    TOTALSHARE = Column(Numeric(18, 4))
    MARKETVALUE = Column(Numeric(18, 4))
    NLCEND = Column(Numeric(20, 2))
    AMOUNT = Column(Numeric(18, 4))
    TRADEVOLUME = Column(Numeric(18, 4))
    HIGHINDEXA = Column(Numeric(10, 4))
    HIGHINDEXB = Column(Numeric(10, 4))
    LOWINDEXA = Column(Numeric(10, 4))
    LOWINDEXB = Column(Numeric(10, 4))
    CLOSEINDEX = Column(Numeric(10, 4))
