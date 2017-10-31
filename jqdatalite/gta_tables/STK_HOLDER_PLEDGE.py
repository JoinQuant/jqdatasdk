

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_HOLDER_PLEDGE(Base):
    __tablename__ = "STK_HOLDER_PLEDGE"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    SHAREHOLDERID = Column(Numeric(20, 0))
    FULLNAME = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    PLEDGEFREEZINGCUSTODYNUMBER = Column(Numeric(20, 2))
    PLEDGENUMBER = Column(Numeric(20, 2))
    FREEZINGNUMBER = Column(Numeric(20, 2))
    CUSTODYNUMBER = Column(Numeric(20, 2))
