

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AGR_MARKETPRICEIDXM(Base):
    __tablename__ = "INDU_AGR_MARKETPRICEIDXM"

    SGNMONTH = Column(String(14), primary_key=True, nullable=False)
    PRODID = Column(String(20), primary_key=True, nullable=False)
    PRICE = Column(Numeric(18, 4))
    PRICEYOY = Column(Numeric(10, 4))
    ACCUMPRICEYOY = Column(Numeric(10, 4))
    PRICEMOM = Column(Numeric(10, 4))
