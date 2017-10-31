

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_SEO_PLAN(Base):
    __tablename__ = "STK_EQ_SEO_PLAN"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    SECURITYTYPEID = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    SECURITYTYPE = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    NEWISSUETYPEID = Column(String(12, u'utf8_bin'))
    NEWISSUETYPE = Column(String(40, u'utf8_bin'))
    PARVALUE = Column(Numeric(10, 2))
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    ISSUESIZE = Column(Numeric(20, 0))
    ISSUESHARESPRIVATE = Column(Numeric(20, 0))
    ISSUESHARESPUBLIC = Column(Numeric(20, 0))
    OBJECT = Column(String(1000, u'utf8_bin'))
    PRICEMODEID = Column(String(40, u'utf8_bin'))
    PRICEMODE = Column(String(40, u'utf8_bin'))
    RAISEFUND = Column(Numeric(20, 2))
    RAISENETFUND = Column(Numeric(20, 2))
    PRICECEILING = Column(Numeric(10, 2))
    PRICEFLOOR = Column(Numeric(10, 2))
    REFORMATIONSIGN = Column(String(2, u'utf8_bin'))
    PASSDATE = Column(DateTime)
    PROJECTACTUALIZEID = Column(String(20, u'utf8_bin'))
    PROJECTACTUALIZE = Column(String(20, u'utf8_bin'))
    UPDATESTATE = Column(SmallInteger, primary_key=True, nullable=False)
