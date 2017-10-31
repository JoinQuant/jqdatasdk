

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSANNUITYQ(Base):
    __tablename__ = "MAC_INSANNUITYQ"

    SGNQUARTER = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(2, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SHORTNAME = Column(String(40, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'))
    ANNUITYPAYMENT = Column(Numeric(22, 4))
    ANNUITYENTRUSTED = Column(Numeric(22, 4))
    ANNUITYINVESTED = Column(Numeric(22, 4))
