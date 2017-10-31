

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_REGEVALWTQUALITY(Base):
    __tablename__ = "MAC_RES_REGEVALWTQUALITY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    WATERRESOURCESREGIONCODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    FLOODPERIOD = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    WATERRESOURCESREGIONNAME = Column(String(100, u'utf8_bin'))
    EVALUATIONOFRIVERLENGTH = Column(Numeric(18, 4))
    RATIOOF1RIVER = Column(Numeric(10, 4))
    RATIOOF2RIVER = Column(Numeric(10, 4))
    RATIOOF3RIVER = Column(Numeric(10, 4))
    RATIOOF4RIVER = Column(Numeric(10, 4))
    RATIOOF5RIVER = Column(Numeric(10, 4))
    RATIOOFINFERIOR5RIVER = Column(Numeric(10, 4))
    RATIOOF1TO3RIVER = Column(Numeric(10, 4))
