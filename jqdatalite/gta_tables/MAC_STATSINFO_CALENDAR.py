

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_STATSINFO_CALENDAR(Base):
    __tablename__ = "MAC_STATSINFO_CALENDAR"

    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    WEEKMARK = Column(String(2, u'utf8_bin'))
    CONTENT = Column(String(100, u'utf8_bin'), primary_key=True, nullable=False)
