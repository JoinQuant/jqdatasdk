

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class INDU_ESTATE_FUNDSOURCE(Base):
    __tablename__ = "INDU_ESTATE_FUNDSOURCE"

    SGNMONTH = Column(String(14), primary_key=True)
    TOTALSOURCE = Column(Numeric(18, 4))
    FUNDBALANCE = Column(Numeric(18, 4))
    CAPITALSOURCE = Column(Numeric(18, 4))
    STATEBUDGET = Column(Numeric(18, 4))
    DOMESTICLOAN = Column(Numeric(18, 4))
    BOND = Column(Numeric(18, 4))
    FOREIGNINVEST = Column(Numeric(18, 4))
    FDI = Column(Numeric(18, 4))
    SELFRAISEDFUND = Column(Numeric(18, 4))
    ENTERPRISEFUND = Column(Numeric(18, 4))
    OTHERFUND = Column(Numeric(18, 4))
    FRONTMONEY = Column(Numeric(18, 4))
    PERSONALMORTGAGELOAN = Column(Numeric(18, 4))
    VARIOUSDUE = Column(Numeric(18, 4))
    PROJECTFUND = Column(Numeric(18, 4))
    EQUIPMENTFUND = Column(Numeric(18, 4))
    TOTALSOURCEYOY = Column(Numeric(10, 4))
    FUNDBALANCEYOY = Column(Numeric(10, 4))
    CAPITALSOURCEYOY = Column(Numeric(10, 4))
    STATEBUDGETYOY = Column(Numeric(10, 4))
    DOMESTICLOANYOY = Column(Numeric(10, 4))
    BONDYOY = Column(Numeric(10, 4))
    FOREIGNINVESTYOY = Column(Numeric(10, 4))
    FDIYOY = Column(Numeric(10, 4))
    SELFRAISEDFUNDYOY = Column(Numeric(10, 4))
    ENTERPRISEFUNDYOY = Column(Numeric(10, 4))
    OTHERFUNDYOY = Column(Numeric(10, 4))
    FRONTMONEYYOY = Column(Numeric(10, 4))
    PERSONALMORTGAGELOANYOY = Column(Numeric(10, 4))
    VARIOUSDUEYOY = Column(Numeric(10, 4))
    PROJECTFUNDYOY = Column(Numeric(10, 4))
    EQUIPMENTFUNDYOY = Column(Numeric(10, 4))
