

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_TRADINGMAIN(Base):
    __tablename__ = "STK_MA_TRADINGMAIN"

    EVENTID = Column(Numeric(20, 0))
    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20, u'utf8_bin'))
    FIRSTDECLAREDATE = Column(DateTime)
    FINISHDECLAREDATE = Column(DateTime)
    ISSUCCEED = Column(String(4, u'utf8_bin'))
    TRADINGPOSITIONID = Column(String(40, u'utf8_bin'))
    TRADINGPOSITION = Column(String(100, u'utf8_bin'))
    RESTRUCTURINGTYPE = Column(String(100, u'utf8_bin'))
    RESTRUCTURINGTYPEID = Column(String(100, u'utf8_bin'))
    UNDERLYINGTYPE = Column(String(100, u'utf8_bin'))
    UNDERLYINGTYPEID = Column(String(40, u'utf8_bin'))
    UNDERLYINGVALUE = Column(Numeric(20, 4))
    EXPENSEVALUE = Column(Numeric(20, 4))
    RELEVANCESIGN = Column(String(4, u'utf8_bin'))
    MAJORRESTRUCTURINGSIGN = Column(String(4, u'utf8_bin'))
    ASSESSINSTITUTION = Column(String(400, u'utf8_bin'))
    FINANCIALADVISER = Column(String(400, u'utf8_bin'))
    ACCOUNTINGFIRM = Column(String(400, u'utf8_bin'))
    LAWFIRM = Column(String(400, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
    LATESTDECLAREDATE = Column(DateTime)
    PAYTYPEID = Column(String(40, u'utf8_bin'))
