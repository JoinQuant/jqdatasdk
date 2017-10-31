

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_HEALTHY(Base):
    __tablename__ = "MAC_REGION_HEALTHY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    DATASIGNID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    DATARANGE = Column(String(100, u'utf8_bin'))
    HOSPITAL = Column(Numeric(20, 4))
    HOSPITALBED = Column(Numeric(20, 4))
    DOCTOR = Column(Numeric(20, 4))
    THEATER = Column(Numeric(20, 4))
    LIBRAYBOOK = Column(Numeric(20, 4))
    LIBRAYBOOKPERHUNDRED = Column(Numeric(20, 4))
