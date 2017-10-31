

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FIXEDBUILDVALUEY(Base):
    __tablename__ = "MAC_AREA_FIXEDBUILDVALUEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    CONSTRUCTAREA = Column(Numeric(18, 4))
    RESIDENTCONSTRUCTAREA = Column(Numeric(18, 4))
    COMMODITYCONSTRUCTAREA = Column(Numeric(18, 4))
    COMPLETEAREA = Column(Numeric(18, 4))
    RESIDENTCOMPLETEAREA = Column(Numeric(18, 4))
    COMMODITYCOMPLETEAREA = Column(Numeric(18, 4))
    COMPLETEVALUE = Column(Numeric(18, 4))
    RESIDENTCOMPLETEVALUE = Column(Numeric(18, 4))
    COMMODITYCOMPLETEVALUE = Column(Numeric(18, 4))
