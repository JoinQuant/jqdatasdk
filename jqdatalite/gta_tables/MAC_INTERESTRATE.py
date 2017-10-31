

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INTERESTRATE(Base):
    __tablename__ = "MAC_INTERESTRATE"

    CHANGEDATE = Column(DateTime, primary_key=True)
    LEGALRESERVERATE = Column(Numeric(10, 4))
    EXCESSRESERVERATE = Column(Numeric(10, 4))
    REFINANCE20DAY = Column(Numeric(10, 4))
    REFINANCE3MONTH = Column(Numeric(10, 4))
    REFINANCE6MONTH = Column(Numeric(10, 4))
    REFINANCE1YEAR = Column(Numeric(10, 4))
    REDISCOUNT = Column(Numeric(10, 4))
