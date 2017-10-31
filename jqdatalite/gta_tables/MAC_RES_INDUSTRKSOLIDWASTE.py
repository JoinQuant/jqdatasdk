

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_INDUSTRKSOLIDWASTE(Base):
    __tablename__ = "MAC_RES_INDUSTRKSOLIDWASTE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    INDUSTRIALPRODUCED = Column(Numeric(18, 4))
    UTILIZED = Column(Numeric(18, 4))
    UTILIZATIONRATE = Column(Numeric(10, 4))
    DISCHARGED = Column(Numeric(18, 4))
    OUTPUTVALUEOFPRODUCTS = Column(Numeric(18, 4))
    TREATED = Column(Numeric(18, 4))
    STOCKS = Column(Numeric(18, 4))
    SLDWASTETYPEID = Column(String(20))
