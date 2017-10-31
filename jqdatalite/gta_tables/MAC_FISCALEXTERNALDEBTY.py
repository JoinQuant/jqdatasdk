

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCALEXTERNALDEBTY(Base):
    __tablename__ = "MAC_FISCALEXTERNALDEBTY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    DEBT = Column(Numeric(18, 4))
    GOVLOAN = Column(Numeric(18, 4))
    INSTITUTIONLOAN = Column(Numeric(18, 4))
    COMMERCELOAN = Column(Numeric(18, 4))
    TRADECREDIT = Column(Numeric(18, 4))
    OTHERDEBT = Column(Numeric(18, 4))
    LONGTERMDEBT = Column(Numeric(18, 4))
    SHORTTERMDEBT = Column(Numeric(18, 4))
    GOVLOANRATE = Column(Numeric(10, 4))
    INSTITUTIONLOANRATE = Column(Numeric(10, 4))
    COMMERCELOANRATE = Column(Numeric(10, 4))
    TRADECREDITRATE = Column(Numeric(10, 4))
    OTHERDEBTRATE = Column(Numeric(10, 4))
    LONGTERMDEBTRATE = Column(Numeric(10, 4))
    SHORTTERMDEBTRATE = Column(Numeric(10, 4))
