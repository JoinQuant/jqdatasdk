

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_RURALFOODCONSUMY(Base):
    __tablename__ = "MAC_AREA_RURALFOODCONSUMY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    GRAIN = Column(Numeric(18, 4))
    VEGETABLE = Column(Numeric(18, 4))
    EDIBLEOIL = Column(Numeric(18, 4))
    PORKBEEFMUTTON = Column(Numeric(18, 4))
    POULTRY = Column(Numeric(18, 4))
    EGG = Column(Numeric(18, 4))
    AQUATIC = Column(Numeric(18, 4))
    SUGAR = Column(Numeric(18, 4))
    LIQUOR = Column(Numeric(18, 4))
