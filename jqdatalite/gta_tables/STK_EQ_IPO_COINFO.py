

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_IPO_COINFO(Base):
    __tablename__ = "STK_EQ_IPO_COINFO"

    INSTITUTIONID = Column(Numeric(20, 0))
    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12))
    SECURITYTYPEID = Column(String(12))
    CROSSSYMBOL = Column(String(12))
    SHORTNAME = Column(String(16))
    INDUSTRYID = Column(String(8))
    INDUSTRYOLDNAME = Column(String(100))
    INDUSTRYCODE = Column(String(10))
    INDUSTRYNAME = Column(String(100))
    EXCHANGECODE = Column(String(20))
    FULLNAME = Column(String(160))
    ENNAME = Column(String(300))
    ESTABLISHDATE = Column(DateTime)
    IPODATE = Column(DateTime)
    LISTEDDATE = Column(DateTime, primary_key=True, nullable=False)
    REGISTERADDRESS = Column(String(120))
    REGISTERCITY = Column(String(100))
    LEGALREPRESENTATIVE = Column(String(16))
    RETIREDNUMBER = Column(Integer)
    DIRECTORNUMBER = Column(Integer)
    SUPERVISORNUMBER = Column(Integer)
    INDCLASSIFYSYSTEMCODE = Column(String(40))
