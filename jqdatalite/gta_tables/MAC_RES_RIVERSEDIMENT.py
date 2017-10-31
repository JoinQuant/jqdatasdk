

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_RIVERSEDIMENT(Base):
    __tablename__ = "MAC_RES_RIVERSEDIMENT"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    RIVERCODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    HYDROLOGICALSTATIONCODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    RIVERNAME = Column(String(100, u'utf8_bin'))
    HYDROLOGICALSTATIONNAME = Column(String(100, u'utf8_bin'))
    CATCHMENTAREA = Column(Numeric(18, 4))
    ANNUALFLOW = Column(Numeric(18, 4))
    ANNUALSEDIMENTDISCHARGE = Column(Numeric(18, 4))
    ANNUALAVERAGESEDICONCENT = Column(Numeric(18, 4))
    AVERAGEMEDIANDIAMETER = Column(Numeric(18, 4))
    SEDIMENTTRANSPORTMODULUS = Column(Numeric(18, 4))
