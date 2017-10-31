

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_SEAAREAANDFISHING(Base):
    __tablename__ = "MAC_RES_SEAAREAANDFISHING"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    SEACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SEANAME = Column(String(100, u'utf8_bin'))
    SEAAREA = Column(Numeric(18, 4))
    FISHINGOFCONTINENTALSHELF = Column(Numeric(18, 4))
    AVERAGEDEPTH = Column(Numeric(18, 4))
    MAXIMUMDEPTH = Column(Numeric(18, 4))
