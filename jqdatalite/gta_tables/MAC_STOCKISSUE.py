

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_STOCKISSUE(Base):
    __tablename__ = "MAC_STOCKISSUE"

    SGNYEAR = Column(String(16, u'utf8_bin'), primary_key=True)
    SHAREISSUED = Column(Numeric(20, 4))
    ASHAREISSUED = Column(Numeric(20, 4))
    BSHAREISSUED = Column(Numeric(20, 4))
    HANDNSHAREISSUED = Column(Numeric(20, 4))
    EQUITFINANCINGAMOUNT = Column(Numeric(20, 4))
    ASHAREFINANCINGAMOUNT = Column(Numeric(20, 4))
    ARATIONEDSHAREFINANCING = Column(Numeric(20, 4))
    BSHAREFINANCINGAMOUNT = Column(Numeric(20, 4))
    BRATIONEDSHAREFINANCING = Column(Numeric(20, 4))
    HANDNSHAREFINANCINGAMOUNT = Column(Numeric(20, 4))
    ABRATIONEDSHAREFINANCING = Column(Numeric(20, 4))
