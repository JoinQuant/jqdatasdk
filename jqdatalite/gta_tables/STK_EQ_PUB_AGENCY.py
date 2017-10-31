

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_EQ_PUB_AGENCY(Base):
    __tablename__ = "STK_EQ_PUB_AGENCY"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    EVENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    EVENTTYPEID = Column(String(12, u'utf8_bin'))
    ISSUESTARTDATE = Column(DateTime, primary_key=True, nullable=False)
    AGENTTYPEID = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    AGENTTYPE = Column(String(100, u'utf8_bin'))
    AGENTID = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    AGENT = Column(String(200, u'utf8_bin'))
    AGENT_EN = Column(String(400, u'utf8_bin'))
    UNDERWRITEDSHARES = Column(Numeric(20, 0))
    UNDERWRITEDTOSUM = Column(Numeric(10, 4))
    ID_0096 = Column(BigInteger)
