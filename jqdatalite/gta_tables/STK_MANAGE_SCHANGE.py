

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_SCHANGE(Base):
    __tablename__ = "STK_MANAGE_SCHANGE"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    DECLARETYPEID = Column(String(100))
    CHANGEDATE = Column(DateTime, primary_key=True, nullable=False)
    CHANGEPOSITION = Column(SmallInteger, primary_key=True, nullable=False)
    CHANGETYPE = Column(SmallInteger, primary_key=True, nullable=False)
    NAME = Column(String(100), primary_key=True, nullable=False)
    PERSONID = Column(Numeric(20, 0))
    EDUCATIONID = Column(String(100))
    TITLE = Column(String(100))
    REASONID = Column(String(100))
    RESIGNATIONAGE = Column(SmallInteger)
    WORKYEARS = Column(Numeric(18, 2))
    FROMEXTERNALORINTERNAL = Column(SmallInteger)
    ISPROXYORNOT = Column(SmallInteger)
    CONCURRENTPOST = Column(SmallInteger)
    PARTTIMEORNOT = Column(SmallInteger)
    SELECTSOURCE = Column(SmallInteger)
    FULLNAME = Column(String(200))
