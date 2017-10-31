

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_OTHERDEPOSITBALANCE(Base):
    __tablename__ = "MAC_OTHERDEPOSITBALANCE"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    FOREIGNASSETS = Column(Numeric(18, 4))
    RESERVEASSETS = Column(Numeric(18, 4))
    RESERVEDEPOSIT = Column(Numeric(18, 4))
    CASHINVAULT = Column(Numeric(18, 4))
    GOVERNMENTCLAIM = Column(Numeric(18, 4))
    CENTRALGOVERNMENTCLAIM = Column(Numeric(18, 4))
    CENTRALBANKCLAIM = Column(Numeric(18, 4))
    OTHERCLAIM = Column(Numeric(18, 4))
    OTHERFINANCECLAIM = Column(Numeric(18, 4))
    NONFINANCECLAIM = Column(Numeric(18, 4))
    OTHERRESIDENTCLAIM = Column(Numeric(18, 4))
    OTHERASSETS = Column(Numeric(18, 4))
    TOTALASSETS = Column(Numeric(18, 4))
    NONFINANCELIABILITY = Column(Numeric(18, 4))
    NONFINANCEINCLUDEBROADMONEY = Column(Numeric(18, 4))
    CORPORATEDEMANDDEPOSIT = Column(Numeric(18, 4))
    CORPORATETIMEDEPOSIT = Column(Numeric(18, 4))
    PERSONALDEPOSIT = Column(Numeric(18, 4))
    EXCLUDEBROADMONEY = Column(Numeric(18, 4))
    TRANSFERDEPOSIT = Column(Numeric(18, 4))
    OTHERDEPOSIT = Column(Numeric(18, 4))
    OTHERNONFINANCELIABILITY = Column(Numeric(18, 4))
    CENTRALBANKLIABILITY = Column(Numeric(18, 4))
    OTHERDEPOSITLIABILITY = Column(Numeric(18, 4))
    OTHERFINANCELIABILITY = Column(Numeric(18, 4))
    INCLUDEBROADMONEY = Column(Numeric(18, 4))
    FOREIGNLIABILITY = Column(Numeric(18, 4))
    BONDISSUE = Column(Numeric(18, 4))
    PAIDINCAPITAL = Column(Numeric(18, 4))
    OTHERLIABILITY = Column(Numeric(18, 4))
    TOTALLIABILITY = Column(Numeric(18, 4))
