

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class BD_LISTEDCOINFO(Base):
    __tablename__ = "BD_LISTEDCOINFO"

    ORGID = Column(BigInteger, primary_key=True)
    FULLNAME = Column(String(200))
    SHORTNAME = Column(String(100))
    LISTSIGN = Column(SmallInteger)
    OWNSHIPID = Column(String(12))
    OWNSHIP = Column(String(100))
    ESTABLISHDATE = Column(DateTime)
    LEGALREPRESENTATIVE = Column(String(100))
    REGISTERADDRESS = Column(String(400))
    OFFICEADDRESS = Column(String(400))
    ZIPCODE = Column(String(12))
    REGISTEREDCAPITAL = Column(BigInteger)
    CURRENCYCODE = Column(String(6))
    CURRENCY = Column(String(100))
    TELSECRETARY = Column(String(100))
    FAXSECRETARY = Column(String(100))
    CHANGEDATE = Column(DateTime)
