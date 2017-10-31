

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_HOUSEHOLDREGISTER(Base):
    __tablename__ = "MAC_AREA_HOUSEHOLDREGISTER"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SAMPLINGFRACTION = Column(Numeric(10, 4))
    POPULATION = Column(Numeric(18, 4))
    MALE = Column(Numeric(18, 4))
    FEMALE = Column(Numeric(18, 4))
    RESIDING = Column(Numeric(18, 4))
    MALERESIDING = Column(Numeric(18, 4))
    FEMALERESIDING = Column(Numeric(18, 4))
    RESIDING6MONTHS = Column(Numeric(18, 4))
    MALERESIDING6MONTHS = Column(Numeric(18, 4))
    FEMALERESIDING6MONTHS = Column(Numeric(18, 4))
    RESIDINGLESS6MONTHS = Column(Numeric(18, 4))
    MALERESIDINGLESS6MONTHS = Column(Numeric(18, 4))
    FEMALERESIDINGLESS6MONTHS = Column(Numeric(18, 4))
    HOUSEHOLDUNSETTLE = Column(Numeric(18, 4))
    MALEHOUSEHOLDUNSETTLE = Column(Numeric(18, 4))
    FEMALEHOUSEHOLDUNSETTLE = Column(Numeric(18, 4))
    ELSEWHERE = Column(Numeric(18, 4))
    MALEELSEWHERE = Column(Numeric(18, 4))
    FEMALEELSEWHERE = Column(Numeric(18, 4))
    RESIDINGABROAD = Column(Numeric(18, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
