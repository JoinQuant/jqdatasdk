

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCALTAXY(Base):
    __tablename__ = "MAC_FISCALTAXY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    TAX = Column(Numeric(18, 4))
    ADDVALUETAX = Column(Numeric(18, 4))
    CONSUMPTETAX = Column(Numeric(18, 4))
    BUSINESSTAX = Column(Numeric(18, 4))
    CORPORATETAX = Column(Numeric(18, 4))
    INDIVIDUALTAX = Column(Numeric(18, 4))
    TARIFF = Column(Numeric(18, 4))
