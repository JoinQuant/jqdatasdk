

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_DEPOSITINTERESTRATE(Base):
    __tablename__ = "MAC_DEPOSITINTERESTRATE"

    CHANGEDATE = Column(DateTime, primary_key=True)
    CURRENTDEPOSIT = Column(Numeric(10, 4))
    LUMPFIXED3MONTH = Column(Numeric(10, 4))
    LUMPFIXED6MONTH = Column(Numeric(10, 4))
    LUMPFIXED1YEAR = Column(Numeric(10, 4))
    LUMPFIXED2YEAR = Column(Numeric(10, 4))
    LUMPFIXED3YEAR = Column(Numeric(10, 4))
    LUMPFIXED5YEAR = Column(Numeric(10, 4))
    INSTALLMENT1YEAR = Column(Numeric(10, 4))
    INSTALLMENT3YEAR = Column(Numeric(10, 4))
    INSTALLMENT5YEAR = Column(Numeric(10, 4))
    TIMEDEMANDDEPOSIT = Column(String(200, u'utf8_bin'))
    AGREEMENTDEPOSIT = Column(Numeric(10, 4))
    NOTICE1DAY = Column(Numeric(10, 4))
    NOTICE7DAY = Column(Numeric(10, 4))
    HOUSEFUND = Column(Numeric(10, 4))
    HOUSEFUNDACCUMULATION = Column(Numeric(10, 4))
