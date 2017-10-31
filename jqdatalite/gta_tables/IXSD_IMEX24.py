

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class IXSD_IMEX24(Base):
    __tablename__ = "IXSD_IMEX24"

    SGNMNTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    PTCD = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    PCTS = Column(String(100, u'utf8_bin'))
    ENTYP = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    IMEX2401 = Column(Numeric(18, 4))
    IMEX2402 = Column(Numeric(9, 4))
    IMEX2403 = Column(Numeric(18, 4))
    IMEX2404 = Column(Numeric(9, 4))
    IMEX2405 = Column(Numeric(18, 4))
    IMEX2406 = Column(Numeric(9, 4))
    IMEX2407 = Column(Numeric(18, 4))
    IMEX2408 = Column(Numeric(9, 4))
