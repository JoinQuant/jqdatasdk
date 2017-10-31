

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_STOCKPAYMENT(Base):
    __tablename__ = "STK_MA_STOCKPAYMENT"

    EVENTID = Column(Numeric(20, 0), primary_key=True)
    AMOUNT = Column(Numeric(20, 4))
    PRICE = Column(Numeric(10, 3))
    VOLUME = Column(BigInteger)
    PROPORTION = Column(Numeric(10, 4))
    SOURCEID = Column(String(40, u'utf8_bin'))
    SOURCE = Column(String(200, u'utf8_bin'))
