

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_STOCKINFO(Base):
    __tablename__ = "STK_STOCKINFO"
    SYMBOL = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0))
    SHORTNAME = Column(String(100, u'utf8_bin'))
    PYSHORTNAME = Column(String(100, u'utf8_bin'))
    ENSHORTNAME = Column(String(400, u'utf8_bin'))
    ENNAME = Column(String(200, u'utf8_bin'))
    LISTEDDATE = Column(DateTime, primary_key=True, nullable=False)
    DELISTEDDATE = Column(DateTime)
    IPOSHARES = Column(Numeric(20, 0))
    PARVALUE = Column(Numeric(20, 10))
    ISSUEPRICE = Column(Numeric(10, 4))
    CURRENCYCODE = Column(String(40, u'utf8_bin'))
    EXCHANGECODE = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    BOARDID = Column(String(40, u'utf8_bin'))
    SHARETYPE = Column(String(2, u'utf8_bin'))
    ISIN = Column(String(40, u'utf8_bin'))
    STATUSID = Column(String(40, u'utf8_bin'))
    FORMERNAME = Column(String(1000, u'utf8_bin'))
    CURRENCY = Column(String(40, u'utf8_bin'))
