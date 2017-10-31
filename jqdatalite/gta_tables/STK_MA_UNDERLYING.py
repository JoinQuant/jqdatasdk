

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_UNDERLYING(Base):
    __tablename__ = "STK_MA_UNDERLYING"

    EVENTID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    UNDERLYINGNAME = Column(String(1400, u'utf8_bin'))
    SYMBOL = Column(String(20, u'utf8_bin'))
    OWNERSHIP = Column(String(1000, u'utf8_bin'))
    PROPERTYID = Column(String(40, u'utf8_bin'))
    PROPERTY = Column(String(200, u'utf8_bin'))
    NETASSETSPERSHARE = Column(Numeric(20, 4))
    VOLUME = Column(BigInteger)
    PROPORTION = Column(Numeric(10, 4))
    BOOKVALUE = Column(Numeric(20, 4))
    EVALUATIONVALUE = Column(Numeric(20, 4))
    BASEDAY = Column(DateTime)
    GUARANTEEID = Column(String(40, u'utf8_bin'))
    GUARANTEE = Column(String(200, u'utf8_bin'))
    AMOUNTTOBUYERTOTALASSETS = Column(Numeric(10, 4))
    AMOUNTTOSELLERTOTALASSETS = Column(Numeric(10, 4))
    BEQUITYPROPORTIONBEFORE = Column(Numeric(10, 4))
    BSTATUSBEFOREID = Column(String(40, u'utf8_bin'))
    BSTATUSBEFORE = Column(String(200, u'utf8_bin'))
    BEQUITYPROPORTIONAFTER = Column(Numeric(10, 4))
    BSTATUSAFTERID = Column(String(40, u'utf8_bin'))
    BSTATUSAFTER = Column(String(200, u'utf8_bin'))
    SEQUITYPROPORTIONBEFORE = Column(Numeric(10, 4))
    SSTATUSBEFOREID = Column(String(40, u'utf8_bin'))
    SSTATUSBEFORE = Column(String(200, u'utf8_bin'))
    SEQUITYPROPORTIONAFTER = Column(Numeric(10, 4))
    SSTATUSAFTERID = Column(String(40, u'utf8_bin'))
    SSTATUSAFTER = Column(String(200, u'utf8_bin'))
    APPRSREPTNO = Column(String(100, u'utf8_bin'))
