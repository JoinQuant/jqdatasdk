

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AREA_AGROUTPUTVALUEY(Base):
    __tablename__ = "INDU_AREA_AGROUTPUTVALUEY"

    SGNYEAR = Column(String(8), primary_key=True, nullable=False)
    AREACODE = Column(String(20), primary_key=True, nullable=False)
    OUTPUTVALUE = Column(Numeric(18, 4))
    FARMING = Column(Numeric(18, 4))
    FORESTRY = Column(Numeric(18, 4))
    ANIMALHUSBANDRY = Column(Numeric(18, 4))
    FISHERY = Column(Numeric(18, 4))
    OUTPUTVALUEIDX = Column(Numeric(10, 4))
    FARMINGIDX = Column(Numeric(10, 4))
    FORESTRYIDX = Column(Numeric(10, 4))
    ANIMALHUSBANDRYIDX = Column(Numeric(10, 4))
    FISHERYIDX = Column(Numeric(10, 4))
