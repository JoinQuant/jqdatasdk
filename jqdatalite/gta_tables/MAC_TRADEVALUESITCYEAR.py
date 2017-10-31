

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_TRADEVALUESITCYEAR(Base):
    __tablename__ = "MAC_TRADEVALUESITCYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    SITCID = Column(BigInteger)
    EXPORT = Column(Numeric(18, 4))
    IMPORT = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
