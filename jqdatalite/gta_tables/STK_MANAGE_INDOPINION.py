

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_MANAGE_INDOPINION(Base):
    __tablename__ = "STK_MANAGE_INDOPINION"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    RANK = Column(BigInteger, primary_key=True, nullable=False)
    NAME = Column(String(200), primary_key=True, nullable=False)
    PERSONID = Column(Numeric(20, 0))
    ITEMID = Column(String(200))
    CATEGORYID = Column(String(40))
    FULLNAME = Column(String(200))
