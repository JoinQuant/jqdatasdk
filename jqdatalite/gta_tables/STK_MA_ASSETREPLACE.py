

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_ASSETREPLACE(Base):
    __tablename__ = "STK_MA_ASSETREPLACE"

    EVENTID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    ASSETSSURRENDEREDPARTY = Column(String(1000, u'utf8_bin'))
    SINSTITUTIONID = Column(Numeric(20, 0))
    SCONCERTEDACTION = Column(SmallInteger)
    ASSETSRECEIVEDPARTY = Column(String(1000, u'utf8_bin'))
    BINSTITUTIONID = Column(Numeric(20, 0))
    RCONCERTEDACTION = Column(SmallInteger)
    SRECEIVINGPARTY = Column(String(1000, u'utf8_bin'))
    RRECEIVINGPARTY = Column(String(1000, u'utf8_bin'))
    SBOOKVALUE = Column(Numeric(20, 4))
    STRADINGPRICE = Column(Numeric(20, 4))
    RBOOKVALUE = Column(Numeric(20, 4))
    RTRADINGPRICE = Column(Numeric(20, 4))
    STRANSFERDATE = Column(DateTime)
    RTRANSFERDATE = Column(DateTime)
    SAPPRSREPTNO = Column(String(100, u'utf8_bin'))
    RAPPRSREPTNO = Column(String(100, u'utf8_bin'))
