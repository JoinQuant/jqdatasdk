

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_POPULATIONY(Base):
    __tablename__ = "MAC_POPULATIONY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    POPULATION = Column(Numeric(18, 4))
    MALE = Column(Numeric(18, 4))
    MALERATIO = Column(Numeric(10, 4))
    FEMALE = Column(Numeric(18, 4))
    FEMALERATIO = Column(Numeric(10, 4))
    URBANPOPULATION = Column(Numeric(18, 4))
    URBANRATIO = Column(Numeric(10, 4))
    RURALPOPULATION = Column(Numeric(18, 4))
    RURALRATIO = Column(Numeric(10, 4))
    BIRTHRATE = Column(Numeric(10, 4))
    DEATHRATE = Column(Numeric(10, 4))
    GROWTHRATE = Column(Numeric(10, 4))
