

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_SEO_PUBLICINFO(Base):
    __tablename__ = "STK_EQ_SEO_PUBLICINFO"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    SECURITYTYPEID = Column(String(12, u'utf8_bin'))
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    SIGNDATE = Column(DateTime)
    ISSUEMODEID = Column(String(100, u'utf8_bin'))
    ISSUEMODE = Column(String(100, u'utf8_bin'))
    UNDERWRITEDMETHODSID = Column(String(12, u'utf8_bin'))
    UNDERWRITEDMETHODS = Column(String(12, u'utf8_bin'))
    ISEXRIGHT = Column(String(2, u'utf8_bin'))
    REGISTERDATE = Column(DateTime)
    EXRIGHTDATE = Column(DateTime)
    UNDERWRITEDSTARTDATE = Column(DateTime)
    UNDERWRITEDENDDATE = Column(DateTime)
    PUBLICATIONS1 = Column(String(200, u'utf8_bin'))
    PUBLICATIONS1_EN = Column(String(400, u'utf8_bin'))
    WEBSITE = Column(String(200, u'utf8_bin'))
    PUBLICATIONS2 = Column(String(200, u'utf8_bin'))
    PUBLICATIONS2_EN = Column(String(400, u'utf8_bin'))
    ISSUESTARTDATE = Column(DateTime)
    ISSUEENDDATE = Column(DateTime)
    ONLINESTARTDATE = Column(DateTime)
    ONLINEENDDATE = Column(DateTime)
    INQUIRYPRICESTARTDATE = Column(DateTime)
    INQUIRYPRICEENDDATE = Column(DateTime)
    PLACEMENTSTARTDATE = Column(DateTime)
    PLACEMENTENDDATE = Column(DateTime)
    ROADSHOWSTARTDATE = Column(DateTime)
    ROADSHOWENDDATE = Column(DateTime)
    OTHERISSUEDATE = Column(DateTime)
    LISTEDDATE = Column(DateTime)
    LISTEDDECLAREDATE = Column(DateTime)
    PRICE = Column(Numeric(10, 2))
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    ISSUESHARES = Column(Numeric(20, 0))
    ISSUESHARESPRIVATE = Column(Numeric(20, 0))
    ISSUESHARESPUBLIC = Column(Numeric(20, 0))
    PE1 = Column(Numeric(10, 4))
    PE2 = Column(Numeric(10, 4))
    PB = Column(Numeric(10, 4))
    EPS = Column(Numeric(10, 4))
    EQUITYPERSHAREBEFORE = Column(Numeric(10, 4))
    EQUITYPERSHAREAFTER = Column(Numeric(10, 4))
    EXPENSE = Column(Numeric(20, 2))
    EXPENSEPERSHARE = Column(Numeric(10, 4))
    RAISEFUND = Column(Numeric(20, 2))
    RAISENETFUND = Column(Numeric(20, 2))
    STAFFNUMBER = Column(Integer)
    UPDATEID = Column(BigInteger, primary_key=True)
    UPDATETIME_EN = Column(DateTime)
