

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_COMMERCIALBILL(Base):
    __tablename__ = "MAC_COMMERCIALBILL"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    COMMERBILLEXCHANGEAMOUNT = Column(Numeric(20, 4))
    COMMERBILLUNEXPIREDAMOUNT = Column(Numeric(20, 4))
    DISCOUNTPAID = Column(Numeric(20, 4))
    DISCOUNTCLOSINGBALANCE = Column(Numeric(20, 4))
    REDISCOUNTPAID = Column(Numeric(20, 4))
    REDISCOUNTPAIDCLOSINGBALANC = Column(Numeric(20, 4))
