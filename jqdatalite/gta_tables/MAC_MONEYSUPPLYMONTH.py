

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MONEYSUPPLYMONTH(Base):
    __tablename__ = "MAC_MONEYSUPPLYMONTH"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    M2 = Column(Numeric(18, 4))
    M1 = Column(Numeric(18, 4))
    M0 = Column(Numeric(18, 4))
    CORPORATEDEMANDDEPOSIT = Column(Numeric(18, 4))
    QUASIMONEY = Column(Numeric(18, 4))
    CORPORATETIMEDEPOSIT = Column(Numeric(18, 4))
    PERSONALDEPOSIT = Column(Numeric(18, 4))
    OTHERDEPOSIT = Column(Numeric(18, 4))
    M2YOY = Column(Numeric(10, 4))
    M1YOY = Column(Numeric(10, 4))
    M0YOY = Column(Numeric(10, 4))
    CORPORATEDEMANDDEPOSITYOY = Column(Numeric(10, 4))
    QUASIMONEYYOY = Column(Numeric(10, 4))
    CORPORATETIMEDEPOSITYOY = Column(Numeric(10, 4))
    PERSONALDEPOSITYOY = Column(Numeric(10, 4))
    OTHERDEPOSITYOY = Column(Numeric(10, 4))
