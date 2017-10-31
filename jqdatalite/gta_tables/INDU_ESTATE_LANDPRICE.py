

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_ESTATE_LANDPRICE(Base):
    __tablename__ = "INDU_ESTATE_LANDPRICE"

    SGNQUARTER = Column(String(14), primary_key=True, nullable=False)
    LANDUSEPROPERTYID = Column(String(20), primary_key=True, nullable=False)
    AVERAGELEVEL = Column(Numeric(18, 4))
    AVERAGELEVELYOY = Column(Numeric(10, 4))
    AVERAGELEVELMOM = Column(Numeric(10, 4))
