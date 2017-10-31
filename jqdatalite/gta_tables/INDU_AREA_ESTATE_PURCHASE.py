

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AREA_ESTATE_PURCHASE(Base):
    __tablename__ = "INDU_AREA_ESTATE_PURCHASE"

    SGNMONTH = Column(String(14), primary_key=True, nullable=False)
    AREACODE = Column(String(20), primary_key=True, nullable=False)
    LANDPURCHASE = Column(Numeric(18, 4))
    LANDPURCHASEAREA = Column(Numeric(18, 4))
    LANDCOMPLETEAREA = Column(Numeric(18, 4))
    LANDPENDINGAREA = Column(Numeric(18, 4))
    LANDTRANSACTION = Column(Numeric(18, 4))
    LANDPURCHASEYOY = Column(Numeric(10, 4))
    LANDPURCHASEAREAYOY = Column(Numeric(10, 4))
    LANDCOMPLETEAREAYOY = Column(Numeric(10, 4))
    LANDPENDINGAREAYOY = Column(Numeric(10, 4))
    LANDTRANSACTIONYOY = Column(Numeric(10, 4))
