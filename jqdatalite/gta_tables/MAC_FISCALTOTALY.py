

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCALTOTALY(Base):
    __tablename__ = "MAC_FISCALTOTALY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    REVENUE = Column(Numeric(18, 4))
    EXPENSE = Column(Numeric(18, 4))
    REVENUEYOY = Column(Numeric(10, 4))
    EXPENSEYOY = Column(Numeric(10, 4))
