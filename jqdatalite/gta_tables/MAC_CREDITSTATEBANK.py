

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_CREDITSTATEBANK(Base):
    __tablename__ = "MAC_CREDITSTATEBANK"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONTYPEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TOTALDEPOSIT = Column(Numeric(18, 4))
    CORPORATEDEPOSIT = Column(Numeric(18, 4))
    CORPORATEDEMANDDEPOSIT = Column(Numeric(18, 4))
    CORPORATETIMEDEPOSIT = Column(Numeric(18, 4))
    NOTICEDEPOSIT = Column(Numeric(18, 4))
    MARGINDEPOSIT = Column(Numeric(18, 4))
    PERSONALDEPOSIT = Column(Numeric(18, 4))
    SAVINGDEPOSIT = Column(Numeric(18, 4))
    DEMANDDEPOSIT = Column(Numeric(18, 4))
    TIMEDEPOSIT = Column(Numeric(18, 4))
    PERSONALMARGINDEPOSIT = Column(Numeric(18, 4))
    PERSONALSTRUCTUREDEPOSIT = Column(Numeric(18, 4))
    RURALDEPOSIT = Column(Numeric(18, 4))
    TEMPORARYDEPOSIT = Column(Numeric(18, 4))
    OTHERDEPOSIT = Column(Numeric(18, 4))
    FINANCEBOND = Column(Numeric(18, 4))
    CENTRALBANKBORROW = Column(Numeric(18, 4))
    BUSINESSSOURCE = Column(Numeric(18, 4))
    OTHERITEM = Column(Numeric(18, 4))
    TOTALFUNDSOURCE = Column(Numeric(18, 4))
    TOTALLOAN = Column(Numeric(18, 4))
    DOMESTICLOAN = Column(Numeric(18, 4))
    SHORTTERMLOAN = Column(Numeric(18, 4))
    MEDIUMLONGTERMLOAN = Column(Numeric(18, 4))
    FINANCELEASE = Column(Numeric(18, 4))
    BILLFINANCE = Column(Numeric(18, 4))
    ADVANCE = Column(Numeric(18, 4))
    OVERSEALOAN = Column(Numeric(18, 4))
    PORTFOLIOINVEST = Column(Numeric(18, 4))
    SECURITY = Column(Numeric(18, 4))
    OTHERSHARE = Column(Numeric(18, 4))
    RESERVEDEPOSIT = Column(Numeric(18, 4))
    BUSINESSUSE = Column(Numeric(18, 4))
    TOTALFUNDUSE = Column(Numeric(18, 4))
    DOMESTICDEPOSIT = Column(Numeric(18, 4))
    STRUCTUREDEPOSIT = Column(Numeric(18, 4))
    TREASURYTIMEDEPOSIT = Column(Numeric(18, 4))
    NONDEPOSITFINANCEDEPOSIT = Column(Numeric(18, 4))
    OVERSEADEPOSIT = Column(Numeric(18, 4))
    REPO = Column(Numeric(18, 4))
    REVERSEREPO = Column(Numeric(18, 4))
