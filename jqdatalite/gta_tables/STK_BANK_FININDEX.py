

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_BANK_FININDEX(Base):
    __tablename__ = "STK_BANK_FININDEX"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    INSTITUTIONNAME = Column(String(100, u'utf8_bin'))
    SYMBOL = Column(String(400, u'utf8_bin'))
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    TOTALDEPOSITS = Column(Numeric(20, 2))
    TOTALLOANS = Column(Numeric(20, 2))
    RETURNONASSETS = Column(Numeric(20, 4))
    RETURNONCAPITAL = Column(Numeric(20, 4))
    CAPITALADEQUACYRATIO = Column(Numeric(20, 4))
    CORCAPITALADEQUACYRATIO = Column(Numeric(20, 4))
    COSTTOINCOMERATIO = Column(Numeric(20, 4))
    NETCORECAPITAL = Column(Numeric(20, 2))
    NETSUPPLEMENTARYCAPITAL = Column(Numeric(20, 2))
    TOTALRISKWEIGHTEDASSETS = Column(Numeric(20, 2))
