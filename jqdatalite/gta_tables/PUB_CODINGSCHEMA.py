

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class PUB_CODINGSCHEMA(Base):
    __tablename__ = "PUB_CODINGSCHEMA"

    CODE = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    CODINGSCHEMAID = Column(String(6, u'utf8_bin'), primary_key=True, nullable=False)
    CODINGSCHEMA = Column(String(40, u'utf8_bin'))
    VALUE = Column(String(100, u'utf8_bin'))
    VALUE_EN = Column(String(600, u'utf8_bin'))
    PARENTCODE = Column(String(12, u'utf8_bin'))
