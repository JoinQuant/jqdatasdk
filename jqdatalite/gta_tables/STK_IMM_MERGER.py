

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_IMM_MERGER(Base):
    __tablename__ = "STK_IMM_MERGER"

    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    COMBINATIONSECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    COMBINATIONSYMBOL = Column(String(20, u'utf8_bin'))
    VALIDPERIOD = Column(SmallInteger)
    SCHEDULE = Column(String(40, u'utf8_bin'))
    SCHEDULECODE = Column(String(40, u'utf8_bin'))
    GENERALMEETINGDATE = Column(DateTime)
    PLANCONVERSIONRATIO = Column(String(40, u'utf8_bin'))
    AVERAGEPRICE = Column(Numeric(10, 6))
    COMBINATIONPRICE = Column(Numeric(10, 6))
    PREMIUMOBJECT = Column(String(20, u'utf8_bin'))
    PREMIUMRATE = Column(Numeric(10, 6))
    CASHOPTIONPRICE = Column(Numeric(10, 6))
    CASHOPTIONSTARTDATE = Column(DateTime)
    CASHOPTIONENDDATE = Column(DateTime)
    COMBINATIONCASHOPTIONPRICE = Column(Numeric(10, 6))
    COMBINATIONSTARTDATE = Column(DateTime)
    COMBINATIONENDDATE = Column(DateTime)
    IMPLEMENTATIONDATE = Column(DateTime)
    CONVERSIONRATIO = Column(Numeric(10, 6))
    BENCHMARKPRICE = Column(Numeric(10, 6))
    COMBINATIONBENCHMARKPRICE = Column(Numeric(10, 6))
    CONVERTDATE = Column(DateTime)
    TRANSACTIONDATE = Column(DateTime)
    ADDSHARES = Column(Numeric(20, 2))
