

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_URBANFIXEDRESIDENT(Base):
    __tablename__ = "MAC_AREA_URBANFIXEDRESIDENT"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    RESIDENTINVEST = Column(Numeric(18, 4))
    RESIDENTCONSTRUCTAREA = Column(Numeric(18, 4))
    RESIDENTCOMPLETEAREA = Column(Numeric(18, 4))
    RESIDENTINVESTYOY = Column(Numeric(10, 4))
    RESIDENTCONSTRUCTAREAYOY = Column(Numeric(10, 4))
    RESIDENTCOMPLETEAREAYOY = Column(Numeric(10, 4))
