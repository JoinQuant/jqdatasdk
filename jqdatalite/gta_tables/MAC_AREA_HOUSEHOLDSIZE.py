

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_HOUSEHOLDSIZE(Base):
    __tablename__ = "MAC_AREA_HOUSEHOLDSIZE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SAMPLINGFRACTION = Column(Numeric(10, 4))
    HOUSEHOLD = Column(Numeric(18, 4))
    FAMILYHOUSEHOLD = Column(Numeric(18, 4))
    COLLECTIVE = Column(Numeric(18, 4))
    POPULATION = Column(Numeric(18, 4))
    MALE = Column(Numeric(18, 4))
    FEMALE = Column(Numeric(18, 4))
    SEXRATIO = Column(Numeric(10, 4))
    FAMILYHOUSEHOLDPOPULATION = Column(Numeric(18, 4))
    MALEFAMILYHOUSEHOLD = Column(Numeric(18, 4))
    FEMALEFAMILYHOUSEHOLD = Column(Numeric(18, 4))
    COLLECTIVEPOPULATION = Column(Numeric(18, 4))
    MALECOLLECTIVE = Column(Numeric(18, 4))
    FEMALECOLLECTIVE = Column(Numeric(18, 4))
    AVGHOUSEHOLDSIZE = Column(Numeric(18, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
