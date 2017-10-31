

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCALEXPENSEMONTH(Base):
    __tablename__ = "MAC_FISCALEXPENSEMONTH"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    FISCALEXPENSEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    EXPENSE = Column(Numeric(18, 4))
    EXPENSEYOY = Column(Numeric(10, 4))
