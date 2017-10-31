

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_EMPLOYY(Base):
    __tablename__ = "MAC_EMPLOYY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    POPULATION = Column(Numeric(18, 4))
    EMPLOY = Column(Numeric(18, 4))
    EMPLOYPRIMARY = Column(Numeric(18, 4))
    EMPLOYSECONDARY = Column(Numeric(18, 4))
    EMPLOYTERTIARY = Column(Numeric(18, 4))
    EMPLOYPRIMARYRATIO = Column(Numeric(10, 4))
    EMPLOYSECONDARYRATIO = Column(Numeric(10, 4))
    EMPLOYTERTIARYRATIO = Column(Numeric(10, 4))
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
    RURALPRIVATE = Column(Numeric(18, 4))
    RURALINDIVIDUAL = Column(Numeric(18, 4))
    STAFF = Column(Numeric(18, 4))
    STAFFSTATEOWNED = Column(Numeric(18, 4))
    STAFFCOLLECTIVE = Column(Numeric(18, 4))
    STAFFOTHER = Column(Numeric(18, 4))
    UNEMPLOYNUM = Column(Numeric(18, 4))
    URUR = Column(Numeric(10, 4))
