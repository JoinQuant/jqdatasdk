

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_RPT_TRANSACTIONS(Base):
    __tablename__ = "STK_RPT_TRANSACTIONS"

    INSTITUTIONID = Column(BigInteger)
    SYMBOL = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    REPORTSOURCE = Column(String(40, u'utf8_bin'))
    ENDDATE = Column(DateTime)
    RALATEDPARTYID = Column(BigInteger)
    RALATEDPARTY = Column(String(1000, u'utf8_bin'))
    RELATIONID = Column(String(100, u'utf8_bin'))
    RELATION = Column(String(100, u'utf8_bin'))
    RELATIONSHIP = Column(String(1000, u'utf8_bin'))
    TRANSACTIONNATURE = Column(SmallInteger)
    TRANSACTIONDIRECTION = Column(String(100, u'utf8_bin'))
    TRANSACTIONKINDID = Column(String(100, u'utf8_bin'))
    TRANSACTIONKIND = Column(String(100, u'utf8_bin'))
    TRANSACTIONS = Column(String(100, u'utf8_bin'))
    TRANSACTIONRANK = Column(BigInteger)
    TRANSACTIONAMOUNT = Column(Numeric(20, 2))
    TRANSACTIONAMOUNTRATIO = Column(Numeric(10, 4))
    CURRENCYCODE = Column(String(40, u'utf8_bin'))
    CAPTIALEXPENSES = Column(Numeric(20, 2))
    INTERSETRATE = Column(String(100, u'utf8_bin'))
    ENDBANLANCE = Column(Numeric(20, 2))
    TRANSACTIONPRICE = Column(String(400, u'utf8_bin'))
    TRADINGDATE = Column(DateTime)
    TRANSACTIONLIMIT = Column(String(200, u'utf8_bin'))
    TRANSACTIONBANK = Column(String(200, u'utf8_bin'))
    PRICINGPRINCIPLEID = Column(String(100, u'utf8_bin'))
    PRICINGPRINCIPLE = Column(String(100, u'utf8_bin'))
    PROFITINFLUENCESIGN = Column(SmallInteger)
    UPDATEID = Column(BigInteger, primary_key=True)
