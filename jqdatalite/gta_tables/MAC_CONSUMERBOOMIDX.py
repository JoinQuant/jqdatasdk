

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_CONSUMERBOOMIDX(Base):
    __tablename__ = "MAC_CONSUMERBOOMIDX"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    EXPECTATIONIDX = Column(Numeric(10, 4))
    SATISFACTIONIDX = Column(Numeric(10, 4))
    CONFIDENCEIDX = Column(Numeric(10, 4))
