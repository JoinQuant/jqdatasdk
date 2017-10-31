

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_LOCK_SHARES(Base):
    __tablename__ = "STK_LOCK_SHARES"

    SYMBOL = Column(String(20, u'utf8_bin'))
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    FULLNAME = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    FULLNAME_EN = Column(String(1000, u'utf8_bin'))
    REASON = Column(String(200, u'utf8_bin'))
    REASONID = Column(String(60, u'utf8_bin'))
    BEGINNINGSHARES = Column(Numeric(20, 2))
    ADDSHARES = Column(Numeric(20, 2))
    LISTEDSHARES = Column(Numeric(20, 2))
    LISTEDDATE = Column(DateTime)
    ENDSHARES = Column(Numeric(20, 2))
    FIRSTLISTEDSHARES = Column(Numeric(20, 2))
    FIRSTLISTEDDATE = Column(DateTime)
    SECONDLISTEDSHARES = Column(Numeric(20, 2))
    SECONDLISTEDDATE = Column(DateTime)
    THIRDLISTEDSHARES = Column(Numeric(20, 2))
    THIRDLISTEDDATE = Column(DateTime)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    UPDATETIME_EN = Column(DateTime)
