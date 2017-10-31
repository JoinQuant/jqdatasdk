

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MONEYPROVIDE(Base):
    __tablename__ = "MAC_MONEYPROVIDE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    M2 = Column(Numeric(20, 4))
    M1 = Column(Numeric(20, 4))
    M0 = Column(Numeric(20, 4))
    DEMANDDEPOSIT = Column(Numeric(20, 4))
    QUASIMONEY = Column(Numeric(20, 4))
    CORPORATETIMEDEPOSIT = Column(Numeric(20, 4))
    PERSONALSAVINGDEPOSIT = Column(Numeric(20, 4))
    OTHERDEPOSITS = Column(Numeric(20, 4))
