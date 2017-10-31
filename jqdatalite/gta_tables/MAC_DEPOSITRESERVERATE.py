

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_DEPOSITRESERVERATE(Base):
    __tablename__ = "MAC_DEPOSITRESERVERATE"

    DECLAREDATE = Column(DateTime)
    CHANGEDATE = Column(DateTime, primary_key=True)
    LARGEFINANCIAL = Column(Numeric(10, 4))
    LARGEFINANCIALCHANGE = Column(Numeric(10, 4))
    SMALLFINANCIAL = Column(Numeric(10, 4))
    SMALLFINANCIALCHANGE = Column(Numeric(10, 4))
