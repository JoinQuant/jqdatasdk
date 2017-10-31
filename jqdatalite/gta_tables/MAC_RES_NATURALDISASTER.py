

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_NATURALDISASTER(Base):
    __tablename__ = "MAC_RES_NATURALDISASTER"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    GEOLOGICALDISASTERS = Column(Numeric(10, 2))
    NUMBEROFEARTHQUAKES = Column(Numeric(10, 2))
    REDTIDES = Column(Numeric(10, 2))
    FORESTFIRES = Column(Numeric(10, 2))
    AREAOFFORESTFIRE = Column(Numeric(18, 4))
    AREAOFFORESTDISINSTOC = Column(Numeric(18, 4))
    AREAOFFORESTDISINSTPC = Column(Numeric(18, 4))
    RATIOOFFORESTDISINSTPC = Column(Numeric(10, 4))
    STORMYTIDES = Column(Numeric(10, 2))
    HUGEWAVES = Column(Numeric(10, 2))
