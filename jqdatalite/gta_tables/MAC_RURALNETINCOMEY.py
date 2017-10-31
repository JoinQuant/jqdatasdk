

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RURALNETINCOMEY(Base):
    __tablename__ = "MAC_RURALNETINCOMEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    REVENUE = Column(Numeric(18, 4))
    BASICINCOME = Column(Numeric(18, 4))
    WAGEINCOME = Column(Numeric(18, 4))
    COLLECTIVE = Column(Numeric(18, 4))
    ENTERPRISE = Column(Numeric(18, 4))
    TOWNSHIPENTERPRISE = Column(Numeric(18, 4))
    OTHERINCOME = Column(Numeric(18, 4))
    BUSINESSINCOME = Column(Numeric(18, 4))
    TRANSFERPROPERTYINCOME = Column(Numeric(18, 4))
    PROPERTYINCOME = Column(Numeric(18, 4))
    TRANSFERINCOME = Column(Numeric(18, 4))
    NETINCOME = Column(Numeric(18, 4))
    WAGENETINCOME = Column(Numeric(18, 4))
    BUSINESSNETINCOME = Column(Numeric(18, 4))
    FARMINGNETINCOME = Column(Numeric(18, 4))
    FORESTRYNETINCOME = Column(Numeric(18, 4))
    ANIMALHUSBANDRYNETINCOME = Column(Numeric(18, 4))
    FISHERYNETINCOME = Column(Numeric(18, 4))
    INDUSTRYNETINCOME = Column(Numeric(18, 4))
    GATHERINGHUNTINGNETINCOME = Column(Numeric(18, 4))
    CONSTRUCTNETINCOME = Column(Numeric(18, 4))
    TRAFFICNETINCOME = Column(Numeric(18, 4))
    WHOLESALENETINCOME = Column(Numeric(18, 4))
    CATERINGNETINCOME = Column(Numeric(18, 4))
    SERVICENETINCOME = Column(Numeric(18, 4))
    EDUCATECULTURENETINCOME = Column(Numeric(18, 4))
    OTHERNETINCOME = Column(Numeric(18, 4))
    TRANSFERPROPERTYNETINCOME = Column(Numeric(18, 4))
    PROPERTYNETINCOME = Column(Numeric(18, 4))
    TRANSFERNETINCOME = Column(Numeric(18, 4))
