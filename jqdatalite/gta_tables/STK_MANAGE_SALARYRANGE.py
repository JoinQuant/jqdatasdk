

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_SALARYRANGE(Base):
    __tablename__ = "STK_MANAGE_SALARYRANGE"

    INSTITUTIONID = Column(Numeric(20, 0))
    ENDDATE = Column(DateTime)
    SALARYRANGETYPEID = Column(String(12, u'utf8_bin'))
    SALARYRANGELEVEL = Column(Integer)
    SYMBOL = Column(String(20, u'utf8_bin'))
    SALARYRANGETYPE = Column(String(100, u'utf8_bin'))
    RANGEFLOOR = Column(Numeric(20, 2))
    RANGECEILING = Column(Numeric(20, 2))
    RANGENUMBER = Column(BigInteger)
    UPDATEID = Column(BigInteger, primary_key=True)
