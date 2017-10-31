

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_FINALCONSUMY(Base):
    __tablename__ = "MAC_AREA_FINALCONSUMY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    FINALEXPENSE = Column(Numeric(18, 4))
    RESIDENTEXPENSE = Column(Numeric(18, 4))
    RURALEXPENSE = Column(Numeric(18, 4))
    URBANEXPENSE = Column(Numeric(18, 4))
    GOVERNMENTEXPENSE = Column(Numeric(18, 4))
    RESIDENTRATIO = Column(Numeric(10, 4))
    GOVERNMENTRATIO = Column(Numeric(10, 4))
    RURALRAIO = Column(Numeric(10, 4))
    URBANRATIO = Column(Numeric(10, 4))
