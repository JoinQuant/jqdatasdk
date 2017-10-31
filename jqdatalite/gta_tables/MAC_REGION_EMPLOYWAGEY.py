

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_EMPLOYWAGEY(Base):
    __tablename__ = "MAC_REGION_EMPLOYWAGEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    EMPLOY = Column(Numeric(20, 4))
    PRIVATEINDIVIDUALNUM = Column(Numeric(20, 4))
    UNEMPLOYNUM = Column(Numeric(20, 4))
    EMPLOYPRIMARY = Column(Numeric(20, 4))
    EMPLOYSECONDARY = Column(Numeric(20, 4))
    EMPLOYTERTIARY = Column(Numeric(20, 4))
    EMPLOYPRIMARYRATIO = Column(Numeric(10, 4))
    EMPLOYSECONDARYRATIO = Column(Numeric(10, 4))
    EMPLOYTERTIARYRATIO = Column(Numeric(10, 4))
    AVGSTAFF = Column(Numeric(20, 4))
    STAFFWAGE = Column(Numeric(20, 4))
    AVGSTAFFWAGE = Column(Numeric(20, 4))
