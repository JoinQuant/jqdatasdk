

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_MEETINGSSTATS(Base):
    __tablename__ = "STK_MANAGE_MEETINGSSTATS"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20))
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    DIRECTORMEETINGTIMES = Column(SmallInteger)
    SUPERVISORMEETINGTIMES = Column(SmallInteger)
    HOLDERMEETINGTIMES = Column(SmallInteger)
    FULLNAME = Column(String(200))
