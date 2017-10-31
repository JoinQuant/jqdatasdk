

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_PUB_EARNFORECAST(Base):
    __tablename__ = "STK_EQ_PUB_EARNFORECAST"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    EVENTTYPEID = Column(String(12, u'utf8_bin'))
    YEARSIGN = Column(DateTime, primary_key=True, nullable=False)
    OPERATINGEVENUE = Column(Numeric(16, 2))
    OPERATINGCOSTS = Column(Numeric(16, 2))
    GROSSPROFIT = Column(Numeric(16, 2))
    EXPENSESOPERATING = Column(Numeric(16, 2))
    EXPENSESADMINISTRATION = Column(Numeric(16, 2))
    EXPENSESFINANCE = Column(Numeric(16, 2))
    OPERATIONPROFIT = Column(Numeric(16, 2))
    INCOMEINVESTMENT = Column(Numeric(20, 2))
    TOTALPROFIT = Column(Numeric(16, 2))
    TAXRATE = Column(Numeric(10, 2))
    INCOMETAX = Column(Numeric(16, 2))
    NETPROFIT = Column(Numeric(16, 2))
    PROFITPARENT = Column(Numeric(16, 2))
    EPSWEIGHTING = Column(Numeric(10, 4))
    EPSDILUTION = Column(Numeric(10, 4))
    NAVPS = Column(Numeric(16, 2))
    NETPROFITTAX15 = Column(Numeric(16, 2))
    NETPROFITTAX33 = Column(Numeric(16, 2))
