

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_INDATTENDED(Base):
    __tablename__ = "STK_MANAGE_INDATTENDED"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20))
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    NAME = Column(String(100), primary_key=True, nullable=False)
    PERSONID = Column(Numeric(20, 0))
    PARTICIPATETIMES = Column(BigInteger)
    ENTRUSTTIMES = Column(BigInteger)
    ABSENTTIMES = Column(BigInteger)
    FULLNAME = Column(String(200))
