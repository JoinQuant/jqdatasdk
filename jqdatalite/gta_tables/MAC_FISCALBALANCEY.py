

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCALBALANCEY(Base):
    __tablename__ = "MAC_FISCALBALANCEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    REVENUE = Column(Numeric(18, 4))
    CENTRALREVENUE = Column(Numeric(18, 4))
    LOCALREVENUE = Column(Numeric(18, 4))
    CENTRALREVENUERATE = Column(Numeric(10, 4))
    LOCALREVENUERATE = Column(Numeric(10, 4))
    EXPENSE = Column(Numeric(18, 4))
    CENTRALEXPENSE = Column(Numeric(18, 4))
    LOCALEXPENSE = Column(Numeric(18, 4))
    CENTRALEXPENSERATE = Column(Numeric(10, 4))
    LOCALEXPENSERATE = Column(Numeric(10, 4))
