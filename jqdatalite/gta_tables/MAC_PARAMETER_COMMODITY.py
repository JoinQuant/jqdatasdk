

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PARAMETER_COMMODITY(Base):
    __tablename__ = "MAC_PARAMETER_COMMODITY"

    COMMODITYID = Column(BigInteger, primary_key=True)
    COMMODITYCODE = Column(String(20, u'utf8_bin'))
    COMMODITYNAME = Column(String(800, u'utf8_bin'))
    SYSTEMID = Column(String(20, u'utf8_bin'))
