

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_POPMARITAL(Base):
    __tablename__ = "MAC_AREA_POPMARITAL"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SAMPLINGFRACTION = Column(Numeric(10, 4))
    AGEOVER15 = Column(Numeric(18, 4))
    MALEAGEOVER15 = Column(Numeric(18, 4))
    FEMALEAGEOVER15 = Column(Numeric(18, 4))
    NEVERMARRIED = Column(Numeric(18, 4))
    MALENEVERMARRIED = Column(Numeric(18, 4))
    FEMALENEVERMARRIED = Column(Numeric(18, 4))
    FIRSTMARRIED = Column(Numeric(18, 4))
    MALEFIRSTMARRIED = Column(Numeric(18, 4))
    FEMALEFIRSTMARRIED = Column(Numeric(18, 4))
    REMARRIED = Column(Numeric(18, 4))
    MALEREMARRIED = Column(Numeric(18, 4))
    FEMALEREMARRIED = Column(Numeric(18, 4))
    DIVORCED = Column(Numeric(18, 4))
    MALEDIVORCED = Column(Numeric(18, 4))
    FEMALEDIVORCED = Column(Numeric(18, 4))
    WIDOWED = Column(Numeric(18, 4))
    MALEWIDOWED = Column(Numeric(18, 4))
    FEMALEWIDOWED = Column(Numeric(18, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
