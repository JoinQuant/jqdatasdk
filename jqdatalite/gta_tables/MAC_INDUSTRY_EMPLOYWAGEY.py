

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_EMPLOYWAGEY(Base):
    __tablename__ = "MAC_INDUSTRY_EMPLOYWAGEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    OBJECTID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    INDUSTRYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    EMPLOY = Column(Numeric(18, 4))
    AVGWAGE = Column(Numeric(18, 4))
    INDUSTRYNAME = Column(String(100, u'utf8_bin'))
    OBJECTNAME = Column(String(20, u'utf8_bin'))
