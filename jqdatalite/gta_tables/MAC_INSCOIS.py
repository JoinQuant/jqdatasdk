

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSCOIS(Base):
    __tablename__ = "MAC_INSCOIS"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SHORTNAME = Column(String(40, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'))
    OPERATINGREVENUE = Column(Numeric(22, 4))
    EARNEDPREMIUM = Column(Numeric(22, 4))
    INSURANCEREVENUE = Column(Numeric(22, 4))
    REINSURANCEREVENUE = Column(Numeric(22, 4))
    LESSREPREMIUMS = Column(Numeric(22, 4))
    EXTRACTUNEXPIREDRESERVES = Column(Numeric(22, 4))
    BANKINTERESTINCOME = Column(Numeric(22, 4))
    COMMISSIONINCOME = Column(Numeric(22, 4))
    INVESTMENTINCOME = Column(Numeric(22, 4))
    COMPANYINESTMENTINCOME = Column(Numeric(22, 4))
    FAIRVALUEGAINS = Column(Numeric(22, 4))
    EXCHANGEGAINS = Column(Numeric(22, 4))
    OTHEREOPERATINGINCOME = Column(Numeric(22, 4))
    OPERATINGEXPENSE = Column(Numeric(22, 4))
    SURRENDERVALUE = Column(Numeric(22, 4))
    PAYMENTS = Column(Numeric(22, 4))
    LESSAMORTIZEDPAYMENTS = Column(Numeric(22, 4))
    EXTRACTINSURERESERVES = Column(Numeric(22, 4))
    LESSAMORTIZEDRESERVES = Column(Numeric(22, 4))
    POLICYDIVIDENDEXPENSE = Column(Numeric(22, 4))
    REINSURANCEFEE = Column(Numeric(22, 4))
    SALESTAX = Column(Numeric(22, 4))
    COMMISSIONFEE = Column(Numeric(22, 4))
    EXPENSES = Column(Numeric(22, 4))
    LESSAMORTIZEDFEE = Column(Numeric(22, 4))
    OTHEROPERATINGCOST = Column(Numeric(22, 4))
    ASSETIMPAIRMENT = Column(Numeric(22, 4))
    OPERATINGPROFIT = Column(Numeric(22, 4))
    NONOPERATINGINCOME = Column(Numeric(22, 4))
    LESSNONOPERATINGEXPENSE = Column(Numeric(22, 4))
    PROFITBEFORETAX = Column(Numeric(22, 4))
    LESSINCOMETAX = Column(Numeric(22, 4))
    NETPROFIT = Column(Numeric(22, 4))
    OWNERSPROFIT = Column(Numeric(22, 4))
    MINORITYPROFIT = Column(Numeric(22, 4))
    EPS = Column(Numeric(22, 4))
    BASICEPS = Column(Numeric(22, 4))
    DILUTEDEPS = Column(Numeric(22, 4))
