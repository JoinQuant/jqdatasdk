

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDU_URBANFIXEDSOURCEY(Base):
    __tablename__ = "MAC_INDU_URBANFIXEDSOURCEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INDUSTRYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TOTALSOURCE = Column(Numeric(18, 4))
    STATEBUDGET = Column(Numeric(18, 4))
    DOMESTICLOAN = Column(Numeric(18, 4))
    FOREIGNINVEST = Column(Numeric(18, 4))
    SELFRAISEDFUND = Column(Numeric(18, 4))
    OTHERFUND = Column(Numeric(18, 4))
    FIXEDASSETSINVEST = Column(Numeric(18, 4))
    NEWFIXEDASSETS = Column(Numeric(18, 4))
    USERATE = Column(Numeric(10, 4))
