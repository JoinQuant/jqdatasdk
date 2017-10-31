

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class PT_LCAPPLICATION(Base):
    __tablename__ = "PT_LCAPPLICATION"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    INVENTION = Column(Integer)
    UTILITYMODEL = Column(Integer)
    DESIGN = Column(Integer)
