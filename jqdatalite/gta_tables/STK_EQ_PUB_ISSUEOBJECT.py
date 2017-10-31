

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_PUB_ISSUEOBJECT(Base):
    __tablename__ = "STK_EQ_PUB_ISSUEOBJECT"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    EVENTTYPEID = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    LISTEDDATE = Column(DateTime)
    ISSUEOBJECTNAME = Column(String(200, u'utf8_bin'))
    ISSUEOBJECTNAME_EN = Column(String(600, u'utf8_bin'))
    ISSUEOBJECTID = Column(String(40, u'utf8_bin'))
    OBJECTTYPEID = Column(String(12, u'utf8_bin'))
    STRATEGICINVESTORSSIGN = Column(String(2, u'utf8_bin'))
    ISSUEOBJECTCORPORATION = Column(String(400, u'utf8_bin'))
    ISSUEOBJECTCORPORATION_EN = Column(String(1000, u'utf8_bin'))
    ISSUEPRICE = Column(Numeric(10, 2))
    SUCCESSFULLYOFFERNUMBER = Column(Numeric(20, 0))
    SUBSCRIPTIONMODEID = Column(String(40, u'utf8_bin'))
    SUBSCRIPTIONMODE = Column(String(100, u'utf8_bin'))
    SUBSCRIPTIONRATIO = Column(Numeric(10, 3))
    RESTRAINNUMBER = Column(SmallInteger)
    RESTRAINPERIOD = Column(Integer)
    RESTRAINRATIO = Column(Numeric(10, 2))
    CIRCULATIONDATE = Column(DateTime)
    RELATIONSHIPID = Column(String(12, u'utf8_bin'))
    RELATIONSHIP = Column(String(400, u'utf8_bin'))
    LISTEDDATE2 = Column(DateTime)
    LISTEDSHARES = Column(Numeric(20, 2))
    UPDATEID = Column(BigInteger, primary_key=True)
    UPDATETIME_EN = Column(DateTime)
