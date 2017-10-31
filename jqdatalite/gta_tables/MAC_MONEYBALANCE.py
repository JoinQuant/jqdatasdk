

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_MONEYBALANCE(Base):
    __tablename__ = "MAC_MONEYBALANCE"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    FOREIGNASSETS = Column(Numeric(18, 4))
    FOREIGNEXCHANGE = Column(Numeric(18, 4))
    MONEYGOLD = Column(Numeric(18, 4))
    OTHERFOREIGNASSETS = Column(Numeric(18, 4))
    GOVERNMENTCLAIM = Column(Numeric(18, 4))
    CENTRALGOVERNMENTCLAIM = Column(Numeric(18, 4))
    MONEYBANKCLAIM = Column(Numeric(18, 4))
    SPECIFICCLAIM = Column(Numeric(18, 4))
    NONMONEYCLAIM = Column(Numeric(18, 4))
    OTHERCLAIM = Column(Numeric(18, 4))
    OTHERFINANCECLAIM = Column(Numeric(18, 4))
    NONFINANCECLAIM = Column(Numeric(18, 4))
    OTHERASSETS = Column(Numeric(18, 4))
    TOTALASSETS = Column(Numeric(18, 4))
    RESERVEMONEY = Column(Numeric(18, 4))
    CURRENCYISSUE = Column(Numeric(18, 4))
    FINANCEDEPOSIT = Column(Numeric(18, 4))
    MONEYBANKDEPOSIT = Column(Numeric(18, 4))
    SPECIFICDEPOSIT = Column(Numeric(18, 4))
    OTHERDEPOSIT = Column(Numeric(18, 4))
    OTHERFINANCEDEPOSIT = Column(Numeric(18, 4))
    NONFINANCEDEPOSIT = Column(Numeric(18, 4))
    DEMANDDEPOSIT = Column(Numeric(18, 4))
    SAVINGDEPOSIT = Column(Numeric(18, 4))
    RESERVEDEPOSIT = Column(Numeric(18, 4))
    EXCLUDERESERVEMONEY = Column(Numeric(18, 4))
    BONDISSUE = Column(Numeric(18, 4))
    FOREIGNLIABILITY = Column(Numeric(18, 4))
    GOVERNMENTDEPOSIT = Column(Numeric(18, 4))
    CENTRALGOVERNMENTDEPOSIT = Column(Numeric(18, 4))
    OWNEDCAPITAL = Column(Numeric(18, 4))
    OTHERLIABILITY = Column(Numeric(18, 4))
    TOTALLIABILITY = Column(Numeric(18, 4))
