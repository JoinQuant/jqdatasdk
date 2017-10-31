

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_LANDUSEBYREGION(Base):
    __tablename__ = "MAC_RES_LANDUSEBYREGION"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    AREAUNDERLANDSURVEY = Column(Numeric(18, 4))
    LANDFORAGRICULTURALUSE = Column(Numeric(18, 4))
    GARDENLAND = Column(Numeric(18, 4))
    GRAZINGANDPASTURELAND = Column(Numeric(18, 4))
    LANDFORCONSTRUCTION = Column(Numeric(18, 4))
    LANDFORINHABITATIONMINING = Column(Numeric(18, 4))
    LANDFORTRANSPORTFACILITIES = Column(Numeric(18, 4))
    WATERCONSERVANCYFACILITIES = Column(Numeric(18, 4))
