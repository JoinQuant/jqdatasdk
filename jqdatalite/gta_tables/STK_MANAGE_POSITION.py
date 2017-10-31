

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_POSITION(Base):
    __tablename__ = "STK_MANAGE_POSITION"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    POSITIONID = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    SERVICESTARTDATE = Column(DateTime, primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    REPTTYPEID = Column(String(12, u'utf8_bin'))
    REPTTYPE = Column(String(100, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    POSITION = Column(String(400, u'utf8_bin'))
    ORIGINALPOSITION = Column(String(400, u'utf8_bin'))
    POSITION_EN = Column(String(1000, u'utf8_bin'))
    SERVICEENDDATE = Column(DateTime)
    RESIGNREASONID = Column(String(12, u'utf8_bin'))
    RESIGNREASON = Column(String(100, u'utf8_bin'))
    SERVICESTATUS = Column(String(2, u'utf8_bin'))
    PERSONID = Column(Numeric(20, 0))
