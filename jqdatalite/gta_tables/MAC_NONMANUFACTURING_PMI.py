

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_NONMANUFACTURING_PMI(Base):
    __tablename__ = "MAC_NONMANUFACTURING_PMI"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    BUSINESSIDX = Column(Numeric(10, 4))
    NEWORDERSIDX = Column(Numeric(10, 4))
    NEWEXPORTORDERSIDX = Column(Numeric(10, 4))
    BACKLOGORDERSIDX = Column(Numeric(10, 4))
    INVENTORYIDX = Column(Numeric(10, 4))
    INPUTIDX = Column(Numeric(10, 4))
    CHARGEIDX = Column(Numeric(10, 4))
    EMPLOYIDX = Column(Numeric(10, 4))
    DELIVERYTIMEIDX = Column(Numeric(10, 4))
    BUSINESSEXPECTIDX = Column(Numeric(10, 4))
