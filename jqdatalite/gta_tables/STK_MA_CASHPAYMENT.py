

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_CASHPAYMENT(Base):
    __tablename__ = "STK_MA_CASHPAYMENT"

    EVENTID = Column(Numeric(20, 0), primary_key=True)
    CASHAMOUNT = Column(Numeric(20, 4))
    DEBTAMOUNT = Column(Numeric(20, 4))
    PAYTYPE = Column(SmallInteger)
    FINANCETYPESID = Column(String(40, u'utf8_bin'))
    FINANCETYPES = Column(String(200, u'utf8_bin'))
