

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_RURALCASHEXPENSEQ(Base):
    __tablename__ = "MAC_AREA_RURALCASHEXPENSEQ"

    SGNQUARTER = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TOTALCASHINCOME = Column(Numeric(18, 4))
    WAGEINCOME = Column(Numeric(18, 4))
    BUSINESSINCOME = Column(Numeric(18, 4))
    FARMINGINCOME = Column(Numeric(18, 4))
    FORESTRYINCOME = Column(Numeric(18, 4))
    ANIMALHUSBANDRYINCOME = Column(Numeric(18, 4))
    FISHERYINCOME = Column(Numeric(18, 4))
    PROPERTYINCOME = Column(Numeric(18, 4))
    TRANSFERINCOME = Column(Numeric(18, 4))
    TOTALCASHEXPENSE = Column(Numeric(18, 4))
    PRODUCTEXPENSE = Column(Numeric(18, 4))
    BUSINESSEXPENSE = Column(Numeric(18, 4))
    AGRPRODUCTEXPENSE = Column(Numeric(18, 4))
    ANIMALHUSBANDRYEXPENSE = Column(Numeric(18, 4))
    PRODUCTASSET = Column(Numeric(18, 4))
    TAXEXPENSE = Column(Numeric(18, 4))
    CONSUMECASH = Column(Numeric(18, 4))
    FOOD = Column(Numeric(18, 4))
    CLOTHING = Column(Numeric(18, 4))
    RESIDENT = Column(Numeric(18, 4))
    HOUSEEQUIPMENT = Column(Numeric(18, 4))
    TRAFFICCOMMUNICATE = Column(Numeric(18, 4))
    EDUCATECULTURE = Column(Numeric(18, 4))
    HEALTHCARE = Column(Numeric(18, 4))
    OTHEREXPENSE = Column(Numeric(18, 4))
    PROPERTYEXPENSE = Column(Numeric(18, 4))
    TRANSFEREXPENSE = Column(Numeric(18, 4))
