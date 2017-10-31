

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_BBONDSBUY(Base):
    __tablename__ = "MAC_BBONDSBUY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    TRANSACTIONTYPE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TRANSACTIONMATURITYTYPE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AVGINTERESTRATE = Column(Numeric(20, 4))
    AMOUNT = Column(Numeric(20, 4))
