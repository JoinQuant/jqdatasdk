

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_ITEMCHANGE(Base):
    __tablename__ = "STK_ITEMCHANGE"

    INSTITUTIONID = Column(Numeric(20, 0))
    SECURITYID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    DECLAREDATE = Column(DateTime)
    CHANGEDATE = Column(DateTime, primary_key=True, nullable=False)
    CHANGEDITEM = Column(String(100, u'utf8_bin'), primary_key=True, nullable=False)
    VALUEBEFORE = Column(String(1000, u'utf8_bin'))
    CODEBEFORE = Column(String(200, u'utf8_bin'))
    VALUEAFTER = Column(String(1000, u'utf8_bin'))
    CODEAFTER = Column(String(200, u'utf8_bin'))
    REASON = Column(String(200, u'utf8_bin'))
    REASONID = Column(String(100, u'utf8_bin'))
    STATEIDCHANGE = Column(String(100, u'utf8_bin'))
