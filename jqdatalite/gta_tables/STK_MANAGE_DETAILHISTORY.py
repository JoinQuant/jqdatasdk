

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_DETAILHISTORY(Base):
    __tablename__ = "STK_MANAGE_DETAILHISTORY"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    FULLNAME = Column(String(100), primary_key=True, nullable=False)
    FULLNAME_EN = Column(String(400))
    POSITIONCODE = Column(String(24))
    POSITION = Column(String(200), primary_key=True, nullable=False)
    POSITION_EN = Column(String(1000))
    GENDER = Column(String(100))
    DEGREEID = Column(String(12))
    SERVICESTARTDATE = Column(String(100))
    SERVICEENDDATE = Column(String(100))
    PAIDSIGN = Column(SmallInteger)
    TOTALSALARY = Column(Numeric(20, 2))
    ALLOWANCE = Column(Numeric(20, 2))
    ISCONCURRENTPOSITION = Column(SmallInteger)
    AGE = Column(Integer)
    HOLDSHARES = Column(Numeric(19, 2))
    PROFESSIONALTITLE = Column(String(200))
