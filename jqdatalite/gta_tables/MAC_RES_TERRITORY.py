

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_TERRITORY(Base):
    __tablename__ = "MAC_RES_TERRITORY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    AREAOFTERRITORY = Column(Numeric(18, 4))
    AREAOFSEA = Column(Numeric(18, 4))
    AVERAGEDEPTHOFSEA = Column(Numeric(18, 4))
    MAXIMUMDEPTHOFSEA = Column(Numeric(18, 4))
    LENGTHOFCOASTLINE = Column(Numeric(18, 4))
    MAINLANDSHORE = Column(Numeric(18, 4))
    ISLANDSHORE = Column(Numeric(18, 4))
    NUMBEROFISLANDS = Column(Numeric(10, 2))
    AREAOFISLANDS = Column(Numeric(18, 4))
    PERCENTAGEOFHUMIDZONE = Column(Numeric(10, 4))
    RATIOOFSEMIHUMIDZONE = Column(Numeric(10, 4))
    PERCENTAGEOFSEMIARIDZONE = Column(Numeric(10, 4))
    PERCENTAGEOFARIDZONE = Column(Numeric(10, 4))
