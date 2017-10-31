

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDU_URBANFIXEDREGISTY(Base):
    __tablename__ = "MAC_INDU_URBANFIXEDREGISTY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INDUSTRYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    FIXEDASSETSINVEST = Column(Numeric(18, 4))
    CENTREPROJECT = Column(Numeric(18, 4))
    LOCALPROJECT = Column(Numeric(18, 4))
    DOMESTIC = Column(Numeric(18, 4))
    HKMACAOTAIWAN = Column(Numeric(18, 4))
    FOREIGN = Column(Numeric(18, 4))
    STATEOWNED = Column(Numeric(18, 4))
    COLLECTIVE = Column(Numeric(18, 4))
    INDIVIDUAL = Column(Numeric(18, 4))
