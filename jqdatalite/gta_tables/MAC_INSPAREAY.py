

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INSPAREAY(Base):
    __tablename__ = "MAC_INSPAREAY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SHORTNAME = Column(String(40, u'utf8_bin'))
    FULLNAME = Column(String(200, u'utf8_bin'))
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    INCOMES = Column(Numeric(22, 4))
    INCOMEENTERPRISE = Column(Numeric(22, 4))
    INCOMEFAMILY = Column(Numeric(22, 4))
    INCOMEMOTORVEHICLE = Column(Numeric(22, 4))
    INCOMELIABILITY = Column(Numeric(22, 4))
    INCOMEPROJECT = Column(Numeric(22, 4))
    INCOMEFREIGHT = Column(Numeric(22, 4))
    INCOMESHIP = Column(Numeric(22, 4))
    INCOMECREDIT = Column(Numeric(22, 4))
    INCOMEGUARANTEE = Column(Numeric(22, 4))
    INCOMECREDITGUARANTEE = Column(Numeric(22, 4))
    INCOMESPECIALRISKS = Column(Numeric(22, 4))
    INCOMEFARM = Column(Numeric(22, 4))
    INCOMESHORTTIMEHEALTH = Column(Numeric(22, 4))
    INCOMEACCIDENT = Column(Numeric(22, 4))
    INCOMEOTHER = Column(Numeric(22, 4))
    INSUREDSAVINGS = Column(Numeric(22, 4))
    INSUREDINVESTMENT = Column(Numeric(22, 4))
    SAVINGSINVESTMENT = Column(Numeric(22, 4))
    PAYMENTS = Column(Numeric(22, 4))
    PAYMENTENTERPRISE = Column(Numeric(22, 4))
    PAYMENTFAMILY = Column(Numeric(22, 4))
    PAYMENTMOTORVEHICLE = Column(Numeric(22, 4))
    PAYMENTLIABILITY = Column(Numeric(22, 4))
    PAYMENTPROJECT = Column(Numeric(22, 4))
    PAYMENTFREIGHT = Column(Numeric(22, 4))
    PAYMENTSHIP = Column(Numeric(22, 4))
    PAYMENTCREDIT = Column(Numeric(22, 4))
    PAYMENTGUARANTEE = Column(Numeric(22, 4))
    PAYMENTCREDITGUARANTEE = Column(Numeric(22, 4))
    PAYMENTSPECIALRISKS = Column(Numeric(22, 4))
    PAYMENTFARM = Column(Numeric(22, 4))
    PAYMENTSHORTTIMEHEALTH = Column(Numeric(22, 4))
    PAYMENTACCIDENT = Column(Numeric(22, 4))
    PAYMENTOTHER = Column(Numeric(22, 4))
    CLAIM = Column(Numeric(22, 4))
    OUTSTANDING = Column(Numeric(22, 4))
    AREANAME = Column(String(100, u'utf8_bin'))
    AREANAME_EN = Column(String(200, u'utf8_bin'))
