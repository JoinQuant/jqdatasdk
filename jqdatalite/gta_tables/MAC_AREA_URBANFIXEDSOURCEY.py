

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_URBANFIXEDSOURCEY(Base):
    __tablename__ = "MAC_AREA_URBANFIXEDSOURCEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    STATEBUDGET = Column(Numeric(18, 4))
    DOMESTICLOAN = Column(Numeric(18, 4))
    FOREIGNINVEST = Column(Numeric(18, 4))
    SELFRAISEDFUND = Column(Numeric(18, 4))
    OTHERFUND = Column(Numeric(18, 4))
    CENTREPROJECT = Column(Numeric(18, 4))
    LOCALPROJECT = Column(Numeric(18, 4))
