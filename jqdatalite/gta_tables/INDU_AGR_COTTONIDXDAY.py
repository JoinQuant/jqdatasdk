

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AGR_COTTONIDXDAY(Base):
    __tablename__ = "INDU_AGR_COTTONIDXDAY"

    ENDDATE = Column(DateTime, primary_key=True)
    CCINDEX328 = Column(Numeric(18, 4))
    CCINDEX328CHANGE = Column(Numeric(10, 4))
    CCINDEX527 = Column(Numeric(18, 4))
    CCINDEX527CHANGE = Column(Numeric(10, 4))
    CCINDEX229 = Column(Numeric(18, 4))
    CCINDEX229CHANGE = Column(Numeric(10, 4))
