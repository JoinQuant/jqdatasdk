

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_GUARANTEE_MAIN(Base):
    __tablename__ = "STK_GUARANTEE_MAIN"

    GUARANTEEID = Column(Numeric(20, 0))
    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    GUARANTEEINSTITUTIONID = Column(String(600, u'utf8_bin'))
    GUARANTEENAME = Column(String(1000, u'utf8_bin'))
    RELATETOGUARANTEE = Column(String(1000, u'utf8_bin'))
    RELATETOGUARANTEEID = Column(String(400, u'utf8_bin'))
    ISLISTINGCORPORATION = Column(String(4, u'utf8_bin'))
    CREDITORTYPEID = Column(String(200, u'utf8_bin'))
    CREDITORTYPE = Column(String(200, u'utf8_bin'))
    CREDITORID = Column(String(600, u'utf8_bin'))
    CREDITORNAME = Column(String(1000, u'utf8_bin'))
    CREDITORTOGUARANTEE = Column(String(1000, u'utf8_bin'))
    CREDITORTOGUARANTEEID = Column(String(400, u'utf8_bin'))
    RELATETOCREDITOR = Column(String(1000, u'utf8_bin'))
    RELATETOCREDITORID = Column(String(400, u'utf8_bin'))
    LOANWAY = Column(String(20, u'utf8_bin'))
    LOANWAYID = Column(String(20, u'utf8_bin'))
    LOANAMOUNT = Column(Numeric(20, 6))
    SIGNDATE = Column(DateTime)
    STARTDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
    GUARANTEETERM = Column(Numeric(10, 2))
    APPROVALSTATUS = Column(String(100, u'utf8_bin'))
    APPROVALSTATUSID = Column(String(100, u'utf8_bin'))
    APPROVALDATE = Column(DateTime)
    GUARANTEETYPE = Column(String(100, u'utf8_bin'))
    GUARANTEETYPEID = Column(String(100, u'utf8_bin'))
    GUARANTEEAMOUNT = Column(Numeric(20, 6))
    TERMDESCRIPTION = Column(String(400, u'utf8_bin'))
    PLEDGENAME = Column(String(1000, u'utf8_bin'))
    PLEDGEUSEFOR = Column(String(1000, u'utf8_bin'))
    BOOKVALUE = Column(Numeric(20, 6))
    MARKETVALUE = Column(Numeric(20, 6))
    PROPORTION = Column(Numeric(12, 4))
    GUARANTEENATURE = Column(String(200, u'utf8_bin'))
    GUARANTEENATUREID = Column(String(20, u'utf8_bin'))
    ISSTRAIGHTGUARANTEE = Column(String(20, u'utf8_bin'))
    SIGNSTATUS = Column(String(20, u'utf8_bin'))
    SIGNSTATUSID = Column(String(20, u'utf8_bin'))
    ISFULFIL = Column(String(20, u'utf8_bin'))
    ISIMPLEMENTATION = Column(String(20, u'utf8_bin'))
    ISIMPLEMENTATIONID = Column(String(20, u'utf8_bin'))
    ISILLEGAL = Column(String(2, u'utf8_bin'))
    ACCUMULATIVETOTAL = Column(Numeric(20, 6))
    TOTALTONETASSETS = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
    SOURCE = Column(String(12, u'utf8_bin'))
    RANK = Column(SmallInteger)
