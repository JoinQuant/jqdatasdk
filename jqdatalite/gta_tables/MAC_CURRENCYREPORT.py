

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_CURRENCYREPORT(Base):
    __tablename__ = "MAC_CURRENCYREPORT"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    NETFOREIGNASSETS = Column(Numeric(18, 4))
    DOMECTICCREDIT = Column(Numeric(18, 4))
    NETONGOVERNMENTCLAIMS = Column(Numeric(18, 4))
    NONFINANCECLAIM = Column(Numeric(18, 4))
    OTHERSPECIFICCLAIM = Column(Numeric(18, 4))
    OTHERFINANCECLAIM = Column(Numeric(18, 4))
    M2 = Column(Numeric(18, 4))
    M1 = Column(Numeric(18, 4))
    M0 = Column(Numeric(18, 4))
    DEMANDDEPOSIT = Column(Numeric(18, 4))
    QUASIMONEY = Column(Numeric(18, 4))
    TIMEDEPOSIT = Column(Numeric(18, 4))
    PERSONALSAVINGDEPOSIT = Column(Numeric(18, 4))
    OTHERDEPOSITS = Column(Numeric(18, 4))
    FOREIGNSAVINGS = Column(Numeric(18, 4))
    BONDS = Column(Numeric(18, 4))
    CENTRALBANKBONDS = Column(Numeric(18, 4))
    PAIDINCAPITAL = Column(Numeric(18, 4))
    OTHERITEMS = Column(Numeric(18, 4))
