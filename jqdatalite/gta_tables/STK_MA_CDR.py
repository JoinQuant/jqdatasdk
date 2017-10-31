

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_CDR(Base):
    __tablename__ = "STK_MA_CDR"

    EVENTID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    CREDITOR = Column(String(1000, u'utf8_bin'))
    CREDITORINSTITUTIONID = Column(Numeric(20, 0))
    DEBTOR = Column(String(1000, u'utf8_bin'))
    DEBTORINSTITUTIONID = Column(Numeric(20, 0))
    TOTALDEBT = Column(Numeric(20, 4))
    PROFIT = Column(Numeric(20, 4))
    DEBTRESTRUCTURINGTYPEID = Column(String(200, u'utf8_bin'))
    DEBTRESTRUCTURINGTYPE = Column(String(200, u'utf8_bin'))
    AMOUNTINVOLVED = Column(Numeric(20, 4))
