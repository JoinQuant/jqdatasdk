

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MANUFACTURING_PMI(Base):
    __tablename__ = "MAC_MANUFACTURING_PMI"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    PMI = Column(Numeric(10, 4))
    PRODIDX = Column(Numeric(10, 4))
    NEWORDERSIDX = Column(Numeric(10, 4))
    NEWEXPORTORDERSIDX = Column(Numeric(10, 4))
    BACKLOGORDERSIDX = Column(Numeric(10, 4))
    FINISHEDPRODIDX = Column(Numeric(10, 4))
    PURCHASEQUANTITYIDX = Column(Numeric(10, 4))
    IMPORTIDX = Column(Numeric(10, 4))
    PURCHASESIDX = Column(Numeric(10, 4))
    RAWMATERIALIDX = Column(Numeric(10, 4))
    EMPLOYIDX = Column(Numeric(10, 4))
    DELIVERYTIMEIDX = Column(Numeric(10, 4))
