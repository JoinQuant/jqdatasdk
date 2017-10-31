

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRYVALUEADD(Base):
    __tablename__ = "MAC_INDUSTRYVALUEADD"

    DECLAREDATE = Column(DateTime)
    SGNMONTH = Column(String(14, u'utf8_bin'))
    DATASIGN = Column(String(4, u'utf8_bin'))
    VALUEADD = Column(Numeric(18, 4))
    LIGHTINDUSTRY = Column(Numeric(18, 4))
    HEAVYINDUSTRY = Column(Numeric(18, 4))
    STATEOWNED = Column(Numeric(18, 4))
    PRIVATE = Column(Numeric(18, 4))
    COLLECTIVE = Column(Numeric(18, 4))
    STOCKCOOPERATE = Column(Numeric(18, 4))
    JOINTSTOCK = Column(Numeric(18, 4))
    FOREIGN = Column(Numeric(18, 4))
    VALUEADDYOY = Column(Numeric(10, 4))
    LIGHTINDUSTYOY = Column(Numeric(10, 4))
    HEAVYINDUSTYOY = Column(Numeric(10, 4))
    STATEOWNEDYOY = Column(Numeric(10, 4))
    PRIVATEYOY = Column(Numeric(10, 4))
    COLLECTIVEYOY = Column(Numeric(10, 4))
    STOCKCOOPERATEYOY = Column(Numeric(10, 4))
    JOINTSTOCKYOY = Column(Numeric(10, 4))
    FOREIGNYOY = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
    VALUEADDMOM = Column(Numeric(10, 4))
