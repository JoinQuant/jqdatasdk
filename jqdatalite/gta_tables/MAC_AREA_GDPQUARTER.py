

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_GDPQUARTER(Base):
    __tablename__ = "MAC_AREA_GDPQUARTER"

    DECLAREDATE = Column(DateTime)
    SGNQUARTER = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    GDP = Column(Numeric(18, 4))
    GDP_PRIMARY = Column(Numeric(18, 4))
    GDP_SECONDARY = Column(Numeric(18, 4))
    GDP_TERTIARY = Column(Numeric(18, 4))
    GDPYOY = Column(Numeric(10, 4))
    GDP_PRIMARYYOY = Column(Numeric(10, 4))
    GDP_SECONDARYYOY = Column(Numeric(10, 4))
    GDP_TERTIARYYOY = Column(Numeric(10, 4))
    GDPMOM = Column(Numeric(10, 4))
