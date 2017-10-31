

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_EXCHANGERATEQUOTE(Base):
    __tablename__ = "MAC_EXCHANGERATEQUOTE"

    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    CURRENCYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    CASHBUYRATE = Column(Numeric(18, 4))
    CASHBUY = Column(Numeric(18, 4))
    SPOTSELL = Column(Numeric(18, 4))
    CASHOFFERPRC = Column(Numeric(18, 4))
    BANKREDUCEDPRC = Column(Numeric(18, 4))
