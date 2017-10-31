

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AGR_VEGETABLEIDXDAY(Base):
    __tablename__ = "INDU_AGR_VEGETABLEIDXDAY"

    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    VEGETABLEID = Column(String(20), primary_key=True, nullable=False)
    PRICEIDX = Column(Numeric(10, 4))
    PRICECHANGE = Column(Numeric(10, 4))
    CHANGERATIO = Column(Numeric(10, 4))
