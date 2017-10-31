

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PBCMARKET(Base):
    __tablename__ = "MAC_PBCMARKET"

    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    OPENMARKETTYPEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TENDERINGTYPEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TRADINGVARIETY = Column(String(100, u'utf8_bin'), primary_key=True, nullable=False)
    OPENMARKETTERMID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    VOLUME = Column(Numeric(18, 4))
    ISSUEPRICE = Column(Numeric(18, 4))
    REFERENCEINTEREST = Column(Numeric(18, 4))
    BIDINTEREST = Column(Numeric(18, 4))
