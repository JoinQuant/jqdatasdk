

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_LANDRESOURCEY(Base):
    __tablename__ = "MAC_REGION_LANDRESOURCEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    LANDAREA = Column(Numeric(20, 4))
    BUILTDISTRICTAREA = Column(Numeric(20, 4))
    CULTIVATEAREA = Column(Numeric(20, 4))
    AVGCULTIVATEDAREA = Column(Numeric(20, 4))
    POPULATIONDENSITY = Column(Numeric(20, 4))
