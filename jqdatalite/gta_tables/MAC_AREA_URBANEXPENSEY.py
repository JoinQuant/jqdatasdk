

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_URBANEXPENSEY(Base):
    __tablename__ = "MAC_AREA_URBANEXPENSEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    EXPENSE = Column(Numeric(18, 4))
    FOOD = Column(Numeric(18, 4))
    GRAIN = Column(Numeric(18, 4))
    STARCHTUBER = Column(Numeric(18, 4))
    BEANPRODUCT = Column(Numeric(18, 4))
    OILFAT = Column(Numeric(18, 4))
    MEAT = Column(Numeric(18, 4))
    EGG = Column(Numeric(18, 4))
    AQUATIC = Column(Numeric(18, 4))
    VEGETABLE = Column(Numeric(18, 4))
    CONDIMENT = Column(Numeric(18, 4))
    SUGAR = Column(Numeric(18, 4))
    TOBACCO = Column(Numeric(18, 4))
    LIQUOR = Column(Numeric(18, 4))
    FRUIT = Column(Numeric(18, 4))
    NUTS = Column(Numeric(18, 4))
    CAKE = Column(Numeric(18, 4))
    MILK = Column(Numeric(18, 4))
    OTHERFOOD = Column(Numeric(18, 4))
    DINING = Column(Numeric(18, 4))
    FOODPROCESSING = Column(Numeric(18, 4))
    CLOTHING = Column(Numeric(18, 4))
    GARMENT = Column(Numeric(18, 4))
    CLOTHINGMATERIAL = Column(Numeric(18, 4))
    SHOES = Column(Numeric(18, 4))
    TAILORING = Column(Numeric(18, 4))
    HOUSEEQUIPMENT = Column(Numeric(18, 4))
    DURABLECONSUMERGOODS = Column(Numeric(18, 4))
    DECORATION = Column(Numeric(18, 4))
    BEDARTICLE = Column(Numeric(18, 4))
    DAILYARTICLE = Column(Numeric(18, 4))
    FURNITUREMATERIAL = Column(Numeric(18, 4))
    HOUSESERVICE = Column(Numeric(18, 4))
    HEALTHCARE = Column(Numeric(18, 4))
    TRAFFICCOMMUNICATE = Column(Numeric(18, 4))
    TRAFFIC = Column(Numeric(18, 4))
    COMMUNICATE = Column(Numeric(18, 4))
    EDUCATECULTURE = Column(Numeric(18, 4))
    RECREATIONARTICLE = Column(Numeric(18, 4))
    EDUCATION = Column(Numeric(18, 4))
    RECREATIONSERVICE = Column(Numeric(18, 4))
    RESIDENT = Column(Numeric(18, 4))
    HOUSE = Column(Numeric(18, 4))
    HYDROELECTRICFUELS = Column(Numeric(18, 4))
    OTHEREXPENSE = Column(Numeric(18, 4))
    MISCELLANEOUSGOODS = Column(Numeric(18, 4))
    MISCELLANEOUSSERVICE = Column(Numeric(18, 4))
