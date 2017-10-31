

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSAREAM(Base):
    __tablename__ = "MAC_INSAREAM"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(2, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    INCOMES = Column(Numeric(22, 4))
    PROPERTY = Column(Numeric(22, 4))
    LIFE = Column(Numeric(22, 4))
    ACCIDENT = Column(Numeric(22, 4))
    HEALTH = Column(Numeric(22, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
