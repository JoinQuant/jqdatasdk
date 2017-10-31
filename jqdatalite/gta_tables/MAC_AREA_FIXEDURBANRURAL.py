

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FIXEDURBANRURAL(Base):
    __tablename__ = "MAC_AREA_FIXEDURBANRURAL"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    FIXEDASSETSINVEST = Column(Numeric(18, 4))
    URBAN = Column(Numeric(18, 4))
    REALESTATE = Column(Numeric(18, 4))
    RURAL = Column(Numeric(18, 4))
    FARMHOUSEHOLD = Column(Numeric(18, 4))
    NONFARMHOUSEHOLD = Column(Numeric(18, 4))
