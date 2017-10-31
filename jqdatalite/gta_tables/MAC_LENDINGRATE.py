

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_LENDINGRATE(Base):
    __tablename__ = "MAC_LENDINGRATE"

    CHANGEDATE = Column(DateTime, primary_key=True)
    LOAN6MONTH = Column(Numeric(10, 4))
    LOAN1YEAR = Column(Numeric(10, 4))
    LOAN3YEAR = Column(Numeric(10, 4))
    LOAN5YEAR = Column(Numeric(10, 4))
    LOANABOVE5YEAR = Column(Numeric(10, 4))
    DISCOUNT = Column(String(200, u'utf8_bin'))
    OVERDUELOAN = Column(String(200, u'utf8_bin'))
    DIVERTLOAN = Column(String(200, u'utf8_bin'))
    HOUSEFUND5YEAR = Column(Numeric(10, 4))
    HOUSEFUNDABOVE5YEAR = Column(Numeric(10, 4))
    HOUSEDEVELOPMENT = Column(String(200, u'utf8_bin'))
    INDIVIDUALHOUSE6MONTH = Column(Numeric(10, 4))
    INDIVIDUALHOUSE1YEAR = Column(Numeric(10, 4))
    INDIVIDUALHOUSE3YEAR = Column(Numeric(10, 4))
    INDIVIDUALHOUSE5YEAR = Column(Numeric(10, 4))
    INDIVIDUALHOUSEABOVE5YEAR = Column(Numeric(10, 4))
    INDIVIDUALHOUSEFLOOR = Column(String(200, u'utf8_bin'))
    CREDIT = Column(String(200, u'utf8_bin'))
    SHIPPING = Column(Numeric(10, 4))
    HIGHTECHNOLOGY = Column(Numeric(10, 4))
    LOWTECHNOLOGY = Column(Numeric(10, 4))
    FACTORYLOAN = Column(Numeric(10, 4))
    DEVELOPMENTLOAN = Column(Numeric(10, 4))
    INDUSTRYLOAN = Column(Numeric(10, 4))
    PRODUCELOAN = Column(Numeric(10, 4))
    RESERVELOAN = Column(Numeric(10, 4))
    POVERTYALLEVIATIONLOAN = Column(Numeric(10, 4))
