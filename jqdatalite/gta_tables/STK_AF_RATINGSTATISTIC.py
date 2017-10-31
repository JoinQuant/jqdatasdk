

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_AF_RATINGSTATISTIC(Base):
    __tablename__ = "STK_AF_RATINGSTATISTIC"

    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    STATISTICDATE = Column(DateTime, primary_key=True, nullable=False)
    STATISTICDAYSID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    BUY = Column(Integer)
    OUTPERFORM = Column(Integer)
    NEUTRAL = Column(Integer)
    UNDERPERFORM = Column(Integer)
    SELL = Column(Integer)
    RATESUM = Column(Integer)
    AVGRATE = Column(Numeric(8, 2))
    MASSRATINGID = Column(String(20, u'utf8_bin'))
    RATERESULTID = Column(String(20, u'utf8_bin'))
    RATINGCHANGEID = Column(String(20, u'utf8_bin'))
