

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSCOLLEGEY(Base):
    __tablename__ = "MAC_INSCOLLEGEY"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    COLLEGENAME = Column(String(200, u'utf8_bin'))
    PHONENUMBER = Column(String(100, u'utf8_bin'))
    ADDRESS = Column(String(200, u'utf8_bin'))
    ZIPCODE = Column(String(20, u'utf8_bin'))
    DEPARTMENT = Column(String(200, u'utf8_bin'))
    STUDENTTOTAL = Column(BigInteger)
    STUDENTDOCTOR = Column(BigInteger)
    STUDENTMASTER = Column(BigInteger)
    STUDENTBACHELOR = Column(BigInteger)
    STUDENTASSOCIATE = Column(BigInteger)
    STUDENTTECHNICAL = Column(BigInteger)
    TEACHERTOTAL = Column(BigInteger)
    TEACHERPROFESSOR = Column(BigInteger)
    TEACHERASSOCIATEPROFESSOR = Column(BigInteger)
    TEACHERLECTURER = Column(BigInteger)
    TEACHERCOURSEASSISTANT = Column(BigInteger)
    UPDATEID = Column(BigInteger, primary_key=True)
