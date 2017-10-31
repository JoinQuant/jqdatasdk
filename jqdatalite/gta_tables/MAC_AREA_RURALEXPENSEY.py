

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_RURALEXPENSEY(Base):
    __tablename__ = "MAC_AREA_RURALEXPENSEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    EXPENSE = Column(Numeric(18, 4))
    FOOD = Column(Numeric(18, 4))
    CLOTHING = Column(Numeric(18, 4))
    RESIDENT = Column(Numeric(18, 4))
    HOUSEEQUIPMENT = Column(Numeric(18, 4))
    HEALTHCARE = Column(Numeric(18, 4))
    TRAFFICCOMMUNICATE = Column(Numeric(18, 4))
    EDUCATECULTURE = Column(Numeric(18, 4))
    OTHEREXPENSE = Column(Numeric(18, 4))
