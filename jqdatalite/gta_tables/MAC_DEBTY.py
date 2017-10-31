

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_DEBTY(Base):
    __tablename__ = "MAC_DEBTY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    DEBTORID = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    FROMFOREIGNGOV = Column(Numeric(18, 2))
    FROMIFI = Column(Numeric(18, 2))
    FROMFOREIGNOTHERBANKS = Column(Numeric(18, 2))
    BUYERSCREDIT = Column(Numeric(18, 2))
    FROMFOREIGNENTITY = Column(Numeric(18, 2))
    FROMFOREIGNBANKS = Column(Numeric(18, 2))
    BONDISSUEDABROAD = Column(Numeric(18, 2))
    TRADEFINANCING = Column(Numeric(18, 2))
    NONRESIDENTDEPOSITS = Column(Numeric(18, 2))
    INTERNATIONALFINANCELEASE = Column(Numeric(18, 2))
    LIABILITYINCOMPENSATIONTRD = Column(Numeric(18, 2))
    TRADECREDITS = Column(Numeric(18, 2))
    OTHERS = Column(Numeric(18, 2))
    TOTAL = Column(Numeric(18, 2))
