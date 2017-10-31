

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_CONSUMEEXPENSEY(Base):
    __tablename__ = "MAC_CONSUMEEXPENSEY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    CONSUMEXPENSE = Column(Numeric(18, 4))
    RURAL = Column(Numeric(18, 4))
    RURALFOOD = Column(Numeric(18, 4))
    RURALCLOTHING = Column(Numeric(18, 4))
    RURALRESIDENT = Column(Numeric(18, 4))
    RURALHOUSEEQUIPMENT = Column(Numeric(18, 4))
    RURALHEALTHCARE = Column(Numeric(18, 4))
    RURALTRAFFICCOMMUNICATE = Column(Numeric(18, 4))
    RURALEDUCATECULTURE = Column(Numeric(18, 4))
    RURALFINANCIALSERVICE = Column(Numeric(18, 4))
    RURALINSURANCESERVICE = Column(Numeric(18, 4))
    RURALOTHEREXPENSE = Column(Numeric(18, 4))
    URBAN = Column(Numeric(18, 4))
    URBANFOOD = Column(Numeric(18, 4))
    URBANCLOTHING = Column(Numeric(18, 4))
    URBANRESIDENT = Column(Numeric(18, 4))
    URBANHOUSEEQUIPMENT = Column(Numeric(18, 4))
    URBANHEALTHCARE = Column(Numeric(18, 4))
    URBANTRAFFICCOMMUNICATE = Column(Numeric(18, 4))
    URBANEDUCATECULTURE = Column(Numeric(18, 4))
    URBANFINANCIALSERVICE = Column(Numeric(18, 4))
    URBANINSURANCESERVICE = Column(Numeric(18, 4))
    URBANOTHEREXPENSE = Column(Numeric(18, 4))
