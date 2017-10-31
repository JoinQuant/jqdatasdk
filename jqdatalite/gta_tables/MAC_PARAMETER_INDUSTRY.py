

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PARAMETER_INDUSTRY(Base):
    __tablename__ = "MAC_PARAMETER_INDUSTRY"

    SYSTEMID = Column(String(20, u'utf8_bin'))
    INDUSTRYID = Column(BigInteger)
    INDUSTRYCODE = Column(String(20, u'utf8_bin'))
    INDUSTRYNAME = Column(String(100, u'utf8_bin'))
    ENINDUSTRYNAME = Column(String(200, u'utf8_bin'))
    INDUSTRYLEVEL = Column(BigInteger)
    INDUSTRYCLASS = Column(String(100, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
