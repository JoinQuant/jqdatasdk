

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_SALARY(Base):
    __tablename__ = "STK_MANAGE_SALARY"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    REPTTYPEID = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    REPTTYPE = Column(String(100, u'utf8_bin'))
    PERSONID = Column(Numeric(20, 0))
    FULLNAME = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    ISRELATEDPARTIESPAID = Column(String(2, u'utf8_bin'))
    PAIDSIGN = Column(String(2, u'utf8_bin'))
    TOTALSALARY = Column(Numeric(20, 2))
    ALLOWANCE = Column(Numeric(20, 2))
    YEARBEGINNINGHOLDSHARES = Column(Numeric(20, 2))
    HOLDSHARES = Column(Numeric(20, 2))
    CHANGEREASON = Column(String(400, u'utf8_bin'))
    SHAREHOLDINGSTYLE = Column(String(40, u'utf8_bin'))
    STOCKOPTIONSNUMBER = Column(Numeric(20, 2))
    CONDITIONALSHARESNUMBER = Column(Numeric(20, 2))
    ISCONCURRENTPOSITION = Column(String(2, u'utf8_bin'))
