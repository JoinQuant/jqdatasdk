

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_ASSETTRANS(Base):
    __tablename__ = "STK_MA_ASSETTRANS"

    EVENTID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    SELLER = Column(String(1000, u'utf8_bin'))
    SINSTITUTIONID = Column(Numeric(20, 0))
    BUYER = Column(String(1000, u'utf8_bin'))
    BINSTITUTIONID = Column(Numeric(20, 0))
    VARIETY = Column(SmallInteger)
    TRADINGATTITUDE = Column(SmallInteger)
    BUYERCOMBINATIONORNOT = Column(SmallInteger)
    BUYERCONCERTEDACTION = Column(SmallInteger)
    SELLERCOMBINATIONORNOT = Column(SmallInteger)
    SELLERCONCERTEDACTION = Column(SmallInteger)
    CONTROLTRANSFERORNOT = Column(SmallInteger)
    TRADINGTYPEID = Column(String(200, u'utf8_bin'))
    TRADINGTYPE = Column(String(200, u'utf8_bin'))
    TOUCHEDOFFERORNOT = Column(SmallInteger)
    OFFEREXEMPTIONORNOT = Column(SmallInteger)
    TRANSFERDATE = Column(DateTime)
