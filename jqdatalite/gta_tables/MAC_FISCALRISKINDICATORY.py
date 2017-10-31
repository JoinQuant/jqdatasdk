

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCALRISKINDICATORY(Base):
    __tablename__ = "MAC_FISCALRISKINDICATORY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    DEBTSERVICERATIO = Column(Numeric(10, 4))
    LIABILITYRATIO = Column(Numeric(10, 4))
    FOREIGNDEBTRATIO = Column(Numeric(10, 4))
