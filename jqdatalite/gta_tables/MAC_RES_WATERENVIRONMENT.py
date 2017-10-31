

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_WATERENVIRONMENT(Base):
    __tablename__ = "MAC_RES_WATERENVIRONMENT"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    TOTALAMOUNTOFWATERRESOURCES = Column(Numeric(18, 4))
    PERCAPITAWATERRESOURCES = Column(Numeric(18, 4))
    TOTALAMOUNTOFWATERSUPPLY = Column(Numeric(18, 4))
    TOTALAMOUNTOFWATERUSE = Column(Numeric(18, 4))
    AGRICULTURALUSE = Column(Numeric(18, 4))
    INDUSTRIALUSE = Column(Numeric(18, 4))
    DOMESTICUSE = Column(Numeric(18, 4))
    WASTEWATERDISCHARGED = Column(Numeric(18, 4))
    INDUSTRIALDISCHARGED = Column(Numeric(18, 4))
    LIVINGDISCHARGED = Column(Numeric(18, 4))
    AMOUNTUPTOTHESTANDARDS = Column(Numeric(18, 4))
    DISCHARGEAMOUNTOFCOD = Column(Numeric(18, 4))
    NH3ANDNDISCHARGED = Column(Numeric(18, 4))
