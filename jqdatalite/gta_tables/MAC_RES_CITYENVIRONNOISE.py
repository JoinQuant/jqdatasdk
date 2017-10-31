

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_CITYENVIRONNOISE(Base):
    __tablename__ = "MAC_RES_CITYENVIRONNOISE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    NUMBEROFDEVELOPEDDISTRICTS = Column(Numeric(10, 2))
    AREAOFUPTONATIONALSTANDARD = Column(Numeric(18, 4))
