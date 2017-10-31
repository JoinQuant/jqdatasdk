

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSSTAFFSY(Base):
    __tablename__ = "MAC_INSSTAFFSY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SHORTNAME = Column(String(40, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'))
    TOTALNUMBER = Column(Numeric(20, 0))
    MALE = Column(Numeric(20, 0))
    FEMAL = Column(Numeric(20, 0))
    STAFF = Column(Numeric(20, 0))
    MANAGER = Column(Numeric(20, 0))
    SALER = Column(Numeric(20, 0))
    DEGREEDOCTOR = Column(Numeric(20, 0))
    DEGREEMASTER = Column(Numeric(20, 0))
    DEGREEBACHELOR = Column(Numeric(20, 0))
    DEGREEASSOCIATE = Column(Numeric(20, 0))
    DEGREETECHNICAL = Column(Numeric(20, 0))
    PROHIGH = Column(Numeric(20, 0))
    PROMIDDLE = Column(Numeric(20, 0))
    PROLOW = Column(Numeric(20, 0))
    AGEUNDER35 = Column(Numeric(20, 0))
    AGE36TO45 = Column(Numeric(20, 0))
    AGEOVER46 = Column(Numeric(20, 0))
