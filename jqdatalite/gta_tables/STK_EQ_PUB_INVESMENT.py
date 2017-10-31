

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_PUB_INVESMENT(Base):
    __tablename__ = "STK_EQ_PUB_INVESMENT"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    EVENTTYPEID = Column(String(12, u'utf8_bin'))
    ISSUESTARTDATE = Column(DateTime, primary_key=True, nullable=False)
    PROJECTORDER = Column(Integer, primary_key=True, nullable=False)
    PROJECTNAME = Column(String(400, u'utf8_bin'))
    PROJECTNAME_EN = Column(String(1000, u'utf8_bin'))
    PROJECTNATUREID = Column(String(12, u'utf8_bin'))
    PROJECTNATURE = Column(String(20, u'utf8_bin'))
    PROJECTTYPEID = Column(String(12, u'utf8_bin'))
    PROJECTTYPE = Column(String(100, u'utf8_bin'))
    PLANINVESTAMOUNT = Column(Numeric(20, 2))
    PLANINVESTRECORDINGAMOUNT = Column(Numeric(20, 2))
    EXPECTSALESINCOME = Column(Numeric(20, 2))
    EXPECTNETPROFIT = Column(Numeric(20, 2))
    EXPECTYEARPROFITMARGIN = Column(Numeric(10, 4))
    PROJECTPERIOD = Column(Numeric(10, 2))
    PAYBACKPERIOD = Column(Numeric(10, 2))
    PROVINCEID = Column(String(12, u'utf8_bin'))
    PROVINCE = Column(String(40, u'utf8_bin'))
    INDUSTRYCODE = Column(String(20, u'utf8_bin'))
    INDUSTRY = Column(String(100, u'utf8_bin'))
    PROJECTCHANGESTATEID = Column(String(12, u'utf8_bin'))
    CHANGEEVENTID = Column(String(40, u'utf8_bin'))
    ID_0098 = Column(BigInteger)
    UPDATETIME_EN = Column(DateTime)
