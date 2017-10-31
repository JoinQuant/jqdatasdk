

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_URBANINCOMEQ(Base):
    __tablename__ = "MAC_AREA_URBANINCOMEQ"

    SGNQUARTER = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    HOUSENUM = Column(Numeric(18, 4))
    AVGPEOPLE = Column(Numeric(18, 4))
    AVGEMPLOYE = Column(Numeric(18, 4))
    AVGINCOME = Column(Numeric(18, 4))
    AVGDPI = Column(Numeric(18, 4))
