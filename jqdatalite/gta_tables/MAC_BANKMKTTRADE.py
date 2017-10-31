

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_BANKMKTTRADE(Base):
    __tablename__ = "MAC_BANKMKTTRADE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    MATURITYTYPE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TRADEVOLUME = Column(Numeric(20, 4))
    AVGINTERESTRATE = Column(Numeric(20, 4))
