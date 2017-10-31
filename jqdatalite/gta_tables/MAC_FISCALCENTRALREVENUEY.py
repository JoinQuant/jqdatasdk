

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCALCENTRALREVENUEY(Base):
    __tablename__ = "MAC_FISCALCENTRALREVENUEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    REVENUEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    REVENUE = Column(Numeric(18, 4))
    CENTRALREVENUE = Column(Numeric(18, 4))
    LOCALREVENUE = Column(Numeric(18, 4))
