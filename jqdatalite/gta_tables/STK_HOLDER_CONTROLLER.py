

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_HOLDER_CONTROLLER(Base):
    __tablename__ = "STK_HOLDER_CONTROLLER"

    INSTITUTIONID = Column(BigInteger)
    SYMBOL = Column(String(20, u'utf8_bin'))
    ENDDATE = Column(DateTime)
    JUDGMENTSTANDARD = Column(String(2, u'utf8_bin'))
    SHAREHOLDERID = Column(BigInteger)
    DIRECTCONTROLLER = Column(String(240, u'utf8_bin'))
    DIRECTCONTROLLERNATUREID = Column(String(60, u'utf8_bin'))
    DIRECTCONTROLLERNATURE = Column(String(100, u'utf8_bin'))
    SHAREHOLDINGRATIO = Column(Numeric(20, 4))
    SHARES = Column(Numeric(20, 2))
    ACTUALCONTROLLER = Column(String(240, u'utf8_bin'))
    ACTUALCONTROLLERNATUREID = Column(String(200, u'utf8_bin'))
    ACTUALCONTROLLERNATURE = Column(String(400, u'utf8_bin'))
    ACTUALCONTROLLERSHARESNATUREID = Column(String(60, u'utf8_bin'))
    ACTUALCONTROLLERSHARESNATURE = Column(String(100, u'utf8_bin'))
    ACTUALCONTROLLERBACKGROUND = Column(String(4000, u'utf8_bin'))
    OWNERSHIPRATIO = Column(Numeric(20, 4))
    CONTROLRATIO = Column(Numeric(20, 4))
    SEPARATIONDEGREE = Column(Numeric(20, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
