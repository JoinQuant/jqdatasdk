

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_HOLDER_TOP10(Base):
    __tablename__ = "STK_HOLDER_TOP10"

    INSTITUTIONID = Column(Numeric(20, 0), primary_key=True, nullable=False)
    SYMBOL = Column(String(20, u'utf8_bin'))
    DECLAREDATE = Column(DateTime)
    ENDDATE = Column(DateTime, primary_key=True, nullable=False)
    SHAREHOLDERID = Column(Numeric(20, 0))
    FULLNAME = Column(String(200, u'utf8_bin'))
    SHAREHOLDERTYPEID = Column(String(12, u'utf8_bin'))
    SHAREHOLDERTYPE = Column(String(100, u'utf8_bin'))
    SHARES = Column(Numeric(20, 2))
    CHANGEREASONID = Column(String(12, u'utf8_bin'), primary_key=True, nullable=False)
    CHANGEREASON = Column(String(100, u'utf8_bin'))
    IFPLEDGEFREEZINGCUSTODY = Column(String(2, u'utf8_bin'))
    PERCENTAGEHOLDING = Column(Numeric(20, 4))
    SHARESNATUREID = Column(String(60, u'utf8_bin'))
    SHARESNATURE = Column(String(100, u'utf8_bin'))
    RANK = Column(Integer, primary_key=True, nullable=False)
