

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDU_URBANFIXEDCONST(Base):
    __tablename__ = "MAC_INDU_URBANFIXEDCONST"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    INDUSTRYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    CONSTRUCT = Column(Numeric(18, 4))
    UNDERCONSTRUCT = Column(Numeric(18, 4))
    NETUNDERCONSTRUCT = Column(Numeric(18, 4))
    FIXEDASSETSINVEST = Column(Numeric(18, 4))
    NEWCONSTRUCT = Column(Numeric(18, 4))
    EXPAND = Column(Numeric(18, 4))
    RECONSTRUCT = Column(Numeric(18, 4))
    CONSTRUCTINSTALL = Column(Numeric(18, 4))
    EQUIPMENTPURCHASE = Column(Numeric(18, 4))
    OTHEREXPENSE = Column(Numeric(18, 4))
