

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_ESTATE_INVEST(Base):
    __tablename__ = "INDU_ESTATE_INVEST"

    DECLAREDATE = Column(DateTime)
    SGNMONTH = Column(String(14), primary_key=True)
    INVEST = Column(Numeric(18, 4))
    STATEOWNED = Column(Numeric(18, 4))
    COMMODITYHOUSE = Column(Numeric(18, 4))
    LAND = Column(Numeric(18, 4))
    AUXILIARYPROJECT = Column(Numeric(18, 4))
    RESIDENT = Column(Numeric(18, 4))
    BELOW90HOUSE = Column(Numeric(18, 4))
    OVER144HOUSE = Column(Numeric(18, 4))
    AFFORDHOUSE = Column(Numeric(18, 4))
    VILLAFLAT = Column(Numeric(18, 4))
    OFFICE = Column(Numeric(18, 4))
    BUSINESS = Column(Numeric(18, 4))
    OTHERHOUSE = Column(Numeric(18, 4))
    CONSTRUCT = Column(Numeric(18, 4))
    INSTALL = Column(Numeric(18, 4))
    EQUIPMENTPURCHASE = Column(Numeric(18, 4))
    OTHEREXPENSE = Column(Numeric(18, 4))
    LANDPURCHASE = Column(Numeric(18, 4))
    PLANINVEST = Column(Numeric(18, 4))
    PLANCOMPLETEINVEST = Column(Numeric(18, 4))
    NEWFIXEDASSETS = Column(Numeric(18, 4))
    COMPLETEVALUE = Column(Numeric(18, 4))
    INVESTYOY = Column(Numeric(10, 4))
    STATEOWNEDYOY = Column(Numeric(10, 4))
    COMMODITYHOUSEYOY = Column(Numeric(10, 4))
    LANDYOY = Column(Numeric(10, 4))
    AUXILIARYPROJECTYOY = Column(Numeric(10, 4))
    RESIDENTYOY = Column(Numeric(10, 4))
    BELOW90HOUSEYOY = Column(Numeric(10, 4))
    OVER144HOUSEYOY = Column(Numeric(10, 4))
    AFFORDHOUSEYOY = Column(Numeric(10, 4))
    VILLAFLATYOY = Column(Numeric(10, 4))
    OFFICEYOY = Column(Numeric(10, 4))
    BUSINESSYOY = Column(Numeric(10, 4))
    OTHERHOUSEYOY = Column(Numeric(10, 4))
    CONSTRUCTYOY = Column(Numeric(10, 4))
    INSTALLYOY = Column(Numeric(10, 4))
    EQUIPMENTPURCHASEYOY = Column(Numeric(10, 4))
    OTHEREXPENSEYOY = Column(Numeric(10, 4))
    LANDPURCHASEYOY = Column(Numeric(10, 4))
    PLANINVESTYOY = Column(Numeric(10, 4))
    PLANCOMPLETEINVESTYOY = Column(Numeric(10, 4))
    NEWFIXEDASSETSYOY = Column(Numeric(10, 4))
    COMPLETEVALUEYOY = Column(Numeric(10, 4))
