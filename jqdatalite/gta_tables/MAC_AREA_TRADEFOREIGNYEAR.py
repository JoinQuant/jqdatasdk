

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_TRADEFOREIGNYEAR(Base):
    __tablename__ = "MAC_AREA_TRADEFOREIGNYEAR"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    TOTAL = Column(Numeric(18, 4))
    EXPORT = Column(Numeric(18, 4))
    IMPORT = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
    AREACODE = Column(String(20, u'utf8_bin'))
