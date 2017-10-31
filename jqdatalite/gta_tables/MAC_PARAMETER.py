

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PARAMETER(Base):
    __tablename__ = "MAC_PARAMETER"

    CLASSCODE = Column(BigInteger)
    CLASSNAME = Column(String(100, u'utf8_bin'))
    PARAMETERCODE = Column(String(20, u'utf8_bin'))
    PARAMETERNAME = Column(String(100, u'utf8_bin'))
    DESCRIPTION = Column(String(200, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
