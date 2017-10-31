

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_ESTATE_BOOMINDEX(Base):
    __tablename__ = "INDU_ESTATE_BOOMINDEX"

    SGNMONTH = Column(String(14), primary_key=True)
    TOTALBOOMIDX = Column(Numeric(10, 4))
    REALESTATEIDX = Column(Numeric(10, 4))
    CAPITALSOURCEIDX = Column(Numeric(10, 4))
    LANDDEVELOPAREAIDX = Column(Numeric(10, 4))
    COMMODITYHOUSEAREAIDX = Column(Numeric(10, 4))
    CONSTRUCTAREAIDX = Column(Numeric(10, 4))
    SALESIDX = Column(Numeric(10, 4))
