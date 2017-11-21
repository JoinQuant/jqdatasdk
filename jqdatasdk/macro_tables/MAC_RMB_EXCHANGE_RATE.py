# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RMB_EXCHANGE_RATE(Base):
    """
    人民币外汇牌价(日级)
    """
    __tablename__ = "MAC_RMB_EXCHANGE_RATE"

    id = Column(Integer, primary_key=True)
    day = Column(String(20), nullable=False)
    currency_id = Column(Integer, nullable=False)
    currency_name = Column(String(20))
    cash_buy_rate = Column(DECIMAL(20, 4))
    cash_buy = Column(DECIMAL(20, 4))
    spot_sell = Column(DECIMAL(20, 4))
    cash_offer_prc = Column(DECIMAL(20, 4))
    safe_prc = Column(DECIMAL(20, 4))
    bank_reduced_prc = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)