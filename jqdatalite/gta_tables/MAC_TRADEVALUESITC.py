

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_TRADEVALUESITC(Base):
    __tablename__ = "MAC_TRADEVALUESITC"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    SITCID = Column(BigInteger, primary_key=True, nullable=False)
    EXPORT = Column(Numeric(18, 4))
    IMPORT = Column(Numeric(18, 4))
    EXPORTYOY = Column(Numeric(10, 4))
    IMPORTYOY = Column(Numeric(10, 4))
