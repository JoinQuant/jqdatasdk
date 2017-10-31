

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHGSYSTFM_BASISPLAN(Base):
    __tablename__ = "STK_SHGSYSTFM_BASISPLAN"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True)
    SYMBOL = Column(String(20, u'utf8_bin'))
    ISADJUSTED = Column(String(2, u'utf8_bin'))
    SUMSHARES = Column(Numeric(20, 0))
    SUMFLOATINGSHARES = Column(Numeric(20, 0))
    PAIDCASHRATIO = Column(Numeric(10, 4))
    MATCHINGCASHRATIO = Column(Numeric(10, 4))
    DIVIDENDRATIO = Column(Numeric(10, 4))
    PAIDSHARESRATIO = Column(Numeric(10, 4))
    MATCHINGSHARESRATIO = Column(Numeric(10, 4))
    BONUSSHARESRATIO = Column(Numeric(10, 4))
    ADDITIONALSHARESRATIO = Column(Numeric(10, 4))
    PAIDCALLWARRANTRATIO = Column(Numeric(10, 4))
    CALLEXERCISEDMETHOD = Column(String(12, u'utf8_bin'))
    CALLEXERCISEDPC = Column(Numeric(10, 4))
    CALLEXERCISEDPRICE = Column(Numeric(10, 4))
    CALLLISTEDDATE = Column(DateTime)
    CALLEXPIRYDATE = Column(DateTime)
    PAIDPUTWARRANTRATIO = Column(Numeric(10, 4))
    PUTEXERCISEDMETHOD = Column(String(12, u'utf8_bin'))
    PUTEXERCISEDPC = Column(Numeric(10, 4))
    PUTEXERCISEDPRICE = Column(Numeric(10, 4))
    PUTLISTEDDATE = Column(DateTime)
    PUTEXPIRYDATE = Column(DateTime)
    STOCKREDUCTIONRATIO = Column(Numeric(10, 4))
    REPURCHASEDSHARES = Column(Numeric(20, 0))
    REPURCHASEDOBJECT = Column(String(200, u'utf8_bin'))
    COMPLETIONDATE = Column(DateTime)
