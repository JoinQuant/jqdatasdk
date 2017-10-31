

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_EMPLOYY(Base):
    __tablename__ = "MAC_AREA_EMPLOYY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    EMPLOY = Column(Numeric(18, 4))
    URBANEMPLOY = Column(Numeric(18, 4))
    URBANSTATEOWNED = Column(Numeric(18, 4))
    URBANCOLLECTIVE = Column(Numeric(18, 4))
    URBANSTOCKCOOPERATE = Column(Numeric(18, 4))
    URBANJOINTOWNERSHIP = Column(Numeric(18, 4))
    URBANLIMITED = Column(Numeric(18, 4))
    URBANSTOCK = Column(Numeric(18, 4))
    URBANPRIVATE = Column(Numeric(18, 4))
    URBANHKMACAOTAIWAN = Column(Numeric(18, 4))
    URBANFOREIGN = Column(Numeric(18, 4))
    URBANINDIVIDUAL = Column(Numeric(18, 4))
    RURALEMPLOY = Column(Numeric(18, 4))
    RURALTOWNSHIP = Column(Numeric(18, 4))
    RURALPRIVATE = Column(Numeric(18, 4))
    RURALINDIVIDUAL = Column(Numeric(18, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
