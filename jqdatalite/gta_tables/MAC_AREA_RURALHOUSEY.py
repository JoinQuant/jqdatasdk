

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_RURALHOUSEY(Base):
    __tablename__ = "MAC_AREA_RURALHOUSEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    HOUSEAREA = Column(Numeric(18, 4))
    HOUSEVALUE = Column(Numeric(18, 4))
    REINFORCEDCONCRETESTRUCTURE = Column(Numeric(18, 4))
    BRICKWOODSTRUCTURE = Column(Numeric(18, 4))
