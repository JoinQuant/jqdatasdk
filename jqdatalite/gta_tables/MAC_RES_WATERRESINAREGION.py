

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_WATERRESINAREGION(Base):
    __tablename__ = "MAC_RES_WATERRESINAREGION"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    WATERRESOURCESREGIONCODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    WATERRESOURCESREGIONNAME = Column(String(100, u'utf8_bin'))
    TOTALAMOUNT = Column(Numeric(18, 4))
    SURFACE = Column(Numeric(18, 4))
    GROUND = Column(Numeric(18, 4))
    DUPLICATEDMEASUREMENT = Column(Numeric(18, 4))
    NODUPLICATEDMEASUREMENT = Column(Numeric(18, 4))
    TOTALPRECIPITATION = Column(Numeric(18, 4))
