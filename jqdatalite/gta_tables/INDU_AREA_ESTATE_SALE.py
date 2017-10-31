

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AREA_ESTATE_SALE(Base):
    __tablename__ = "INDU_AREA_ESTATE_SALE"

    SGNMONTH = Column(String(14), primary_key=True, nullable=False)
    AREACODE = Column(String(20), primary_key=True, nullable=False)
    SALEAREA = Column(Numeric(18, 4))
    READYHOUSEAREA = Column(Numeric(18, 4))
    FORWARDHOUSEAREA = Column(Numeric(18, 4))
    RESIDENTAREA = Column(Numeric(18, 4))
    RESIDENTREADYAREA = Column(Numeric(18, 4))
    RESIDENTFORWARDAREA = Column(Numeric(18, 4))
    OFFICEAREA = Column(Numeric(18, 4))
    OFFICEREADYAREA = Column(Numeric(18, 4))
    OFFICEFORWARDAREA = Column(Numeric(18, 4))
    BUSINESSAREA = Column(Numeric(18, 4))
    BUSINESSREADYAREA = Column(Numeric(18, 4))
    BUSINESSFORWARDAREA = Column(Numeric(18, 4))
    SALEVALUE = Column(Numeric(18, 4))
    RESIDENTVALUE = Column(Numeric(18, 4))
    OFFICEVALUE = Column(Numeric(18, 4))
    BUSINESSVALUE = Column(Numeric(18, 4))
    FORSALEAREA = Column(Numeric(18, 4))
    RESIDENTFORSALEAREA = Column(Numeric(18, 4))
    OFFICEFORSALEAREA = Column(Numeric(18, 4))
    BUSINESSFORSALEAREA = Column(Numeric(18, 4))
    SALEAREAYOY = Column(Numeric(10, 4))
    READYHOUSEAREAYOY = Column(Numeric(10, 4))
    FORWARDHOUSEAREAYOY = Column(Numeric(10, 4))
    RESIDENTAREAYOY = Column(Numeric(10, 4))
    RESIDENTREADYAREAYOY = Column(Numeric(10, 4))
    RESIDENTFORWARDAREAYOY = Column(Numeric(10, 4))
    OFFICEAREAYOY = Column(Numeric(10, 4))
    OFFICEREADYAREAYOY = Column(Numeric(10, 4))
    OFFICEFORWARDAREAYOY = Column(Numeric(10, 4))
    BUSINESSAREAYOY = Column(Numeric(10, 4))
    BUSINESSREADYAREAYOY = Column(Numeric(10, 4))
    BUSINESSFORWARDAREAYOY = Column(Numeric(10, 4))
    SALEVALUEYOY = Column(Numeric(10, 4))
    RESIDENTVALUEYOY = Column(Numeric(10, 4))
    OFFICEVALUEYOY = Column(Numeric(10, 4))
    BUSINESSVALUEYOY = Column(Numeric(10, 4))
    FORSALEAREAYOY = Column(Numeric(10, 4))
    RESIDENTFORSALEAREAYOY = Column(Numeric(10, 4))
    OFFICEFORSALEAREAYOY = Column(Numeric(10, 4))
    BUSINESSFORSALEAREAYOY = Column(Numeric(10, 4))
