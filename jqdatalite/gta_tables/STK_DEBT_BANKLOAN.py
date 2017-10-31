

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_DEBT_BANKLOAN(Base):
    __tablename__ = "STK_DEBT_BANKLOAN"

    EVENTID = Column(String(40, u'utf8_bin'))
    SYMBOL = Column(String(20, u'utf8_bin'))
    INSTITUTIONID = Column(Numeric(20, 0))
    INSTITUTIONTYPE = Column(String(4, u'utf8_bin'))
    INSTITUTIONNAME = Column(String(800, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    SIGNDATE = Column(DateTime)
    LOANBANK = Column(String(600, u'utf8_bin'))
    LOANBANK_EN = Column(String(1800, u'utf8_bin'))
    ISSIGN = Column(String(4, u'utf8_bin'))
    CURRENCYCODE = Column(String(6, u'utf8_bin'))
    CURRENCY = Column(String(40, u'utf8_bin'))
    LOANAMOUNT = Column(Numeric(20, 2))
    AMOUNTRANGE = Column(String(100, u'utf8_bin'))
    LOANTERM = Column(Numeric(10, 5))
    STARTDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
    INTERSETRATE = Column(Numeric(20, 6))
    FLOATINGRATE = Column(String(400, u'utf8_bin'))
    LOANTYPE = Column(String(40, u'utf8_bin'))
    INDEPENDENTGUARANTOR = Column(String(400, u'utf8_bin'))
    INDEPENDENTGUARANTOR_EN = Column(String(800, u'utf8_bin'))
    RELATEDGUARANTOR = Column(String(400, u'utf8_bin'))
    RELATEDGUARANTOR_EN = Column(String(800, u'utf8_bin'))
    ISGUARANTEE = Column(String(4, u'utf8_bin'))
    PLEDGE = Column(String(400, u'utf8_bin'))
    PLEDGETERM = Column(Numeric(10, 5))
    INVESTPROJECT = Column(String(400, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
    UPDATETIME_EN = Column(DateTime)
