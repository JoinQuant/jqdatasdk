

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_GUARANTEE_STATISTICS(Base):
    __tablename__ = "STK_GUARANTEE_STATISTICS"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    ENDDATE = Column(DateTime)
    REPORTSOURCE = Column(String(12, u'utf8_bin'))
    CURRENCYCODE = Column(String(12, u'utf8_bin'))
    GUARANTEEQUOTA = Column(Numeric(20, 6))
    QUOTATOOUTSIDE = Column(Numeric(20, 6))
    QUOTATOSUBSIDIARY = Column(Numeric(20, 6))
    ACTUALGUARANTEEAMOUNT = Column(Numeric(20, 6))
    ACTUALGUARANTEETOOUTSIDE = Column(Numeric(20, 6))
    ACTUALGUARANTEETOSUBSIDIARY = Column(Numeric(20, 6))
    ACCUMULATIVETOTALAMOUNT = Column(Numeric(20, 6))
    ACCUMULATIVETOOUTSIDE = Column(Numeric(20, 6))
    ACCUMULATIVETOSUBSIDIARY = Column(Numeric(20, 6))
    GUARANTEETOTALTONETASSETS = Column(Numeric(18, 4))
    GUARANTEETOSHAREHOLDER = Column(Numeric(20, 6))
    GUARANTEETOHIGHDEBTRATIOCO = Column(Numeric(20, 6))
    EXCEED50NETASSETSAMOUNT = Column(Numeric(20, 6))
    OVERDUEAMOUNT = Column(Numeric(20, 6))
    ILLEGALAMOUNT = Column(Numeric(20, 6))
    UPDATEID = Column(BigInteger, primary_key=True)
