

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AGR_PRODUCTIDXQUARTER(Base):
    __tablename__ = "INDU_AGR_PRODUCTIDXQUARTER"

    SGNQUARTER = Column(String(14), primary_key=True, nullable=False)
    AREACODE = Column(String(20), primary_key=True, nullable=False)
    PRODID = Column(String(20), primary_key=True, nullable=False)
    DATASIGN = Column(String(8), primary_key=True, nullable=False)
    PRICEIDX = Column(Numeric(10, 4))
