

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_HOLDER_SYSTEMATICS(Base):
    __tablename__ = "STK_HOLDER_SYSTEMATICS"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    FUNDHOLDSHARES = Column(Numeric(20, 2))
    FUNDHOLDPROPORTION = Column(Numeric(10, 4))
    QFIIHOLDSHARES = Column(Numeric(20, 2))
    QFIIHOLDPROPORTION = Column(Numeric(10, 4))
    BROKERHOLDSHARES = Column(Numeric(20, 2))
    BROKERHOLDPROPORTION = Column(Numeric(10, 4))
    INSURANCEHOLDSHARES = Column(Numeric(20, 2))
    INSURANCEHOLDPROPORTION = Column(Numeric(10, 4))
    SECURITYFUNDHOLDSHARES = Column(Numeric(20, 2))
    SECURITYFUNDHOLDPROPORTION = Column(Numeric(10, 4))
    ENTRUSTHOLDSHARES = Column(Numeric(20, 2))
    ENTRUSTHOLDPROPORTION = Column(Numeric(10, 4))
    FINANCEHOLDSHARES = Column(Numeric(20, 2))
    FINANCEHOLDPROPORTION = Column(Numeric(10, 4))
    BANKHOLDSHARES = Column(Numeric(20, 2))
    BANKHOLDPROPORTION = Column(Numeric(10, 4))
    NONFINANCEHOLDSHARES = Column(Numeric(20, 2))
    NONFINANCEHOLDPROPORTION = Column(Numeric(10, 4))
