

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FOREIGNCOOPERATEYEAR(Base):
    __tablename__ = "MAC_FOREIGNCOOPERATEYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    CONTRACTNUM = Column(Numeric(18, 4))
    PROJECTCONTRACTNUM = Column(Numeric(18, 4))
    LABOURCONTRACTNUM = Column(Numeric(18, 4))
    DESIGNCONTRACTNUM = Column(Numeric(18, 4))
    CONTRACTVALUE = Column(Numeric(18, 4))
    PROJECTVALUE = Column(Numeric(18, 4))
    LABOURVALUE = Column(Numeric(18, 4))
    DESIGNVALUE = Column(Numeric(18, 4))
    TURNOVER = Column(Numeric(18, 4))
    PROJECTTURNOVER = Column(Numeric(18, 4))
    LABOURTURNOVER = Column(Numeric(18, 4))
    DESIGNTURNOVER = Column(Numeric(18, 4))
    ABROADPERSONNUM = Column(Numeric(18, 4))
    PROJECTABROADPERSONNUM = Column(Numeric(18, 4))
    LABOURABROADPERSONNUM = Column(Numeric(18, 4))
    DISPATCHNUM = Column(Numeric(18, 4))
    PROJECTDISPATCHNUM = Column(Numeric(18, 4))
    LABOURDISPATCHNUM = Column(Numeric(18, 4))
