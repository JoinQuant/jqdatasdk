

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SALE_DOMESTICTRADE(Base):
    __tablename__ = "MAC_SALE_DOMESTICTRADE"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    AREACODE = Column(String(20, u'utf8_bin'))
    INDUSTRYID = Column(String(20, u'utf8_bin'))
    ENTERPRISENUM = Column(Numeric(18, 4))
    EMPLOYNUM = Column(Numeric(18, 4))
    PURCHASES = Column(Numeric(18, 4))
    IMPORTS = Column(Numeric(18, 4))
    SALES = Column(Numeric(18, 4))
    EXPORTS = Column(Numeric(18, 4))
    WHOLESALE = Column(Numeric(18, 4))
    RETAIL = Column(Numeric(18, 4))
    INVENTORY = Column(Numeric(18, 4))
    RETAILAREA = Column(Numeric(18, 4))
    BUSINESSREVENUE = Column(Numeric(18, 4))
    HOTELROOMS = Column(Numeric(18, 4))
    MEALS = Column(Numeric(18, 4))
    SALESREVENUE = Column(Numeric(18, 4))
    ROOMSNUM = Column(Numeric(18, 4))
    BEDSNUM = Column(Numeric(18, 4))
    CATERINGAREA = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
