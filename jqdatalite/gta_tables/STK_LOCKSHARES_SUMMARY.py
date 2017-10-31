

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_LOCKSHARES_SUMMARY(Base):
    __tablename__ = "STK_LOCKSHARES_SUMMARY"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    LISTEDDATE = Column(DateTime, primary_key=True, nullable=False)
    HOLDERNUMBER = Column(BigInteger)
    LISTEDSHARES = Column(Numeric(20, 4))
    TOTALLOCKSHARES = Column(Numeric(20, 4))
    PROPORTION1 = Column(Numeric(10, 4))
    PROPORTION2 = Column(Numeric(10, 4))
    PROPORTION3 = Column(Numeric(10, 4))
    REMAINEDLOCKSHARES = Column(Numeric(20, 4))
