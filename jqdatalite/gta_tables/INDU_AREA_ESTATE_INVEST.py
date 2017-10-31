

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AREA_ESTATE_INVEST(Base):
    __tablename__ = "INDU_AREA_ESTATE_INVEST"

    SGNMONTH = Column(String(14), primary_key=True, nullable=False)
    AREACODE = Column(String(20), primary_key=True, nullable=False)
    INVEST = Column(Numeric(18, 4))
    RESIDENT = Column(Numeric(18, 4))
    AFFORDHOUSE = Column(Numeric(18, 4))
    INVESTYOY = Column(Numeric(10, 4))
    RESIDENTYOY = Column(Numeric(10, 4))
    AFFORDHOUSEYOY = Column(Numeric(10, 4))
