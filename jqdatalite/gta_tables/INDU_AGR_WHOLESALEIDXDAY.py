

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AGR_WHOLESALEIDXDAY(Base):
    __tablename__ = "INDU_AGR_WHOLESALEIDXDAY"

    ENDDATE = Column(DateTime, primary_key=True)
    AGRIDX = Column(Numeric(10, 4))
    FOODBASKETIDX = Column(Numeric(10, 4))
