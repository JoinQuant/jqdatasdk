

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INTRATE(Base):
    __tablename__ = "MAC_INTRATE"

    TRADINGDATE = Column(DateTime, primary_key=True, nullable=False)
    AREAINTERSETRATEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    VARIETYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    INTERSETRATE = Column(Numeric(8, 4))
    VARIETYNAME = Column(String(100, u'utf8_bin'))
