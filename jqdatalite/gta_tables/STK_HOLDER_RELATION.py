

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_HOLDER_RELATION(Base):
    __tablename__ = "STK_HOLDER_RELATION"

    INSTITUTIONID = Column(Numeric(20, 0))
    SYMBOL = Column(String(20, u'utf8_bin'))
    ENDDATE = Column(DateTime)
    RELATIONSHIPID = Column(String(40, u'utf8_bin'))
    RELATIONSHIP = Column(String(200, u'utf8_bin'))
    FULLNAME1 = Column(String(200, u'utf8_bin'))
    FULLNAME1ISSHAREHOLDER = Column(String(2, u'utf8_bin'))
    FULLNAME2 = Column(String(200, u'utf8_bin'))
    FULLNAME2ISSHAREHOLDER = Column(String(2, u'utf8_bin'))
    SHAREHOLDINGRATIO = Column(Numeric(10, 2))
    SPECIALEXPLANATION = Column(String(4000, u'utf8_bin'))
    RELATIONDETAILED = Column(String(400, u'utf8_bin'))
    UPDATEID = Column(BigInteger, primary_key=True)
