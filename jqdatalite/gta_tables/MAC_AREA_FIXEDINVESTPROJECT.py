

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FIXEDINVESTPROJECT(Base):
    __tablename__ = "MAC_AREA_FIXEDINVESTPROJECT"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    CONSTRUCTPROJECTNUM = Column(Numeric(18, 4))
    STARTPROJECTNUM = Column(Numeric(18, 4))
    CONSTRUCTPROJECTNUMCHANGE = Column(Numeric(18, 4))
    STARTPROJECTNUMCHANGE = Column(Numeric(18, 4))
    CONSTRUCTPROJECTNUMADD = Column(Numeric(18, 4))
    STARTPROJECTNUMADD = Column(Numeric(18, 4))
