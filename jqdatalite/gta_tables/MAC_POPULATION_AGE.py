

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_POPULATION_AGE(Base):
    __tablename__ = "MAC_POPULATION_AGE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AGE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SAMPLINGFRACTION = Column(Numeric(10, 4))
    POPULATION = Column(Numeric(18, 4))
    MALE = Column(Numeric(18, 4))
    FEMALE = Column(Numeric(18, 4))
    RATIO = Column(Numeric(10, 4))
    MALERATIO = Column(Numeric(10, 4))
    FEMALERATIO = Column(Numeric(10, 4))
    SEXRATIO = Column(Numeric(10, 4))
