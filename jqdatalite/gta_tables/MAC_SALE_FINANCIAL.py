

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SALE_FINANCIAL(Base):
    __tablename__ = "MAC_SALE_FINANCIAL"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    AREACODE = Column(String(20, u'utf8_bin'))
    INDUSTRYID = Column(String(20, u'utf8_bin'))
    TOTALASSETS = Column(Numeric(18, 4))
    TOTALCURRENTASSETS = Column(Numeric(18, 4))
    TOTALFIXEDASSETS = Column(Numeric(18, 4))
    TOTALLIABILITIES = Column(Numeric(18, 4))
    TOTALOWNEREQUITY = Column(Numeric(18, 4))
    MAINSALEREVENUE = Column(Numeric(18, 4))
    MAINOPERATINGCOST = Column(Numeric(18, 4))
    MAINSALETAXADD = Column(Numeric(18, 4))
    MAINOPERATINGPROFIT = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
