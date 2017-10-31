

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_POPEDUCATION(Base):
    __tablename__ = "MAC_AREA_POPEDUCATION"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SAMPLINGFRACTION = Column(Numeric(10, 4))
    AGEOVER6 = Column(Numeric(18, 4))
    MALEAGEOVER6 = Column(Numeric(18, 4))
    FEMALEAGEOVER6 = Column(Numeric(18, 4))
    NOSCHOOLING = Column(Numeric(18, 4))
    MALENOSCHOOLING = Column(Numeric(18, 4))
    FEMALENOSCHOOLING = Column(Numeric(18, 4))
    PRIMARYSCHOOL = Column(Numeric(18, 4))
    MALEPRIMARYSCHOOL = Column(Numeric(18, 4))
    FEMALEPRIMARYSCHOOL = Column(Numeric(18, 4))
    JUNIORSECONDARYSCHOOL = Column(Numeric(18, 4))
    MALEJUNIORSECONDARYSCHOOL = Column(Numeric(18, 4))
    FEMALEJUNIORSECONDARYSCHOOL = Column(Numeric(18, 4))
    SENIORSECONDARYSCHOOL = Column(Numeric(18, 4))
    MALESENIORSECONDARYSCHOOL = Column(Numeric(18, 4))
    FEMALESENIORSECONDARYSCHOOL = Column(Numeric(18, 4))
    COLLEGE = Column(Numeric(18, 4))
    MALECOLLEGE = Column(Numeric(18, 4))
    FEMALECOLLEGE = Column(Numeric(18, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
