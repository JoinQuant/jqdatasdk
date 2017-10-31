

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDU_URBANFIXEDPROJECTY(Base):
    __tablename__ = "MAC_INDU_URBANFIXEDPROJECTY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INDUSTRYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    CONSTRUCTPROJECTNUM = Column(Numeric(18, 4))
    STARTPROJECTNUM = Column(Numeric(18, 4))
    COMPLETEPROJECTNUM = Column(Numeric(18, 4))
    USERATE = Column(Numeric(10, 4))
