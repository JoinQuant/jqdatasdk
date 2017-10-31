

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_ELECTRICITY_IDX(Base):
    __tablename__ = "INDU_ELECTRICITY_IDX"

    SGNMONTH = Column(String(14), primary_key=True, nullable=False)
    DATASIGN = Column(String(4), primary_key=True, nullable=False)
    ELECTRICITYID = Column(String(20), primary_key=True, nullable=False)
    UNITNAME = Column(String(100))
    TOTALVALUE = Column(Numeric(20, 4))
    VALUEYOY = Column(Numeric(10, 4))
