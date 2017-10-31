

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_BOOMIDX(Base):
    __tablename__ = "MAC_INDUSTRY_BOOMIDX"

    SGNMONTH = Column(String(14, u'utf8_bin'))
    INDUSTRYID = Column(String(20, u'utf8_bin'))
    BOOMIDX = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
