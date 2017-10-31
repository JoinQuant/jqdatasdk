

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_ECOLOGICALENVIRO(Base):
    __tablename__ = "MAC_RES_ECOLOGICALENVIRO"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    FORESTAREA = Column(Numeric(18, 4))
    FORESTCOVERRATE = Column(Numeric(10, 4))
    TOTALAREAOFAFFORESTATION = Column(Numeric(18, 4))
    NUMBEROFNATURERESERVES = Column(Numeric(10, 2))
    AREAOFNATURERESERVES = Column(Numeric(18, 4))
    NUMBEROFDEMONSTRATIONZONE = Column(Numeric(10, 2))
    AREAOFWETLAND = Column(Numeric(18, 4))
