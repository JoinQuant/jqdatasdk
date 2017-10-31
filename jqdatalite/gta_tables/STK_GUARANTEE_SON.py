

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_GUARANTEE_SON(Base):
    __tablename__ = "STK_GUARANTEE_SON"

    GUARANTEEID = Column(Numeric(20, 0))
    GUARANTORNAME = Column(String(1000, u'utf8_bin'))
    GUARANTORID = Column(String(600, u'utf8_bin'))
    GUARANTORTYPEID = Column(String(200, u'utf8_bin'))
    GUARANTORTYPE = Column(String(200, u'utf8_bin'))
    GUARANTORTOGUARANTEE = Column(String(1000, u'utf8_bin'))
    GUARANTORTOGUARANTEEID = Column(String(400, u'utf8_bin'))
    RELATETOGUARANTOR = Column(String(1000, u'utf8_bin'))
    RELATETOGUARANTORID = Column(String(400, u'utf8_bin'))
    GUARANTEETYPE = Column(String(100, u'utf8_bin'))
    GUARANTEETYPEID = Column(String(100, u'utf8_bin'))
    GUARANTEEAMOUNT = Column(Numeric(20, 6))
    GUARANTEEAMOUNTTOTOTAL = Column(Numeric(12, 4))
    BOOKVALUE = Column(Numeric(20, 6))
    MARKETVALUE = Column(Numeric(20, 6))
    UPDATEID = Column(BigInteger, primary_key=True)
    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    RANK = Column(SmallInteger)
