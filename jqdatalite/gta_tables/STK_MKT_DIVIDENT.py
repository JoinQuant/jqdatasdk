

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MKT_DIVIDENT(Base):
    __tablename__ = "STK_MKT_DIVIDENT"

    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    EXDIVIDENDDATE = Column(DateTime, primary_key=True, nullable=False)
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    RECORDDATE = Column(DateTime)
    FINALTRADINGDATE = Column(DateTime)
    PAYMENTDATE = Column(DateTime)
    CURRENCYCODE = Column(String(40, u'utf8_bin'))
    ALLOTMENTPRICE = Column(Numeric(10, 4))
    ALLOTMENTPERSHARE = Column(Numeric(10, 6))
    DIVIDENTBT = Column(Numeric(10, 6))
    DIVIDENTAT = Column(Numeric(10, 6))
    BONUSRATIO = Column(Numeric(10, 6))
    CONVERSIONRATIO = Column(Numeric(10, 6))
