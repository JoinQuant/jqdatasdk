

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FIXEDINVESTPLAN(Base):
    __tablename__ = "MAC_AREA_FIXEDINVESTPLAN"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    CONSTRUCTPROJECT = Column(Numeric(18, 4))
    STARTPROJECT = Column(Numeric(18, 4))
    STARTPROJECTTOCONSTRUCT = Column(Numeric(10, 4))
    CONSTRUCTPROJECTYOY = Column(Numeric(10, 4))
    STARTPROJECTYOY = Column(Numeric(10, 4))
    STARTPROJECTTOCONSTRUCTYOY = Column(Numeric(10, 4))
