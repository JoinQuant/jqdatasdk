

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_IPO_EMPLOYEEINFO(Base):
    __tablename__ = "STK_EQ_IPO_EMPLOYEEINFO"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    SECURITYTYPEID = Column(String(12, u'utf8_bin'))
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    STATISTICALSCOPEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    STATISTICALSCOPE = Column(String(20, u'utf8_bin'))
    STATISTICALCOVERAGEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    STATISTICALCOVERAGE = Column(String(20, u'utf8_bin'))
    POSITIONTYPE = Column(String(100, u'utf8_bin'), primary_key=True, nullable=False)
    EMPLOYEENUMBER = Column(Integer)
    UPDATETIME_EN = Column(DateTime)
