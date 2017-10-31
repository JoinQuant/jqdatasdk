

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSLAREAY(Base):
    __tablename__ = "MAC_INSLAREAY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SHORTNAME = Column(String(40, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'))
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    INCOMES = Column(Numeric(22, 4))
    PERSONALLIFE = Column(Numeric(22, 4))
    PERSONALORDINARYLIFE = Column(Numeric(22, 4))
    PERSONALDIVIDENDLIFE = Column(Numeric(22, 4))
    PERSONALINVESTMENTLINKED = Column(Numeric(22, 4))
    PERSONALMULTIPURPOSE = Column(Numeric(22, 4))
    PERSONALOTHERLIFE = Column(Numeric(22, 4))
    PERSONALACCIDENT = Column(Numeric(22, 4))
    PERSONALHEALTH = Column(Numeric(22, 4))
    GROUPLIFE = Column(Numeric(22, 4))
    GROUPORDINARYLIFE = Column(Numeric(22, 4))
    GROUPDIVIDENDLIFE = Column(Numeric(22, 4))
    GROUPINVESTMENTLINKED = Column(Numeric(22, 4))
    GROUPMULTIPURPOSE = Column(Numeric(22, 4))
    GROUPOTHERLIFE = Column(Numeric(22, 4))
    GROUPACCIDENT = Column(Numeric(22, 4))
    GROUPHEALTH = Column(Numeric(22, 4))
    POLICYNEW = Column(Numeric(22, 4))
    POLICYEFFECTIVE = Column(Numeric(22, 4))
    CHANNELSINCOMES = Column(Numeric(22, 4))
    CHANNELPERSONALAGENTS = Column(Numeric(22, 4))
    CHANNELCODIRECTSELL = Column(Numeric(22, 4))
    CHANNELPROAGENTS = Column(Numeric(22, 4))
    CHANNELBANKAGENTS = Column(Numeric(22, 4))
    CHANNELOTHERAGENTS = Column(Numeric(22, 4))
    CHANNELBROKERING = Column(Numeric(22, 4))
    PAYMENTS = Column(Numeric(22, 4))
    PERSONALPAYMENT = Column(Numeric(22, 4))
    PERSONALCASUALTIESMEDICAL = Column(Numeric(22, 4))
    PERSONALEXPIRES = Column(Numeric(22, 4))
    PERSONALANNUITY = Column(Numeric(22, 4))
    GROUPPAYMENT = Column(Numeric(22, 4))
    GROUPCASUALTIESMEDICAL = Column(Numeric(22, 4))
    GROUPEXPIRES = Column(Numeric(22, 4))
    GROUPANNUITY = Column(Numeric(22, 4))
    SURRENDERVALUE = Column(Numeric(22, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
