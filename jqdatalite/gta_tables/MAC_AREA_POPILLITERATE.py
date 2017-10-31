

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_POPILLITERATE(Base):
    __tablename__ = "MAC_AREA_POPILLITERATE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SAMPLINGFRACTION = Column(Numeric(10, 4))
    AGEOVER15 = Column(Numeric(18, 4))
    MALEAGEOVER15 = Column(Numeric(18, 4))
    FEMALEAGEOVER15 = Column(Numeric(18, 4))
    ILLITERATE = Column(Numeric(18, 4))
    MALEILLITERATE = Column(Numeric(18, 4))
    FEMALEILLITERATE = Column(Numeric(18, 4))
    PERCENTAGE = Column(Numeric(10, 4))
    MALEPERCENTAGE = Column(Numeric(10, 4))
    FEMALEPERCENTAGE = Column(Numeric(10, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
