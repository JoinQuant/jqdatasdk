

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_OCEANECONOADDVALUE(Base):
    __tablename__ = "MAC_RES_OCEANECONOADDVALUE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    TOTALOCEANPRODUCT = Column(Numeric(18, 4))
    MARINEINDUSTRIES = Column(Numeric(18, 4))
    MARINEFISHERY = Column(Numeric(18, 4))
    MARINEOILANDGAS = Column(Numeric(18, 4))
    OCEANMINING = Column(Numeric(18, 4))
    SEASALT = Column(Numeric(18, 4))
    MARINESHIPPING = Column(Numeric(18, 4))
    MARINECHEMICAL = Column(Numeric(18, 4))
    BIOLOGICALMEDICINE = Column(Numeric(18, 4))
    ENGINEERINGCONSTRUCTION = Column(Numeric(18, 4))
    ELECTRICPOWER = Column(Numeric(18, 4))
    UTILIZATIONOFSEAWATER = Column(Numeric(18, 4))
    OCEANTRANSPORTATION = Column(Numeric(18, 4))
    COASTALTOURISM = Column(Numeric(18, 4))
    SEARELATEDEMPLOYMENT = Column(Numeric(18, 4))
