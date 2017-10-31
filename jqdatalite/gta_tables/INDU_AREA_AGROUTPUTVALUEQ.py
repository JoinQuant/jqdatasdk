

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AREA_AGROUTPUTVALUEQ(Base):
    __tablename__ = "INDU_AREA_AGROUTPUTVALUEQ"

    SGNQUARTER = Column(String(14), primary_key=True, nullable=False)
    AREACODE = Column(String(20), primary_key=True, nullable=False)
    OUTPUTVALUE = Column(Numeric(18, 4))
    FARMING = Column(Numeric(18, 4))
    FORESTRY = Column(Numeric(18, 4))
    ANIMALHUSBANDRY = Column(Numeric(18, 4))
    FISHERY = Column(Numeric(18, 4))
    OUTPUTVALUEYOY = Column(Numeric(10, 4))
    FARMINGYOY = Column(Numeric(10, 4))
    FORESTRYYOY = Column(Numeric(10, 4))
    ANIMALHUSBANDRYYOY = Column(Numeric(10, 4))
    FISHERYYOY = Column(Numeric(10, 4))
