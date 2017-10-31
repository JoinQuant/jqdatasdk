

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SALE_SCALERETAILMONTH(Base):
    __tablename__ = "MAC_SALE_SCALERETAILMONTH"

    DECLAREDATE = Column(DateTime)
    SGNMONTH = Column(String(14, u'utf8_bin'))
    DATASIGN = Column(String(4, u'utf8_bin'))
    RETAILSUM = Column(Numeric(18, 4))
    RETAIL = Column(Numeric(18, 4))
    CATERING = Column(Numeric(18, 4))
    RETAILSUMYOY = Column(Numeric(10, 4))
    RETAILYOY = Column(Numeric(10, 4))
    CATERINGYOY = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
