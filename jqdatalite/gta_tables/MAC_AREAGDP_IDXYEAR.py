

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREAGDP_IDXYEAR(Base):
    __tablename__ = "MAC_AREAGDP_IDXYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    GNI = Column(Numeric(10, 4))
    GDP = Column(Numeric(10, 4))
    GDP_PRIMARY = Column(Numeric(10, 4))
    GDP_SECONDARY = Column(Numeric(10, 4))
    GDP_INDUSTRY = Column(Numeric(10, 4))
    GDP_CONSTRUCTION = Column(Numeric(10, 4))
    GDP_TERTIARY = Column(Numeric(10, 4))
    GDP_TRANSPORT = Column(Numeric(10, 4))
    GDP_WHOLESALE = Column(Numeric(10, 4))
    GDP_HOTELS = Column(Numeric(10, 4))
    GDP_FINANCIAL = Column(Numeric(10, 4))
    GDP_REALESTATE = Column(Numeric(10, 4))
    GDP_OTHERS = Column(Numeric(10, 4))
    GDP_PERCAPITA = Column(Numeric(10, 4))
