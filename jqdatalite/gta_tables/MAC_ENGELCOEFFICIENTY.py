

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_ENGELCOEFFICIENTY(Base):
    __tablename__ = "MAC_ENGELCOEFFICIENTY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    NETINCOME = Column(Numeric(18, 4))
    DPI = Column(Numeric(18, 4))
    NETINCOMEIDX = Column(Numeric(10, 4))
    DPIIDX = Column(Numeric(10, 4))
    RURALENGELCOEFFICIENT = Column(Numeric(10, 4))
    URBANENGELCOEFFICIENT = Column(Numeric(10, 4))
