

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_SUPPLEMENT(Base):
    __tablename__ = "STK_MANAGE_SUPPLEMENT"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    SHAREHOLDERS = Column(Numeric(20, 0))
    TOP10HOLDERRELATIONSIGN = Column(String(2))
    EQUITYCHANGEDSIGN = Column(String(2))
    CONSISTENCY = Column(String(2))
    FULLNAME = Column(String(200))
