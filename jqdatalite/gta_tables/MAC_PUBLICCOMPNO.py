

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PUBLICCOMPNO(Base):
    __tablename__ = "MAC_PUBLICCOMPNO"

    SGNYEAR = Column(String(16, u'utf8_bin'), primary_key=True)
    NATIONALPUBLICCOMPANY = Column(Integer)
    SHANGHAIPUBLICCOMPANY = Column(Integer)
    SHENZHENPUBLICCOMPANY = Column(Integer)
    ONLYISSUEDA = Column(Integer)
    ONLYISSUEDB = Column(Integer)
    BOTHAANDB = Column(Integer)
    BOTHAANDH = Column(Integer)
