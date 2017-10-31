

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_EIPLAN(Base):
    __tablename__ = "STK_MANAGE_EIPLAN"

    BUSINESSID = Column(String(40), primary_key=True, nullable=False)
    EVENTID = Column(BigInteger, primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    FIRSTDECLAREDATE = Column(DateTime)
    HOLDERSMEETINGDATE = Column(DateTime)
    SUBJECTID = Column(String(12), primary_key=True, nullable=False)
    STOCKTYPE = Column(String(12), primary_key=True, nullable=False)
    SUBJECTSOURCEID = Column(String(12), primary_key=True, nullable=False)
    IMPLEMENTATIONPHASE = Column(String(100))
    AMOUNT = Column(Numeric(20, 0))
    AMOUNTTOTOTAL = Column(Numeric(16, 4))
    INTERESTSRESERVED = Column(Numeric(20, 0))
    INTERESTSRESERVEDTOTOTAL = Column(Numeric(16, 4))
    PEOPLENUMBER = Column(Integer)
    EXECUTIVERIGHTSAMOUNT = Column(Numeric(20, 0))
    TECHNICIANRIGHTSAMOUNT = Column(Numeric(20, 0))
    PRICE = Column(Numeric(10, 4))
    AWARDINGWAY = Column(String(2))
    TERMOFVALIDITY = Column(Numeric(4, 2))
    LOCKUPPERIOD = Column(Numeric(4, 2))
    FIRSTEXERCISEPERIOD = Column(Numeric(4, 2))
    RESERVEEXERCISEPERIOD = Column(Numeric(4, 2))
    FULLNAME = Column(String(200))
