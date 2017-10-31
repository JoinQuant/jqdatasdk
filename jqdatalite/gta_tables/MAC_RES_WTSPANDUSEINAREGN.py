

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_WTSPANDUSEINAREGN(Base):
    __tablename__ = "MAC_RES_WTSPANDUSEINAREGN"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    WATERRESOURCESREGIONCODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    WATERRESOURCESREGIONNAME = Column(String(100, u'utf8_bin'))
    WATERSUPPLY = Column(Numeric(18, 4))
    SURFACEWATER = Column(Numeric(18, 4))
    GROUNDWATER = Column(Numeric(18, 4))
    OTHERS = Column(Numeric(18, 4))
    WATERUSE = Column(Numeric(18, 4))
    AGRICULTURE = Column(Numeric(18, 4))
    INDUSTRY = Column(Numeric(18, 4))
    CONSUMPTION = Column(Numeric(18, 4))
    ECOLOGICALPROTECTION = Column(Numeric(18, 4))
    PERCAPITAWATERUSE = Column(Numeric(18, 4))
