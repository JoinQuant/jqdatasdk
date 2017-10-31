

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_AREA_ESTATE_BUILD(Base):
    __tablename__ = "INDU_AREA_ESTATE_BUILD"

    SGNMONTH = Column(String(14), primary_key=True, nullable=False)
    AREACODE = Column(String(20), primary_key=True, nullable=False)
    CONSTRUCTAREA = Column(Numeric(18, 4))
    NEWSTARTAREA = Column(Numeric(18, 4))
    COMPLETEAREA = Column(Numeric(18, 4))
    RESIDENTCONSTRUCTAREA = Column(Numeric(18, 4))
    RESIDENTNEWSTARTAREA = Column(Numeric(18, 4))
    RESIDENTCOMPLETEAREA = Column(Numeric(18, 4))
    OFFICECONSTRUCTAREA = Column(Numeric(18, 4))
    OFFICENEWSTARTAREA = Column(Numeric(18, 4))
    OFFICECOMPLETEAREA = Column(Numeric(18, 4))
    BUSINESSCONSTRUCTAREA = Column(Numeric(18, 4))
    BUSINESSNEWSTARTAREA = Column(Numeric(18, 4))
    BUSINESSCOMPLETEAREA = Column(Numeric(18, 4))
    CONSTRUCTAREAYOY = Column(Numeric(10, 4))
    NEWSTARTAREAYOY = Column(Numeric(10, 4))
    COMPLETEAREAYOY = Column(Numeric(10, 4))
    RESIDENTCONSTRUCTAREAYOY = Column(Numeric(10, 4))
    RESIDENTNEWSTARTAREAYOY = Column(Numeric(10, 4))
    RESIDENTCOMPLETEAREAYOY = Column(Numeric(10, 4))
    OFFICECONSTRUCTAREAYOY = Column(Numeric(10, 4))
    OFFICENEWSTARTAREAYOY = Column(Numeric(10, 4))
    OFFICECOMPLETEAREAYOY = Column(Numeric(10, 4))
    BUSINESSCONSTRUCTAREAYOY = Column(Numeric(10, 4))
    BUSINESSNEWSTARTAREAYOY = Column(Numeric(10, 4))
    BUSINESSCOMPLETEAREAYOY = Column(Numeric(10, 4))
