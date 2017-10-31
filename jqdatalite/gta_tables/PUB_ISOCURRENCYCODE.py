

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class PUB_ISOCURRENCYCODE(Base):
    __tablename__ = "PUB_ISOCURRENCYCODE"

    CURRENCYCODE = Column(String(6), primary_key=True)
    CURRENCYCODENUM = Column(String(6))
    CURRENCYNAME = Column(String(200))
    CURRENCYNAME_EN = Column(String(200))
