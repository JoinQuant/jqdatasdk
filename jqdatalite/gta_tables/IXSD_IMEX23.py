

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class IXSD_IMEX23(Base):
    __tablename__ = "IXSD_IMEX23"

    SGNMNTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    PTCD = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    PCTS = Column(String(100, u'utf8_bin'))
    TTYP = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    IMEX2301 = Column(Numeric(18, 4))
    IMEX2302 = Column(Numeric(18, 4))
    IMEX2303 = Column(Numeric(18, 4))
    IMEX2304 = Column(Numeric(18, 4))
    IMEX2305 = Column(Numeric(18, 4))
    IMEX2306 = Column(Numeric(18, 4))
    IMEX2307 = Column(Numeric(18, 4))
    IMEX2308 = Column(Numeric(18, 4))
