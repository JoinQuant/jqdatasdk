

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_STRUCTURE(Base):
    __tablename__ = "STK_MANAGE_STRUCTURE"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20, u'utf8_bin'))
    ENDDATE = Column(DateTime)
    REPTTYPEID = Column(String(12, u'utf8_bin'))
    STAFFNUMBER = Column(BigInteger)
    RETIREDNUMBER = Column(BigInteger)
    COMMISSIONNUMBER = Column(BigInteger)
    STANDARDCOMMISSIONNUMBER = Column(BigInteger)
    OTHERCOMMISSIONNUMBER = Column(BigInteger)
    STANDARDCOMMISSIONNAME = Column(String(200, u'utf8_bin'))
    STANDARDCOMMISSIONNAME_EN = Column(String(600, u'utf8_bin'))
    OTHERCOMMISSIONNAME = Column(String(100, u'utf8_bin'))
    OTHERCOMMISSIONNAME_EN = Column(String(600, u'utf8_bin'))
    DIRECTORNUMBER = Column(BigInteger)
    INDEPENDENTDIRECTORNUMBER = Column(BigInteger)
    FEMALEDIRECTORNUMBER = Column(BigInteger)
    SUPERVISORNUMBER = Column(BigInteger)
    STAFFSUPERVISORNUMBER = Column(BigInteger)
    EXECUTIVESNUMBER = Column(BigInteger)
    MANAGERNUMBER = Column(BigInteger)
    UPDATEID = Column(BigInteger, primary_key=True)
    UPDATETIME_EN = Column(DateTime)
