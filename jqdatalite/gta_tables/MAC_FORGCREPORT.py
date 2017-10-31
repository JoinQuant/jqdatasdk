

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FORGCREPORT(Base):
    __tablename__ = "MAC_FORGCREPORT"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    SGNBANK = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    FOREIGNASSETS = Column(Numeric(18, 4))
    RESERVEASSETS = Column(Numeric(18, 4))
    RESERVEDEPOSIT = Column(Numeric(18, 4))
    CASHINVAULT = Column(Numeric(18, 4))
    CENTRALBANKBONDS = Column(Numeric(18, 4))
    GOVERNMENTCLAIM = Column(Numeric(18, 4))
    CENTRALGOVERNMENTCLAIM = Column(Numeric(18, 4))
    NONFINANCECLAIM = Column(Numeric(18, 4))
    OTHERSPECIFICCLAIM = Column(Numeric(18, 4))
    OTHERFINANCECLAIM = Column(Numeric(18, 4))
    OTHERASSETS = Column(Numeric(18, 4))
    TOTALASSETS = Column(Numeric(18, 4))
    NONFINANCELIABILITY = Column(Numeric(18, 4))
    DEMANDDEPOSIT = Column(Numeric(18, 4))
    CORPORATETIMEDEPOSIT = Column(Numeric(18, 4))
    PERSONALSAVINGDEPOSIT = Column(Numeric(18, 4))
    OTHERDEPOSITS = Column(Numeric(18, 4))
    FOREIGNSAVINGS = Column(Numeric(18, 4))
    CENTRALBANKLIABILITY = Column(Numeric(18, 4))
    OTHERDEPOSITLIABILITY = Column(Numeric(18, 4))
    OTHERFINANCELIABILITY = Column(Numeric(18, 4))
    OTHERBROADMONEYLIABILITY = Column(Numeric(18, 4))
    FOREIGNLIABILITY = Column(Numeric(18, 4))
    BONDS = Column(Numeric(18, 4))
    PAIDINCAPITAL = Column(Numeric(18, 4))
    OTHERLIABILITIES = Column(Numeric(18, 4))
    TOTALLIABILITIES = Column(Numeric(18, 4))
