

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHGSYSTFM_SHRSCSHRLFO(Base):
    __tablename__ = "STK_SHGSYSTFM_SHRSCSHRLFO"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    LISTEDDATE = Column(DateTime, primary_key=True, nullable=False)
    SHAREHOLDERNAME = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    LISTEDSHARES = Column(Numeric(20, 0))
    LOCKSHARES = Column(Numeric(20, 0))
    LISTEDSHARESPERCENTAGE = Column(Numeric(10, 4))
