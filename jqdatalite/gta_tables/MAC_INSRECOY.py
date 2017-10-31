

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSRECOY(Base):
    __tablename__ = "MAC_INSRECOY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SHORTNAME = Column(String(40, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'))
    LEGALOUTPREMIUMS = Column(Numeric(22, 4))
    LEGALAMORTIZEDFEE = Column(Numeric(22, 4))
    LEGALAMORTIZEDPAY = Column(Numeric(22, 4))
    NONLEGALOUTPREMIUMS = Column(Numeric(22, 4))
    NONLEGALAMORTIZEDFEE = Column(Numeric(22, 4))
    NONLEGALAMORTIZEDPAY = Column(Numeric(22, 4))
    NONLEGALOUTPREMIUMSPACT = Column(Numeric(22, 4))
    NONLEGALAMORTIZEDFEEPACT = Column(Numeric(22, 4))
    NONLEGALAMORTIZEDPAYPACT = Column(Numeric(22, 4))
    NONLEGALOUTPREMIUMSTEMP = Column(Numeric(22, 4))
    NONLEGALAMORTIZEDFEETEMP = Column(Numeric(22, 4))
    NONLEGALAMORTIZEDPAYTEMP = Column(Numeric(22, 4))
    NONLEGALINCOMES = Column(Numeric(22, 4))
    NONLEGALPAYMENTSFEE = Column(Numeric(22, 4))
    NONLEGALPAYMENTSPAY = Column(Numeric(22, 4))
    NONLEGALINCOMESPACT = Column(Numeric(22, 4))
    NONLEGALPAYMENTSFEEPACT = Column(Numeric(22, 4))
    NONLEGALPAYMENTSPAYPACT = Column(Numeric(22, 4))
    NONLEGALINCOMESTEMP = Column(Numeric(22, 4))
    NONLEGALPAYMENTSFEETEMP = Column(Numeric(22, 4))
    NONLEGALPAYMENTSPAYTEMP = Column(Numeric(22, 4))
