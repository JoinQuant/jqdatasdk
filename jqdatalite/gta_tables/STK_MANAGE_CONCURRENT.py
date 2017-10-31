

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_CONCURRENT(Base):
    __tablename__ = "STK_MANAGE_CONCURRENT"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20, u'utf8_bin'))
    ENDDATE = Column(DateTime)
    REPTTYPEID = Column(String(12, u'utf8_bin'))
    REPTTYPE = Column(String(100, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'))
    CONCURRENTINSTITUTIONNAME = Column(String(400, u'utf8_bin'))
    CONCURRENTINSTITUTIONNAME_EN = Column(String(800, u'utf8_bin'))
    CONCURRENTPOSITION = Column(String(200, u'utf8_bin'))
    CONCURRENTPOSITION_EN = Column(String(800, u'utf8_bin'))
    PAIDSIGN = Column(String(2, u'utf8_bin'))
    CONCURRENTPOSITIONTYPEID = Column(String(12, u'utf8_bin'))
    CONCURRENTPOSITIONTYPE = Column(String(100, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
    PERSONID = Column(Numeric(20, 0))
    UPDATETIME_EN = Column(DateTime)
