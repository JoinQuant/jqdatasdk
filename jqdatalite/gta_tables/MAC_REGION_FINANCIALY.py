

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_FINANCIALY(Base):
    __tablename__ = "MAC_REGION_FINANCIALY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    ENTERPRISENUM = Column(Numeric(20, 4))
    TOTALINDUSTRY = Column(Numeric(20, 4))
    EMPLOYNUM = Column(Numeric(20, 4))
    SALEREVENUE = Column(Numeric(20, 4))
    PROFITTAX = Column(Numeric(20, 4))
    SALETAXADD = Column(Numeric(20, 4))
    VALUEADDTAX = Column(Numeric(20, 4))
    TOTALPROFIT = Column(Numeric(20, 4))
    TOTALCURRENTASSETS = Column(Numeric(20, 4))
    FIXEDASSET = Column(Numeric(20, 4))
    AVGCURRENTASSETS = Column(Numeric(20, 4))
    AVGFIXEDASSET = Column(Numeric(20, 4))
