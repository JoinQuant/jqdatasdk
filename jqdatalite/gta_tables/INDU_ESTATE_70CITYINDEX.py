

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_ESTATE_70CITYINDEX(Base):
    __tablename__ = "INDU_ESTATE_70CITYINDEX"

    SGNMONTH = Column(String(14), primary_key=True, nullable=False)
    AREACODE = Column(String(20), primary_key=True, nullable=False)
    FIXEDBASEID = Column(String(20), primary_key=True, nullable=False)
    HOUSEIDX = Column(Numeric(10, 4))
    RESIDENTIDX = Column(Numeric(10, 4))
    COMMODITYHOUSEIDX = Column(Numeric(10, 4))
    SECONDHANDIDX = Column(Numeric(10, 4))
    RESIDENTBELOW90IDX = Column(Numeric(10, 4))
    COMMONRESIDENTBELOW90IDX = Column(Numeric(10, 4))
    COMMODITYBELOW90IDX = Column(Numeric(10, 4))
    COMMODITY144IDX = Column(Numeric(10, 4))
    COMMODITYABOVE144IDX = Column(Numeric(10, 4))
    SECONDHANDBELOW90IDX = Column(Numeric(10, 4))
    SECONDHAND144IDX = Column(Numeric(10, 4))
    SECONDHANDABOVE144IDX = Column(Numeric(10, 4))
