# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_LEND_RATE(Base):
    """
    银行间拆借利率表
    """

    __tablename__ = "MAC_LEND_RATE"

    id = Column(Integer, primary_key=True)
    day = Column(String(20), nullable=False)
    currency_id = Column(Integer, nullable=False)
    currency_name = Column(String(20))
    market_id = Column(Integer, nullable=False)
    term_id = Column(Integer, nullable=False)
    interest_rate = Column(DECIMAL(10, 6), nullable=False)
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)