

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MA_MERGER(Base):
    __tablename__ = "STK_MA_MERGER"

    EVENTID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    MERGERTYPEID = Column(String(100, u'utf8_bin'))
    MERGERTYPE = Column(String(200, u'utf8_bin'))
    COMBININGPARTY = Column(String(1000, u'utf8_bin'))
    COMBININGINSTITUTIONID = Column(Numeric(20, 0))
    COMBINEDPARTY = Column(String(1000, u'utf8_bin'))
    COMBINEDINSTITUTIONID = Column(Numeric(20, 0))
    CONCERTEDACTION = Column(SmallInteger)
    SURVIVINGPARTY = Column(String(1000, u'utf8_bin'))
    PROPORTION = Column(Numeric(10, 4))
    COMBININGSTOCKPRICE = Column(Numeric(10, 3))
    COMBINEDSTOCKPRICE = Column(Numeric(10, 3))
    LISTEDDATE = Column(DateTime)
    ISSUESHARES = Column(BigInteger)
