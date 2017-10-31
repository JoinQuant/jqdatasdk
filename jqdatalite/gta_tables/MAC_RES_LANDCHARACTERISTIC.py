

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RES_LANDCHARACTERISTIC(Base):
    __tablename__ = "MAC_RES_LANDCHARACTERISTIC"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    TOTALLANDAREA = Column(Numeric(18, 4))
    MOUNTAINS = Column(Numeric(18, 4))
    PLATEAUS = Column(Numeric(18, 4))
    BASINS = Column(Numeric(18, 4))
    PLAINS = Column(Numeric(18, 4))
    HILLS = Column(Numeric(18, 4))
    BELOW500M = Column(Numeric(18, 4))
    BETWEEN500AND1000M = Column(Numeric(18, 4))
    BETWEEN1000AND2000M = Column(Numeric(18, 4))
    BETWEEN2000AND3000M = Column(Numeric(18, 4))
    ABOVE3000M = Column(Numeric(18, 4))
    CULTIVATEDLAND = Column(Numeric(18, 4))
    FORESTS = Column(Numeric(18, 4))
    WATERAREAINLAND = Column(Numeric(18, 4))
    AREAOFGRASSLAND = Column(Numeric(18, 4))
    OTHERS = Column(Numeric(18, 4))
