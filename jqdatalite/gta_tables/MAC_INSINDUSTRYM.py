

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSINDUSTRYM(Base):
    __tablename__ = "MAC_INSINDUSTRYM"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(2, u'utf8_bin'), primary_key=True, nullable=False)
    INCOMES = Column(Numeric(22, 4))
    INCOMEPROPERTY = Column(Numeric(22, 4))
    INCOMEPERSONAL = Column(Numeric(22, 4))
    INCOMELIFE = Column(Numeric(22, 4))
    INCOMEHEALTH = Column(Numeric(22, 4))
    INCOMEACCIDENT = Column(Numeric(22, 4))
    INCOMEINVESTNEWFEES = Column(Numeric(22, 4))
    INCOMELINKEDACCOUNTFEES = Column(Numeric(22, 4))
    ANNUITYPAYMENT = Column(Numeric(22, 4))
    PAYMENTS = Column(Numeric(22, 4))
    PAYMENTPROPERTY = Column(Numeric(22, 4))
    PAYMENTPERSONAL = Column(Numeric(22, 4))
    PAYMENTLIFE = Column(Numeric(22, 4))
    PAYMENTHEALTH = Column(Numeric(22, 4))
    PAYMENTACCIDENT = Column(Numeric(22, 4))
    EXPENSES = Column(Numeric(22, 4))
    BANKDEPOSITS = Column(Numeric(22, 4))
    INVESTMENTS = Column(Numeric(22, 4))
    STOCK = Column(Numeric(22, 4))
    BOND = Column(Numeric(22, 4))
    FUND = Column(Numeric(22, 4))
    TOTALASSETS = Column(Numeric(22, 4))
    ANNUITYENTRUSTED = Column(Numeric(22, 4))
    ANNUITYINVESTED = Column(Numeric(22, 4))
