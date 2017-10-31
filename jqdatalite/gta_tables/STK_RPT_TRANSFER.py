

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_RPT_TRANSFER(Base):
    __tablename__ = "STK_RPT_TRANSFER"

    INSTITUTIONID = Column(BigInteger, primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    RALATEDPARTYID = Column(BigInteger)
    RALATEDPARTY = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    RELATIONID = Column(String(100, u'utf8_bin'))
    RELATION = Column(String(100, u'utf8_bin'))
    RELATIONSHIP = Column(String(200, u'utf8_bin'))
    ACCOUNTTITLEID = Column(String(100, u'utf8_bin'), primary_key=True, nullable=False)
    ACCOUNTTITLE = Column(String(100, u'utf8_bin'))
    TRANSACTIONACCOUNT = Column(String(100, u'utf8_bin'))
    TRANSACTIONRANK = Column(BigInteger, primary_key=True, nullable=False)
    BEGINNINGBANLANCE = Column(Numeric(20, 2))
    ENDBANLANCE = Column(Numeric(20, 2))
    ENDBANLANCERATIO = Column(Numeric(10, 4))
    CURRENCYCODE = Column(String(40, u'utf8_bin'))
