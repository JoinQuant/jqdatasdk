

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_EXCITATION(Base):
    __tablename__ = "STK_MANAGE_EXCITATION"

    EVENTID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20))
    INSTITUTIONID = Column(Numeric(20, 0))
    DECLAREDATE = Column(DateTime)
    SCHEDULEID = Column(String(100))
    PERSONID = Column(Numeric(20, 0))
    FULLNAME = Column(String(400))
    POSITION = Column(String(400))
    IMPLEMENTATIONPHASE = Column(String(200))
    SUBJECT = Column(String(40))
    SUBJECTID = Column(String(12))
    OBTAINEDSHARES = Column(Numeric(20, 2))
    PROPORTION1 = Column(Numeric(10, 4))
    PROPORTION2 = Column(Numeric(10, 4))
    EXERCISESIGN = Column(SmallInteger)
    REASONID = Column(String(100))
    EXERCISEDATE = Column(DateTime)
    EXERCISENUMBER = Column(Numeric(20, 2))
    BUSINESSID = Column(String(40))
    UPDATEID = Column(BigInteger, primary_key=True)
