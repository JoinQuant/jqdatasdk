

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_LIABILITY(Base):
    __tablename__ = "MAC_LIABILITY"

    SGNQUATER = Column(String(28, u'utf8_bin'), primary_key=True, nullable=False)
    SGNBANK = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    FOREIGNASSETS = Column(Numeric(20, 4))
    RESERVEASSETS = Column(Numeric(20, 4))
    RESERVEDEPOSIT = Column(Numeric(20, 4))
    CASHINVAULT = Column(Numeric(20, 4))
    GOVERNMENTCLAIM = Column(Numeric(20, 4))
    CENTRALGOVERNMENTCLAIM = Column(Numeric(20, 4))
    CENTRALBANKBONDS = Column(Numeric(20, 4))
    OTHERCLAIM = Column(Numeric(20, 4))
    OTHERFINANCECLAIM = Column(Numeric(20, 4))
    NONFINANCECLAIM = Column(Numeric(20, 4))
    OTHERRESIDENTCLAIM = Column(Numeric(20, 4))
    OTHERASSETS = Column(Numeric(20, 4))
    TOTALASSETS = Column(Numeric(20, 4))
    NONFINANCELIABILITY = Column(Numeric(20, 4))
    BROADMONEY = Column(Numeric(20, 4))
    ENTERPRISEDEMANDDEPOSIT = Column(Numeric(20, 4))
    ENTERPRISETIMEDEPOSIT = Column(Numeric(20, 4))
    CITIZENSAVINGS = Column(Numeric(20, 4))
    EXCLUDEBROADMONEY = Column(Numeric(20, 4))
    TRANSFERDEPOSIT = Column(Numeric(20, 4))
    OTHERDEPOSIT = Column(Numeric(20, 4))
    OTHERNONFINANCIALLIABILITY = Column(Numeric(20, 4))
    CENTRALBANKLIABILITY = Column(Numeric(20, 4))
    OTHERDEPOSITLIABILITY = Column(Numeric(20, 4))
    OTHERFINANCELIABILITY = Column(Numeric(20, 4))
    OTHERBROADMONEYLIABILITY = Column(Numeric(20, 4))
    FOREIGNLIABILITY = Column(Numeric(20, 4))
    BONDISSUE = Column(Numeric(20, 4))
    PAIDINCAPITAL = Column(Numeric(20, 4))
    OTHERFINANCIALLIABILITY = Column(Numeric(20, 4))
    TOTALLIABILITY = Column(Numeric(20, 4))
