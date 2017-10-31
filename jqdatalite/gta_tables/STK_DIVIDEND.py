

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_DIVIDEND(Base):
    __tablename__ = "STK_DIVIDEND"

    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    DIVDENDYEAR = Column(SmallInteger, primary_key=True, nullable=False)
    RANK = Column(SmallInteger, primary_key=True, nullable=False)
    TERMCODE = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    ISDIVIDEND = Column(String(2, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    OBJECT = Column(String(1000, u'utf8_bin'))
    SCHEDULE = Column(String(40, u'utf8_bin'))
    HOLDERSMEETINGDATE = Column(DateTime)
    HOLDERSMEETINGDECLAREDATE = Column(DateTime)
    IMPLEMENTATIONDATE = Column(DateTime)
    PLANBONUSRATIO = Column(Numeric(10, 6))
    PLANCONVERSIONRATIO = Column(Numeric(10, 6))
    PLANDIVIDENTBT = Column(Numeric(10, 6))
    BONUSRATIO = Column(Numeric(10, 6))
    CONVERSIONRATIO = Column(Numeric(10, 6))
    DIVIDENTBT = Column(Numeric(10, 6))
    DIVIDENTAT = Column(Numeric(10, 6))
    RECORDDATE = Column(DateTime)
    EXDIVIDENDDATE = Column(DateTime)
    FINALTRADINGDATE = Column(DateTime)
    PAYMENTDATE = Column(DateTime)
    ADDSHARESLISTINGDATE = Column(DateTime)
    EXCHANGERATEDATE = Column(DateTime)
    DISTRIBUTIONBASESHARES = Column(Numeric(20, 0))
    CURRENCY = Column(String(40, u'utf8_bin'))
    ADDSHARES = Column(Numeric(20, 2))
    TOTALDIVIDENDDISTRI = Column(Numeric(20, 4))
    EVENTID = Column(BigInteger)
