

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHARES_STRUCTURE(Base):
    __tablename__ = "STK_SHARES_STRUCTURE"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    CHANGEDATE = Column(DateTime, primary_key=True, nullable=False)
    CHANGEREASON = Column(String(400, u'utf8_bin'))
    CHANGEREASONID = Column(String(400, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    STATEOWNEDSHARES = Column(Numeric(20, 0))
    STATESHARES = Column(Numeric(20, 0))
    SLS = Column(Numeric(20, 0))
    OTHERDOMESTICSHARES = Column(Numeric(20, 0))
    SOCIALLEGALPERSONSHARES = Column(Numeric(20, 0))
    NATURALPERSONSHARES = Column(Numeric(20, 0))
    PROMOTERSHARES = Column(Numeric(20, 0))
    EMPLOYEESHARES = Column(Numeric(20, 0))
    EXECUTIVESSHARES = Column(Numeric(20, 0))
    FOREIGNSHARES = Column(Numeric(20, 0))
    FOREIGNLEGALPERSONSHARES = Column(Numeric(20, 0))
    FOREIGNERSHARES = Column(Numeric(20, 0))
    ALLOCATIONSHARES = Column(Numeric(20, 0))
    STRATEGICINVESTORSHARES = Column(Numeric(20, 0))
    FUNDALLOCATIONSHARES = Column(Numeric(20, 0))
    OTHERALLOCATIONSHARES = Column(Numeric(20, 0))
    TRANSFERREDALOTTEDSHARES = Column(Numeric(20, 0))
    PREFERREDSHARE = Column(Numeric(20, 0))
    OTHERNEGOTIABLESHARES = Column(Numeric(20, 0))
    NONTRADABLESHARE = Column(Numeric(20, 0))
    OTHERLOCKSHARES = Column(Numeric(20, 0))
    LOCKSHARESTOTAL = Column(Numeric(20, 0))
    TRADABLESHARESA = Column(Numeric(20, 0))
    TRADABLEEXECUTIVESSHARES = Column(Numeric(20, 0))
    TRADABLESHARESB = Column(Numeric(20, 0))
    TRADABLESHARESH = Column(Numeric(20, 0))
    OTHERTRADABLESHARES = Column(Numeric(20, 0))
    TRADESHARESTOTAL = Column(Numeric(20, 0))
    TOTAL = Column(Numeric(20, 0))
