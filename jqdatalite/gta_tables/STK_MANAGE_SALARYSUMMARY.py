

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_SALARYSUMMARY(Base):
    __tablename__ = "STK_MANAGE_SALARYSUMMARY"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20, u'utf8_bin'))
    ENDDATE = Column(DateTime)
    DISCLOSETYPEID = Column(String(12, u'utf8_bin'))
    DISCLOSETYPE = Column(String(100, u'utf8_bin'))
    SUMSALARY = Column(Numeric(20, 2))
    SUMALLOWANCE = Column(Numeric(20, 2))
    TOP3SUMSALARY = Column(Numeric(20, 2))
    TOP3DIRECTORSUMSALARY = Column(Numeric(20, 2))
    TOP3DIRECTORPAIDNUMBER = Column(BigInteger)
    TOP3MANAGESUMSALARY = Column(Numeric(20, 2))
    TOP3MANAGEPAIDNUMBER = Column(BigInteger)
    UNPAIDNUMBER = Column(BigInteger)
    DIRECTORUNPAIDNUMBER = Column(BigInteger)
    SUPERVISORUNPAIDNUMBER = Column(BigInteger)
    MANAGESUMSALARY = Column(Numeric(20, 2))
    DIRECTORSUMSALARY = Column(Numeric(20, 2))
    SUPERVISORSUMSALARY = Column(Numeric(20, 2))
    UPDATEID = Column(BigInteger, primary_key=True)
