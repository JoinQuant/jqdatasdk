

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_ENVIRONMENTY(Base):
    __tablename__ = "MAC_REGION_ENVIRONMENTY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    TREATPOLLUTINVEST = Column(Numeric(20, 4))
    INFRASTRUCTUREINVEST = Column(Numeric(20, 4))
    UTILIZEWASTE = Column(Numeric(20, 4))
    WASTEWATERDISCHARGE = Column(Numeric(20, 4))
    WASTEWATERSTANDARD = Column(Numeric(20, 4))
    SULPHURDIOXIDEREMOVE = Column(Numeric(20, 4))
    SULPHURDIOXIDEEMISSION = Column(Numeric(20, 4))
    SOOTREMOVE = Column(Numeric(20, 4))
    SOOTDISCHARGE = Column(Numeric(20, 4))
    UTILIZEWASTERATIO = Column(Numeric(10, 4))
    WASTEWATERRATIO = Column(Numeric(10, 4))
    WASTETREATMENTRATIO = Column(Numeric(10, 4))
