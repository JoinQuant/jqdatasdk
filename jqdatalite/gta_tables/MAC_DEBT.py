

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_DEBT(Base):
    __tablename__ = "MAC_DEBT"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    DEBTINFLOW = Column(Numeric(18, 2))
    INFLOWYOY = Column(Numeric(8, 2))
    DEBTOUTFLOW = Column(Numeric(18, 2))
    OUTFLOWYOY = Column(Numeric(8, 2))
    DEBTNETINFLOW = Column(Numeric(18, 2))
    GDP = Column(Numeric(18, 2))
    GDPYOY = Column(Numeric(8, 2))
    DEBTOUTFLOWTOGDP = Column(Numeric(18, 4))
    FEINCOME = Column(Numeric(18, 2))
    FEINCOMEYOY = Column(Numeric(8, 2))
    DEBT = Column(Numeric(18, 2))
    DEBTYOY = Column(Numeric(8, 2))
    LONGDEBT = Column(Numeric(18, 2))
    LONGDEBTYOY = Column(Numeric(8, 2))
    LONGDEBTTOTOTAL = Column(Numeric(8, 2))
    SHORTDEBT = Column(Numeric(18, 2))
    SHORTDEBTYOY = Column(Numeric(8, 2))
    SHORTDEBTTOTOTAL = Column(Numeric(8, 2))
    SHORTDEBTTORESERVE = Column(Numeric(8, 2))
    DEBTSERVICERATIO = Column(Numeric(8, 4))
    LIABILITYRATIO = Column(Numeric(8, 4))
    DEBTRATIO = Column(Numeric(8, 4))
