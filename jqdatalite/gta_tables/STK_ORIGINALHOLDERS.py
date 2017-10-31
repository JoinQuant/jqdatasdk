

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_ORIGINALHOLDERS(Base):
    __tablename__ = "STK_ORIGINALHOLDERS"

    SYMBOL = Column(String(20, u'utf8_bin'))
    RANK = Column(Integer, primary_key=True, nullable=False)
    DECLAREDATE = Column(DateTime)
    FULLNAME = Column(String(200, u'utf8_bin'))
    FULLNAME_EN = Column(String(1000, u'utf8_bin'))
    SHARES = Column(Numeric(20, 2))
    PERCENTAGEHOLDING = Column(Numeric(20, 4))
    LOCKTERM = Column(SmallInteger)
    STARTDATE = Column(DateTime)
    PLANLISTEDDATE = Column(DateTime)
    LISTEDDATE = Column(DateTime)
    LISTEDSHARES = Column(Numeric(20, 2))
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    UPDATETIME_EN = Column(DateTime)
