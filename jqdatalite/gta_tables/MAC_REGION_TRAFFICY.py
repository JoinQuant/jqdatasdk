

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_TRAFFICY(Base):
    __tablename__ = "MAC_REGION_TRAFFICY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    PASSENGER = Column(Numeric(20, 4))
    RAILWAYPASSENGER = Column(Numeric(20, 4))
    HIGHWAYPASSENGER = Column(Numeric(20, 4))
    FREIGHT = Column(Numeric(20, 4))
    RAILWAYFREIGHT = Column(Numeric(20, 4))
    HIGHWAYFREIGHT = Column(Numeric(20, 4))
