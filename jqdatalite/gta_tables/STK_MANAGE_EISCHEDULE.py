

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_EISCHEDULE(Base):
    __tablename__ = "STK_MANAGE_EISCHEDULE"

    BUSINESSID = Column(String(40), primary_key=True, nullable=False)
    EVENTID = Column(BigInteger, primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    RANK = Column(SmallInteger, primary_key=True, nullable=False)
    GRANTDATE = Column(DateTime)
    IMPLEMENTATIONPHASE = Column(String(100))
    SCHEDULEID = Column(String(12), primary_key=True, nullable=False)
    PEOPLENUMBER = Column(Integer)
    GRANTRIGHTS = Column(Numeric(20, 0))
    GRANTRIGHTSTOTOTAL = Column(Numeric(16, 4))
    INTERESTSRESERVED = Column(Numeric(20, 0))
    INTERESTSRESERVEDTOTOTAL = Column(Numeric(16, 4))
    ADJUSTMENTRATIO = Column(Numeric(4, 2))
    INVALIDRIGHTS = Column(Numeric(20, 0))
    EXECUTIVERIGHTS = Column(Numeric(20, 0))
    TECHNICIANRIGHTS = Column(Numeric(20, 0))
    EXERCISEPERIOD = Column(String(200))
    EXERCISESITUATION = Column(String(2))
    EXERCISEPEOPLE = Column(Integer)
    EXERCISEDNUMBER = Column(Numeric(20, 0))
    EXERCISEDNUMBERTOTOTAL = Column(Numeric(16, 4))
    REALEXERCISEDNUMBER = Column(Numeric(20, 0))
    EXECUTIVENUMBER = Column(Numeric(20, 0))
    TECHNICIANNUMBER = Column(Numeric(20, 0))
    PRICE = Column(Numeric(10, 4))
    REPURCHASEPRICE = Column(Numeric(10, 4))
    STRIKEPRICE = Column(Numeric(10, 4))
    REVENUEINCENTIVEFOREACH = Column(Numeric(10, 4))
    TOTALREWARDS = Column(Numeric(20, 2))
    AWARDEDADJUSTMENT = Column(String(2))
    EXERCISEADJUSTMENT = Column(String(2))
    FULLNAME = Column(String(200))
