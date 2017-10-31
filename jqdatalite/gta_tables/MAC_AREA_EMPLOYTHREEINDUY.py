

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_EMPLOYTHREEINDUY(Base):
    __tablename__ = "MAC_AREA_EMPLOYTHREEINDUY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    EMPLOY = Column(Numeric(18, 4))
    EMPLOYPRIMARY = Column(Numeric(18, 4))
    EMPLOYSECONDARY = Column(Numeric(18, 4))
    EMPLOYTERTIARY = Column(Numeric(18, 4))
    EMPLOYPRIMARYRATIO = Column(Numeric(10, 4))
    EMPLOYSECONDARYRATIO = Column(Numeric(10, 4))
    EMPLOYTERTIARYRATIO = Column(Numeric(10, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
