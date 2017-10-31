

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_NBANKRMBCREDIT(Base):
    __tablename__ = "MAC_NBANKRMBCREDIT"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    TOTALDEPOSITS = Column(Numeric(18, 4))
    DEPOSITSOFENTERPRISES = Column(Numeric(18, 4))
    ORGDEMANDDEPOSITS = Column(Numeric(18, 4))
    ORGTIMEDEPOSITS = Column(Numeric(18, 4))
    FISCALDEPOSITS = Column(Numeric(18, 4))
    GOVERNMENTDEPOSIT = Column(Numeric(18, 4))
    DEPOSITSOFTOWNS = Column(Numeric(18, 4))
    TOWNSDEMANDDEPOSITS = Column(Numeric(18, 4))
    TOWNSTIMEDEPOSITS = Column(Numeric(18, 4))
    RURALDEPOSIT = Column(Numeric(18, 4))
    OTHERDEPOSITS = Column(Numeric(18, 4))
    FINANCIALBOND = Column(Numeric(18, 4))
    INTER_BANKSACCOUNTIN = Column(Numeric(18, 4))
    M0 = Column(Numeric(18, 4))
    FINANCELIABILITY = Column(Numeric(18, 4))
    OWNEDCAPITAL = Column(Numeric(18, 4))
    OTHERITEMS = Column(Numeric(18, 4))
    FUNDSUSESINTOTAL = Column(Numeric(18, 4))
    TOTALLOANS = Column(Numeric(18, 4))
    SHORTTERMLOANS = Column(Numeric(18, 4))
    INDUSTRYLOAN = Column(Numeric(18, 4))
    COMMERCELOAN = Column(Numeric(18, 4))
    CONSTRUCTLOAN = Column(Numeric(18, 4))
    AGRICULTURELOAN = Column(Numeric(18, 4))
    TOWNSHIPCOMPANYLOANS = Column(Numeric(18, 4))
    FOREIGNFUNDEDCOMPANYLOANS = Column(Numeric(18, 4))
    PRIVATECOMPANYLOANS = Column(Numeric(18, 4))
    OTHERSHORTTERMLOANS = Column(Numeric(18, 4))
    MEDIUMANDLONGTERMLOANS = Column(Numeric(18, 4))
    OTHERLOANS = Column(Numeric(18, 4))
    PORTFOLIOINVESTMENT = Column(Numeric(18, 4))
    INTER_BANKSACCOUNTOUT = Column(Numeric(18, 4))
    GOLDANDSILVERPURCHASE = Column(Numeric(18, 4))
    FOREXPURCHASE = Column(Numeric(18, 4))
    TREASURYADVANCE = Column(Numeric(18, 4))
    INTERNATIONALFINANCEASSETS = Column(Numeric(18, 4))
    RMBUSEINTOTAL = Column(Numeric(18, 4))
