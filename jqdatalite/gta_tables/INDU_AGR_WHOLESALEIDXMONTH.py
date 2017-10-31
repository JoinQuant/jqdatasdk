

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AGR_WHOLESALEIDXMONTH(Base):
    __tablename__ = "INDU_AGR_WHOLESALEIDXMONTH"

    SGNMONTH = Column(String(14), primary_key=True)
    AGRFIXEDBASEIDX = Column(Numeric(10, 4))
    AGRYOYIDX = Column(Numeric(10, 4))
    AGRMOMIDX = Column(Numeric(10, 4))
    FOODBASKETFIXEDBASEIDX = Column(Numeric(10, 4))
    FOODBASKETYOYIDX = Column(Numeric(10, 4))
    FOODBASKETMOMIDX = Column(Numeric(10, 4))
