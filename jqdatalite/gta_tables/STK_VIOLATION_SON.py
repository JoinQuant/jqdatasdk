

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_VIOLATION_SON(Base):
    __tablename__ = "STK_VIOLATION_SON"

    VIOLATIONID = Column(Numeric(20, 0))
    VIOLATORNAME = Column(String(200, u'utf8_bin'))
    VIOLATORID = Column(Numeric(20, 0))
    RELATIONSHIP = Column(String(200, u'utf8_bin'))
    RELATIONSHIPID = Column(String(100, u'utf8_bin'))
    VIOLATORNATURE = Column(String(100, u'utf8_bin'))
    VIOLATORNATUREID = Column(String(12, u'utf8_bin'))
    PUNISHMENTTYPE = Column(String(200, u'utf8_bin'))
    PUNISHMENTTYPEID = Column(String(100, u'utf8_bin'))
    PENALTY = Column(Numeric(20, 2))
    UPDATEID = Column(BigInteger, primary_key=True, server_default=text("'0'"))
