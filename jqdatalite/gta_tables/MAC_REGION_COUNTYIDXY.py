

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_COUNTYIDXY(Base):
    __tablename__ = "MAC_REGION_COUNTYIDXY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    LANDAREA = Column(Numeric(20, 4))
    POPULATION = Column(Numeric(20, 4))
    GDP = Column(Numeric(20, 4))
    GDP_PRIMARY = Column(Numeric(20, 4))
    GDP_SECONDARY = Column(Numeric(20, 4))
    GDP_INDUSTRY = Column(Numeric(20, 4))
    GDP_TERTIARY = Column(Numeric(20, 4))
    GDP_PERCAPITA = Column(Numeric(20, 4))
    URBANEMPLOY = Column(Numeric(20, 4))
    RURALEMPLOY = Column(Numeric(20, 4))
    AGREMPLOY = Column(Numeric(20, 4))
    FIXEDASSETSINVEST = Column(Numeric(20, 4))
    REVENUE = Column(Numeric(20, 4))
    EXPENSE = Column(Numeric(20, 4))
    AVGINCOME = Column(Numeric(20, 4))
    AVGWAGE = Column(Numeric(20, 4))
    CULTIVATEAREA = Column(Numeric(20, 4))
    GRAINOUTPUT = Column(Numeric(20, 4))
    OUTPUTVALUE = Column(Numeric(20, 4))
    RETAILSUM = Column(Numeric(20, 4))
