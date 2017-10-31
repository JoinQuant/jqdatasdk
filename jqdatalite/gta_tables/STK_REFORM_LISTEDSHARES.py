

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_REFORM_LISTEDSHARES(Base):
    __tablename__ = "STK_REFORM_LISTEDSHARES"

    INSTITUTIONID = Column(BigInteger)
    SYMBOL = Column(String(20, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    SHAREHOLDERID = Column(BigInteger)
    SHAREHOLDERNAME = Column(String(400, u'utf8_bin'))
    LISTEDDATE = Column(DateTime)
    LOCKSHARES = Column(BigInteger)
    LISTEDSHARES = Column(BigInteger)
    PROPORTION = Column(Numeric(10, 4))
    REMAINEDLOCKSHARES = Column(BigInteger)
    UPDATEID = Column(BigInteger, primary_key=True)
