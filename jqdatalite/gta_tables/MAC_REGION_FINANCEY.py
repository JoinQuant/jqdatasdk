

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_FINANCEY(Base):
    __tablename__ = "MAC_REGION_FINANCEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    DATASIGNID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    DATARANGE = Column(String(100, u'utf8_bin'))
    TOTALLOAN = Column(Numeric(20, 4))
    TOTALDEPOSIT = Column(Numeric(20, 4))
    SAVINGSDEPOSIT = Column(Numeric(20, 4))
