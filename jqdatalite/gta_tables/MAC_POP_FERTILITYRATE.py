

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_POP_FERTILITYRATE(Base):
    __tablename__ = "MAC_POP_FERTILITYRATE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AGE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    SAMPLINGFRACTION = Column(Numeric(10, 4))
    AVGWOMENOFCHILDBEARING = Column(Numeric(18, 4))
    BIRTHS = Column(Numeric(18, 4))
    FIRSTBIRTHS = Column(Numeric(18, 4))
    SECONDBIRTHS = Column(Numeric(18, 4))
    THIRDBIRTHS = Column(Numeric(18, 4))
    FERTILITYRATE = Column(Numeric(10, 4))
    FIRSTFERTILITYRATE = Column(Numeric(10, 4))
    SECONDFERTILITYRATE = Column(Numeric(10, 4))
    THIRDFERTILITYRATE = Column(Numeric(10, 4))
