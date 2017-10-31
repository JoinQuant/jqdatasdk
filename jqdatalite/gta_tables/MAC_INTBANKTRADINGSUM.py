

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INTBANKTRADINGSUM(Base):
    __tablename__ = "MAC_INTBANKTRADINGSUM"

    TRADINGDATE = Column(DateTime, primary_key=True)
    WEIGHTEDRATE = Column(Numeric(9, 4))
    BASEPOINT = Column(Numeric(9, 4))
    AMOUNT = Column(Numeric(9, 4))
    AMOUNTADJUST = Column(Numeric(9, 4))
    TRADINGCOUNT = Column(Integer)
    TRADINGCOUNTADJUST = Column(Integer)
    PARTICIPATORSUM = Column(Integer)
