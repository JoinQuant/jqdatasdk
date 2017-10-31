

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREAGDP_INCOMEYEAR(Base):
    __tablename__ = "MAC_AREAGDP_INCOMEYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    GDPINCOME = Column(Numeric(18, 4))
    GDP_EMPLOYCOMPENSAT = Column(Numeric(18, 4))
    GDP_NETTAXONPRODUCT = Column(Numeric(18, 4))
    GDP_FADEPRECIAT = Column(Numeric(18, 4))
    GDP_OPERATSURPLUS = Column(Numeric(18, 4))
