

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_ENVIROTREATINVEST(Base):
    __tablename__ = "MAC_RES_ENVIROTREATINVEST"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    TOTALINVESTINTPOLLUTION = Column(Numeric(18, 4))
    INVESTINURBANINFRASTRUCT = Column(Numeric(18, 4))
    GASSUPPLY = Column(Numeric(18, 4))
    CENTRALIZEDHEATING = Column(Numeric(18, 4))
    DRAINAGEWORKS = Column(Numeric(18, 4))
    GARDENINGANDGREENING = Column(Numeric(18, 4))
    ENVIRONMENTALSANITATION = Column(Numeric(18, 4))
    INVESTOFINDUSTRIALPOLLUT = Column(Numeric(18, 4))
    TREATMENTOFWASTEWATER = Column(Numeric(18, 4))
    TREATMENTOFWASTEGAS = Column(Numeric(18, 4))
    TREATMENTOFSOLIDWASTE = Column(Numeric(18, 4))
    TREATMENTOFNOISEPOLLUTION = Column(Numeric(18, 4))
    TREATMENTOFOTHERPOLLUTION = Column(Numeric(18, 4))
    THREESIMULTANEITIESINVEST = Column(Numeric(18, 4))
    INVESTMENTASPERCENTOFGDP = Column(Numeric(10, 4))
