

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHGSYSTFM_CALENDAR(Base):
    __tablename__ = "STK_SHGSYSTFM_CALENDAR"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True)
    SYMBOL = Column(String(20, u'utf8_bin'))
    BATCH = Column(String(20, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    STKREGDATESM = Column(DateTime)
    SDATEBCLGVR = Column(DateTime)
    EDATEBCLGVR = Column(DateTime)
    SHSDATEOLV = Column(DateTime)
    SHEDATEOLV = Column(DateTime)
    DATEHGSHHM = Column(DateTime)
    SRDATEPLIMP = Column(DateTime)
    CARVDSZSEMAH = Column(DateTime)
    CARVDSSEMAH = Column(DateTime)
    SARVDSZSEMAH = Column(DateTime)
    SARVDSSEMAH = Column(DateTime)
    MAHWRTARVDATE = Column(DateTime)
    FIRSTTRADINGDATE = Column(DateTime)
    MAHWRTLSFLDATE = Column(DateTime)
