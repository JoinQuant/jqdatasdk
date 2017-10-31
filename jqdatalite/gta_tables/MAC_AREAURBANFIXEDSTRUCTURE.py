

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREAURBANFIXEDSTRUCTURE(Base):
    __tablename__ = "MAC_AREAURBANFIXEDSTRUCTURE"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    STRUCTUREFUND = Column(Numeric(18, 4))
    CONSTRUCTINSTALL = Column(Numeric(18, 4))
    EQUIPMENTPURCHASE = Column(Numeric(18, 4))
    OTHEREXPENSE = Column(Numeric(18, 4))
    COMPOSITFUNDYOY = Column(Numeric(10, 4))
    CONSTRUCTINSTALLYOY = Column(Numeric(10, 4))
    EQUIPMENTPURCHASEYOY = Column(Numeric(10, 4))
    OTHEREXPENSEYOY = Column(Numeric(10, 4))
