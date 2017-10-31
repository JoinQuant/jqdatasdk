

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MEQUITYMARRE(Base):
    __tablename__ = "MAC_MEQUITYMARRE"

    SGNMONTH = Column(String(16, u'utf8_bin'), primary_key=True, nullable=False)
    EXCHANGESGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    TRADEDAYS = Column(BigInteger)
    PUBLICCOMPANYNUMBER = Column(BigInteger)
    NEWIPONO = Column(BigInteger)
    LISTEDSTOCK = Column(BigInteger)
    LISTEDSECURITY = Column(BigInteger)
    STOCKISSUEDSHARE = Column(Numeric(20, 4))
    STOCKISSUEDTOTALVALUE = Column(Numeric(20, 4))
    FLOWOFSTOCKSHARE = Column(Numeric(20, 4))
    FLOWOFSTOCKSHAREVALUE = Column(Numeric(20, 4))
    TRADETOTALVALUE = Column(Numeric(20, 4))
    STOCKTRADETOTALVALUE = Column(Numeric(20, 4))
    NATIONALDEBTTRADEVALUE = Column(Numeric(20, 4))
    TRADEVALUESMEBOARD = Column(Numeric(20, 4))
    TRADEVALUEGEBOARD = Column(Numeric(20, 4))
    DAYAVGTRADEVALUE = Column(Numeric(20, 4))
    STOCKDAYAVGTRADEVALUE = Column(Numeric(20, 4))
    NDEBTDAYAVGTRADEVALUE = Column(Numeric(20, 4))
    MONTHLYSHARESTRADE = Column(Numeric(20, 4))
    MONTHLYENDAVGPE = Column(Numeric(20, 4))
    MONTHLYFLOWTURNOVERRATE = Column(Numeric(20, 4))
