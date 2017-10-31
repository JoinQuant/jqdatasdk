

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_CMEMBERS(Base):
    __tablename__ = "STK_MANAGE_CMEMBERS"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20))
    COMMITTEE = Column(String(200))
    REPTTYPEID = Column(String(40))
    DECLAREDATE = Column(DateTime)
    MEMBERNAME = Column(String(200))
    PERSONID = Column(Numeric(20, 0))
    POSITIONID = Column(String(100))
    STARTDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
    FULLNAME = Column(String(200))
    UPDATEID = Column(BigInteger, primary_key=True)
