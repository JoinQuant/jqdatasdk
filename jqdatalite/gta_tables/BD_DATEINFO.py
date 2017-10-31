

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class BD_DATEINFO(Base):
    __tablename__ = "BD_DATEINFO"

    INSTITUTIONID = Column(String(40))
    ORGID = Column(BigInteger, primary_key=True, nullable=False)
    SYMBOL = Column(String(12), primary_key=True, nullable=False)
    SHORTNAME = Column(String(40))
    STOCKVARIETYCODE = Column(String(12))
    LISTSIGN = Column(SmallInteger)
    STARTDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
