

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_TENDEROFFER(Base):
    __tablename__ = "STK_MA_TENDEROFFER"

    EVENTID = Column(Numeric(20, 0), primary_key=True)
    ACQUIRER = Column(String(1000, u'utf8_bin'))
    ACQUIRERINSTITUTIONID = Column(Numeric(20, 0))
    BUYERCOMBINATIONORNOT = Column(SmallInteger)
    BUYERCONCERTEDACTION = Column(SmallInteger)
    TRADINGATTITUDE = Column(SmallInteger)
    CONTROLTRANSFERORNOT = Column(SmallInteger)
    TYPE = Column(SmallInteger)
    PREORDERTSHARESVOLUME = Column(BigInteger)
    PREORDERTSHARESRATIO = Column(Numeric(10, 4))
    TSHARESOFFERPRICE = Column(Numeric(10, 3))
    TSHARESBASEPRICE = Column(Numeric(10, 3))
    PREORDERNONTSHARESVOLUME = Column(BigInteger)
    PREORDERNONTSHARESRATIO = Column(Numeric(10, 4))
    NONTSHARESOFFERPRICE = Column(Numeric(10, 3))
    NONTSHARESBASEPRICE = Column(Numeric(10, 3))
    AIMTOTERMINATEORNOT = Column(SmallInteger)
    BETERMINATEDORNOT = Column(SmallInteger)
    CONTINUEDLISTINGORNOT = Column(SmallInteger)
    STARTDATE = Column(DateTime)
    EXPIRATIONDATE = Column(DateTime)
    COMPETITIVETENDEROFFER = Column(String(4, u'utf8_bin'))
    PREACCEPTTSHARESVOLUME = Column(BigInteger)
    PREACCEPTNONTSHARESVOLUME = Column(BigInteger)
    TSHARESVOLUME = Column(BigInteger)
    TSHARESRATIO = Column(Numeric(10, 4))
    NONTSHARESVOLUME = Column(BigInteger)
    NONTSHARESRATIO = Column(Numeric(10, 4))
    PAYTYPE = Column(SmallInteger)
