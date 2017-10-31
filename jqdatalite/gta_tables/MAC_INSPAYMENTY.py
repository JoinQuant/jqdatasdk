

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSPAYMENTY(Base):
    __tablename__ = "MAC_INSPAYMENTY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    TOTALCO = Column(Numeric(16, 4))
    PROPERTYCO = Column(Numeric(16, 4))
    ENTERPRISE = Column(Numeric(16, 4))
    FAMLIY = Column(Numeric(16, 4))
    MOTORVEHICLE = Column(Numeric(16, 4))
    PROJECT = Column(Numeric(16, 4))
    LIABILITY = Column(Numeric(16, 4))
    CREDIT = Column(Numeric(16, 4))
    GUARANTEE = Column(Numeric(16, 4))
    SHIP = Column(Numeric(16, 4))
    FREIGHT = Column(Numeric(16, 4))
    SPECIALRISKS = Column(Numeric(16, 4))
    FARM = Column(Numeric(16, 4))
    PROPERTYCOHEALTH = Column(Numeric(16, 4))
    PROPERTYCOACCIDENT = Column(Numeric(16, 4))
    OTHER = Column(Numeric(16, 4))
    PERSONALCO = Column(Numeric(16, 4))
    LIFE = Column(Numeric(16, 4))
    HEALTH = Column(Numeric(16, 4))
    ACCIDENT = Column(Numeric(16, 4))
