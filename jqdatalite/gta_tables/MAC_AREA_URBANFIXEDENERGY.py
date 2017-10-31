

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_URBANFIXEDENERGY(Base):
    __tablename__ = "MAC_AREA_URBANFIXEDENERGY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    ENERGY = Column(Numeric(18, 4))
    COALMINING = Column(Numeric(18, 4))
    PETROLEUMNATURAL = Column(Numeric(18, 4))
    PETROLEUMCOKING = Column(Numeric(18, 4))
    ELECTRICGASWATER = Column(Numeric(18, 4))
