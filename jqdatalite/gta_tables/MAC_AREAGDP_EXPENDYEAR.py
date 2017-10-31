

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREAGDP_EXPENDYEAR(Base):
    __tablename__ = "MAC_AREAGDP_EXPENDYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    GDPEXPEND = Column(Numeric(18, 4))
    GDP_FINCOMSUMEXPEND = Column(Numeric(18, 4))
    GDP_HOUSEHOLDEXPEND = Column(Numeric(18, 4))
    GDP_RUARLHOLDEXPEND = Column(Numeric(18, 4))
    GDP_UHOUSEHOLDEXPEND = Column(Numeric(18, 4))
    GDP_GOVEXPEND = Column(Numeric(18, 4))
    GDP_GROSSCAPITALFORMAT = Column(Numeric(18, 4))
    GDP_GROSSFIXEDFORMAT = Column(Numeric(18, 4))
    GDP_GROSSINVENTORYFORMAT = Column(Numeric(18, 4))
    GDP_NETEXPORT = Column(Numeric(18, 4))
    FINALCOMSUMRATE = Column(Numeric(10, 4))
    CAPITALFORMATRATE = Column(Numeric(10, 4))
