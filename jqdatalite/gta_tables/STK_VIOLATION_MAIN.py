

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_VIOLATION_MAIN(Base):
    __tablename__ = "STK_VIOLATION_MAIN"

    VIOLATIONID = Column(Numeric(20, 0))
    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    DISPOSALDATE = Column(DateTime)
    DECLAREDATE = Column(DateTime)
    PROMULGATOR = Column(String(100, u'utf8_bin'))
    DOCUMENTNUMBER = Column(String(100, u'utf8_bin'))
    SUPERVISOR = Column(String(100, u'utf8_bin'))
    VIOLATIONTYPE = Column(String(200, u'utf8_bin'))
    VIOLATIONTYPEID = Column(String(200, u'utf8_bin'))
    VIOLATIONYEAR = Column(String(200, u'utf8_bin'))
    SUMPENALTY = Column(Numeric(20, 2))
    ISVIOLATED = Column(String(2, u'utf8_bin'))
    PUNISHMENTTYPE = Column(String(200, u'utf8_bin'))
    PUNISHMENTTYPEID = Column(String(100, u'utf8_bin'))
    PENALTY = Column(Numeric(20, 2))
    UPDATEID = Column(BigInteger, primary_key=True, server_default=text("'0'"))
