

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_TRADEIDX_HS2(Base):
    __tablename__ = "MAC_TRADEIDX_HS2"

    SGNMONTH = Column(String(14, u'utf8_bin'))
    HS2ID = Column(BigInteger)
    IMPORTPRICEIDX = Column(Numeric(10, 4))
    IMPORTQUANTITYIDX = Column(Numeric(10, 4))
    IMPORTVALUEIDX = Column(Numeric(10, 4))
    EXPORTPRICEIDX = Column(Numeric(10, 4))
    EXPORTQUANTITYIDX = Column(Numeric(10, 4))
    EXPORTVALUEIDX = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
