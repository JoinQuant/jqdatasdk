

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHGSYSTFM_SHGFLTOP10(Base):
    __tablename__ = "STK_SHGSYSTFM_SHGFLTOP10"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    SHAREHOLDERNAME = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    BEFOREMATCHEDSHARES = Column(Numeric(20, 0))
    BEFOREMATCHEDPERCENTAGE = Column(Numeric(10, 4))
    VOTINGNUMBER = Column(Numeric(20, 0))
    VOTINGSTATUS = Column(String(12, u'utf8_bin'))
    AFTERMATCHEDSHARES = Column(Numeric(20, 0))
    AFTERMATCHEDPERCENTAGE = Column(Numeric(10, 4))
    COMPLETIONDATE = Column(DateTime)
