

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_STOCKTRADE(Base):
    __tablename__ = "MAC_STOCKTRADE"

    SGNYEAR = Column(String(16, u'utf8_bin'), primary_key=True)
    NOOFPUBLICCOMPANY = Column(BigInteger)
    NEWSTOCKNO = Column(BigInteger)
    ASHARESNEW = Column(BigInteger)
    BSHARESNEW = Column(BigInteger)
    TOTALMEMBER = Column(BigInteger)
    TOTALSHARE = Column(Numeric(20, 4))
    ATOTALSHARE = Column(Numeric(20, 4))
    BTOTALSHARE = Column(Numeric(20, 4))
    FLOWOFEQUITY = Column(Numeric(20, 4))
    FLOWOFEQUITYA = Column(Numeric(20, 4))
    FLOWOFEQUITYB = Column(Numeric(20, 4))
    TOTALSTOCKVALUE = Column(Numeric(20, 4))
    TOTALASTOCKVALUE = Column(Numeric(20, 4))
    TOTALBSTOCKVALUE = Column(Numeric(20, 4))
    FLOWEQUITYVALUE = Column(Numeric(20, 4))
    AFLOWEQUITYVALUE = Column(Numeric(20, 4))
    BFLOWEQUITYVALUE = Column(Numeric(20, 4))
    TRADEPRICEAMOUNT = Column(Numeric(20, 4))
    TRADEPRICEAMOUNTA = Column(Numeric(20, 4))
    TRADEPRICEAMOUNTB = Column(Numeric(20, 4))
    TOTALTRADESHARE = Column(Numeric(20, 4))
    TOTALTRADESHAREA = Column(Numeric(20, 4))
    TOTALTRADESHAREB = Column(Numeric(20, 4))
    HIGHVALUEOFSZCOMPOSITEINDEX = Column(Numeric(20, 4))
    LOWVALUEOFSZCOMPOSITEINDEX = Column(Numeric(20, 4))
    HIGHVALUEOFSHCOMPOSITEINDEX = Column(Numeric(20, 4))
    LOWVALUEOFSHCOMPOSITEINDEX = Column(Numeric(20, 4))
    CLOSEVALUEOFSZCOMPOSITEINDEX = Column(Numeric(20, 4))
    CLOSEVALUEOFSHCOMPOSITEINDEX = Column(Numeric(20, 4))
