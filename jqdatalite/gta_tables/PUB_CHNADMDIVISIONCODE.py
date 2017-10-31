

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class PUB_CHNADMDIVISIONCODE(Base):
    __tablename__ = "PUB_CHNADMDIVISIONCODE"

    DIVISIONCODE = Column(String(12, u'utf8_bin'), primary_key=True)
    DIVISIONNAME = Column(String(100, u'utf8_bin'))
    DIVISIONNAME_EN = Column(String(200, u'utf8_bin'))
    P_DIVISIONCODE = Column(String(12, u'utf8_bin'))
