

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_ASSETSTOPAY(Base):
    __tablename__ = "STK_MA_ASSETSTOPAY"

    EVENTID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    AMOUNT = Column(Numeric(20, 4))
    ASSETNAME = Column(String(400, u'utf8_bin'))
    OWNERSHIP = Column(String(200, u'utf8_bin'))
    BOOKVALUE = Column(Numeric(20, 4))
    EVALUATIONVALUE = Column(Numeric(20, 4))
    BASEDAY = Column(DateTime)
    GUARANTEE = Column(String(100, u'utf8_bin'))
    AMOUNTTOBUYERTOTALASSETS = Column(Numeric(10, 4))
    AMOUNTTOSELLERTOTALASSETS = Column(Numeric(10, 4))
    EVALUATIONINSTITUTION = Column(String(100, u'utf8_bin'))
