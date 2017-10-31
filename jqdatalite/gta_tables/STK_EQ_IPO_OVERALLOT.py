

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_IPO_OVERALLOT(Base):
    __tablename__ = "STK_EQ_IPO_OVERALLOT"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    SECURITYTYPEID = Column(String(12, u'utf8_bin'))
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    ENDDATE = Column(DateTime)
    AVERAGEPRICE = Column(Numeric(10, 2))
    SHARES = Column(Numeric(20, 0))
    OVERALLOTMENTSHARES = Column(Numeric(20, 0))
    OVERALLOTMENTRATIO = Column(Numeric(8, 4))
    ISFULLAMOUNT = Column(String(2, u'utf8_bin'))
    FUNDADDED = Column(Numeric(20, 2))
    EXPENSEADDED = Column(Numeric(20, 2))
    RAISEFUND = Column(Numeric(20, 2))
    RAISENETFUND = Column(Numeric(20, 2))
    RAISEFUNDINFOREIGNCURRENCY = Column(Numeric(20, 2))
    RAISENETFUNDINFOREIGNCURRENCY = Column(Numeric(20, 2))
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    CURRENCY = Column(String(20, u'utf8_bin'))
