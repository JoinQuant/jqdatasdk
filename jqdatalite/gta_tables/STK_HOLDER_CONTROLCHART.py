

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_HOLDER_CONTROLCHART(Base):
    __tablename__ = "STK_HOLDER_CONTROLCHART"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    FILETTYE = Column(String(20, u'utf8_bin'))
