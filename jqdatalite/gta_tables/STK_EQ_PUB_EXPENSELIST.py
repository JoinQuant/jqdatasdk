

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_PUB_EXPENSELIST(Base):
    __tablename__ = "STK_EQ_PUB_EXPENSELIST"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    EVENTTYPEID = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    ACTUALTOTALFLOTATIONCOSTS = Column(Numeric(20, 2))
    EXPENSESUNDERWRITINGSURETY = Column(Numeric(20, 2))
    EXPENSESPONSORSHIP = Column(Numeric(20, 2))
    EXPENSESAUDITING = Column(Numeric(20, 2))
    EXPENSESAPPRAISALASSET = Column(Numeric(20, 2))
    SOLICITORFEE = Column(Numeric(20, 2))
    ONLINEEXPENSESOFFERING = Column(Numeric(20, 2))
    STOCKREGISTRATIONFEE = Column(Numeric(20, 2))
    EXAMINEEXPENSES = Column(Numeric(20, 2))
    EXPENSESDECLARATION = Column(Numeric(20, 2))
    EXPENSESOTHER = Column(Numeric(20, 2))
