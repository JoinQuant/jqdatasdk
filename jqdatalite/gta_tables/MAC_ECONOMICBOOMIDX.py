

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_ECONOMICBOOMIDX(Base):
    __tablename__ = "MAC_ECONOMICBOOMIDX"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    EARLYWARNINGIDX = Column(Numeric(10, 4))
    CONSISTENCYIDX = Column(Numeric(10, 4))
    LEADINGIDX = Column(Numeric(10, 4))
    LAGGINGIDX = Column(Numeric(10, 4))
