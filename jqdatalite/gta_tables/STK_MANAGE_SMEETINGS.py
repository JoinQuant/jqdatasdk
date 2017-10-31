

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_SMEETINGS(Base):
    __tablename__ = "STK_MANAGE_SMEETINGS"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20))
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    DECLAREDATE = Column(DateTime)
    MEETINGDATE = Column(DateTime, primary_key=True, nullable=False)
    STARTDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
    ADDRESS = Column(String(1000))
    MEETINGTYPEID = Column(String(100))
    CONVENEWAYID = Column(String(100))
    VOTEWAYID = Column(String(100))
    SHAREHOLDERNUMBER = Column(BigInteger)
    SHARES = Column(Numeric(18, 2))
    PROPORTION = Column(Numeric(10, 4))
    FULLNAME = Column(String(200))
