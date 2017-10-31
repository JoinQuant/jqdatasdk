

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_RPT_RALATEDPARTY(Base):
    __tablename__ = "STK_RPT_RALATEDPARTY"

    INSTITUTIONID = Column(BigInteger, primary_key=True, nullable=False)
    SYMBOL = Column(String(12, u'utf8_bin'))
    DECLAREDATE = Column(DateTime, primary_key=True, nullable=False)
    REPORTSOURCE = Column(String(40, u'utf8_bin'), primary_key=True, nullable=False)
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    RALATEDPARTYID = Column(BigInteger)
    RALATEDPARTY = Column(String(200, u'utf8_bin'), primary_key=True, nullable=False)
    OTHERPARTYSIGN = Column(String(20, u'utf8_bin'))
    RELATIONID = Column(String(100, u'utf8_bin'))
    RELATION = Column(String(100, u'utf8_bin'))
    RELATIONSHIP = Column(String(100, u'utf8_bin'))
    ENTERPRISENATUREID = Column(String(100, u'utf8_bin'))
    ENTERPRISENATURE = Column(String(100, u'utf8_bin'))
    REGISTERCAPITAL = Column(Numeric(20, 2))
    CURRENCYCODE = Column(String(40, u'utf8_bin'))
    REGISTERADDRESS = Column(String(400, u'utf8_bin'))
    LEGALREPRESENTATIVE = Column(String(200, u'utf8_bin'))
    RESHAREHOLDINGRATIO = Column(Numeric(20, 2))
    REVOTERATIO = Column(Numeric(20, 2))
    COSHAREHOLDINGRATIO = Column(Numeric(20, 2))
    COVOTERATIO = Column(Numeric(20, 2))
    ORGANIZATIONCODE = Column(String(20, u'utf8_bin'))
