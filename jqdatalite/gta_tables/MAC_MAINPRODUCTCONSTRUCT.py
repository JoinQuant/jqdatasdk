

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MAINPRODUCTCONSTRUCT(Base):
    __tablename__ = "MAC_MAINPRODUCTCONSTRUCT"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    PRODUCTCAPACITYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    UNITNAME = Column(String(40, u'utf8_bin'))
    CONSTRUCT = Column(Numeric(18, 4))
    UNDERCONSTRUCT = Column(Numeric(18, 4))
    NEWSTART = Column(Numeric(18, 4))
    NEWINCREASEACCUMULATE = Column(Numeric(18, 4))
    NEWINCREASE = Column(Numeric(18, 4))
