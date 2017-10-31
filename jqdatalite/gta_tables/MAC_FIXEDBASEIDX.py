

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FIXEDBASEIDX(Base):
    __tablename__ = "MAC_FIXEDBASEIDX"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    ITEMID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    FIXEDBASEIDX = Column(Numeric(10, 4))
