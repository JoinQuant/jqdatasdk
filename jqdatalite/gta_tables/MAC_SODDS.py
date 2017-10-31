

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SODDS(Base):
    __tablename__ = "MAC_SODDS"

    SGNMONTH = Column(String(16, u'utf8_bin'), primary_key=True)
    GSISSUE = Column(Numeric(20, 2))
    GSOUTSTANDING = Column(Numeric(20, 2))
    CBBISSUE = Column(Numeric(20, 2))
    CBBOUTSTANDING = Column(Numeric(20, 2))
    FBISSUE = Column(Numeric(20, 2))
    FBOUTSTANDING = Column(Numeric(20, 2))
    CDBISSUE = Column(Numeric(20, 2))
    CDBOUTSTANDING = Column(Numeric(20, 2))
    IIBISSUE = Column(Numeric(20, 2))
    IIBOUTSTANDING = Column(Numeric(20, 2))
    TOTALISSUE = Column(Numeric(20, 2))
    TOTALOUTSTANDING = Column(Numeric(20, 2))
