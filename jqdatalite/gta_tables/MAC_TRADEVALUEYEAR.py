

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_TRADEVALUEYEAR(Base):
    __tablename__ = "MAC_TRADEVALUEYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    TOTALRMB = Column(Numeric(18, 4))
    EXPORTRMB = Column(Numeric(18, 4))
    IMPORTRMB = Column(Numeric(18, 4))
    BALANCERMB = Column(Numeric(18, 4))
    TOTAL = Column(Numeric(18, 4))
    EXPORT = Column(Numeric(18, 4))
    IMPORT = Column(Numeric(18, 4))
    BALANCE = Column(Numeric(18, 4))
