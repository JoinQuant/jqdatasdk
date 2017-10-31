

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PRODUCTTRADEVALUE(Base):
    __tablename__ = "MAC_PRODUCTTRADEVALUE"

    SGNMONTH = Column(String(14, u'utf8_bin'))
    DATASIGN = Column(String(4, u'utf8_bin'))
    PRODID = Column(BigInteger)
    UNITNAME = Column(String(40, u'utf8_bin'))
    EXPORTVOLUME = Column(Numeric(18, 4))
    EXPORTVALUE = Column(Numeric(18, 4))
    EXPORTVOLUMEYOY = Column(Numeric(10, 4))
    EXPORTVALUEYOY = Column(Numeric(10, 4))
    PERIODEXPORTVOLUME = Column(Numeric(18, 4))
    PERIODEXPORTVALUE = Column(Numeric(18, 4))
    IMPORTVOLUME = Column(Numeric(18, 4))
    IMPORTVALUE = Column(Numeric(18, 4))
    IMPORTVOLUMEYOY = Column(Numeric(10, 4))
    IMPORTVALUEYOY = Column(Numeric(10, 4))
    PERIODIMPORTVOLUME = Column(Numeric(18, 4))
    PERIODIMPORTVALUE = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
