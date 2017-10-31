

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_CONSUMEY(Base):
    __tablename__ = "MAC_AREA_CONSUMEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    RESIDENT = Column(Numeric(18, 4))
    RURAL = Column(Numeric(18, 4))
    URBAN = Column(Numeric(18, 4))
    CONSUMERATIO = Column(Numeric(10, 4))
    HOUSEHOLDYOY = Column(Numeric(10, 4))
    RURALYOY = Column(Numeric(10, 4))
    URBANYOY = Column(Numeric(10, 4))
    HOUSEHOLDFIXEDBASEIDX = Column(Numeric(10, 4))
    RURALFIXEDBASEIDX = Column(Numeric(10, 4))
    URBANFIXEDBASEIDX = Column(Numeric(10, 4))
