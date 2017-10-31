

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FAMILYHOUSEHOLD(Base):
    __tablename__ = "MAC_AREA_FAMILYHOUSEHOLD"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SAMPLINGFRACTION = Column(Numeric(10, 4))
    FAMILYHOUSEHOLD = Column(Numeric(18, 4))
    ONEPERSON = Column(Numeric(18, 4))
    TWOPERSONS = Column(Numeric(18, 4))
    THREEPERSONS = Column(Numeric(18, 4))
    FOURPERSONS = Column(Numeric(18, 4))
    FIVEPERSONS = Column(Numeric(18, 4))
    SIXPERSONS = Column(Numeric(18, 4))
    SEVENPERSONS = Column(Numeric(18, 4))
    EIGHTPERSONS = Column(Numeric(18, 4))
    NINEPERSONS = Column(Numeric(18, 4))
    OVERTENPERSONS = Column(Numeric(18, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
