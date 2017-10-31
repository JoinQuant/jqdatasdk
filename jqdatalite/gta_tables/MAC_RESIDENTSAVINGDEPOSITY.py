

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESIDENTSAVINGDEPOSITY(Base):
    __tablename__ = "MAC_RESIDENTSAVINGDEPOSITY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    SAVINGDEPOSIT = Column(Numeric(18, 4))
    TIMEDEPOSIT = Column(Numeric(18, 4))
    DEMANDDEPOSIT = Column(Numeric(18, 4))
    SAVINGDEPOSITINCREASE = Column(Numeric(18, 4))
    TIMEDEPOSITINCREASE = Column(Numeric(18, 4))
    DEMANDDEPOSITINCREASE = Column(Numeric(18, 4))
