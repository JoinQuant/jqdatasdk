

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_ENTERPRISECONFIDENCEIDX(Base):
    __tablename__ = "MAC_ENTERPRISECONFIDENCEIDX"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    CONFIDENCEIDX = Column(Numeric(10, 4))
    INDUSTRY = Column(Numeric(10, 4))
    CONSTRUCTION = Column(Numeric(10, 4))
    TRANSPORT = Column(Numeric(10, 4))
    WHOLESALERETAIL = Column(Numeric(10, 4))
    REALESTATE = Column(Numeric(10, 4))
    SERVICE = Column(Numeric(10, 4))
    INFORMATION = Column(Numeric(10, 4))
    HOTELCATERING = Column(Numeric(10, 4))
