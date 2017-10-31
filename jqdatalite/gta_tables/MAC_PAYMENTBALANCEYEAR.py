

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PAYMENTBALANCEYEAR(Base):
    __tablename__ = "MAC_PAYMENTBALANCEYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    ITEMID = Column(String(20, u'utf8_bin'))
    BALANCE = Column(Numeric(18, 4))
    CREDIT = Column(Numeric(18, 4))
    DEBIT = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
