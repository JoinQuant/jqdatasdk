

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INRSWAPQUOTE(Base):
    __tablename__ = "MAC_INRSWAPQUOTE"

    TRADINGDATE = Column(DateTime, primary_key=True, nullable=False)
    REFERATEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    TRADETERMID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    FIXEDRATE = Column(Numeric(6, 2))
    NOTIONALPRINCIPAL = Column(Numeric(8, 2))
