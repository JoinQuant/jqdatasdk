

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_CURRENCYSTATE(Base):
    __tablename__ = "MAC_CURRENCYSTATE"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    FOREIGNASSETS = Column(Numeric(20, 4))
    FOREIGNEXCHANGE = Column(Numeric(20, 4))
    MONEYGOLD = Column(Numeric(20, 4))
    OTHERFOREIGNASSETS = Column(Numeric(20, 4))
    GOVERNMENTCLAIM = Column(Numeric(20, 4))
    CENTRALGOVERNMENTCLAIM = Column(Numeric(20, 4))
    OTHERCLAIM = Column(Numeric(20, 4))
    OTHERFINANCECLAIM = Column(Numeric(20, 4))
    NONFINANCECLAIM = Column(Numeric(20, 4))
    OTHERASSETS = Column(Numeric(20, 4))
    TOTALASSETS = Column(Numeric(20, 4))
    RESERVEMONEY = Column(Numeric(20, 4))
    CURRENCYISSUE = Column(Numeric(20, 4))
    FINANCEDEPOSIT = Column(Numeric(20, 4))
    OTHERDEPOSIT = Column(Numeric(20, 4))
    OTHERFINANCEDEPOSIT = Column(Numeric(20, 4))
    NONFINANCEDEPOSIT = Column(Numeric(20, 4))
    EXCLUDERESERVEFINANCEDEPOSIT = Column(Numeric(20, 4))
    DEMANDDEPOSIT = Column(Numeric(20, 4))
    BONDISSUE = Column(Numeric(20, 4))
    FOREIGNLIABILITY = Column(Numeric(20, 4))
    GOVERNMENTDEPOSIT = Column(Numeric(20, 4))
    OWNEDCAPITAL = Column(Numeric(20, 4))
    OTHERLIABILITY = Column(Numeric(20, 4))
    TOTALLIABILITY = Column(Numeric(20, 4))
