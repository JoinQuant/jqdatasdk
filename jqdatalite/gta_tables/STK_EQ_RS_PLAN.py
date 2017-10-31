

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_RS_PLAN(Base):
    __tablename__ = "STK_EQ_RS_PLAN"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    SECURITYTYPEID = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    SHAREHOLDERSDECISION = Column(String(600, u'utf8_bin'))
    DIRECTORATEALLOTMENTRATIO = Column(Numeric(10, 4))
    SHAREHOLDERSALLOTMENTRATIO = Column(Numeric(10, 4))
    PARVALUE = Column(Numeric(10, 4))
    REFERENCESHARES = Column(Numeric(20, 0))
    REFERENCEDATE = Column(DateTime)
    PRICEMODEID = Column(String(40, u'utf8_bin'))
    PRICEMODE = Column(String(40, u'utf8_bin'))
    ALLOTMENTSHARES = Column(Numeric(20, 0))
    RAISENETFUND = Column(Numeric(20, 2))
    RAISEFUND = Column(Numeric(20, 2))
    PRICECEILING = Column(Numeric(10, 2))
    PRICEFLOOR = Column(Numeric(10, 2))
    DESCRIPTION = Column(String(600, u'utf8_bin'))
    PASSDATE = Column(DateTime)
    PROJECTACTUALIZEID = Column(String(20, u'utf8_bin'))
    PROJECTACTUALIZE = Column(String(20, u'utf8_bin'))
    DECLAREDATE2 = Column(DateTime)
    UPDATESTATE = Column(SmallInteger, primary_key=True, nullable=False)
