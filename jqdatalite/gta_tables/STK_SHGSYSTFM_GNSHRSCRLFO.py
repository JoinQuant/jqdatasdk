

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHGSYSTFM_GNSHRSCRLFO(Base):
    __tablename__ = "STK_SHGSYSTFM_GNSHRSCRLFO"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    LISTEDDATE = Column(DateTime, primary_key=True, nullable=False)
    LISTEDBATCH = Column(SmallInteger)
    LISTEDSHAREHOLDERS = Column(BigInteger)
    SUMLISTEDSHARES = Column(Numeric(20, 0))
    LOCKSHARESTOTAL = Column(Numeric(20, 0))
    PCTSRRSCITSHRSC = Column(Numeric(10, 4))
    PCTSRRSCITFLASH = Column(Numeric(10, 4))
    PCTSRRSCITCS = Column(Numeric(10, 4))
    REMAINEDLOCKSHARES = Column(Numeric(20, 0))
