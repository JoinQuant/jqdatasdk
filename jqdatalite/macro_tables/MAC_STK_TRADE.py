# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_STK_TRADE(Base):
    """
    股票市场统计表
    """

    __tablename__ = "MAC_STK_TRADE"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    public_company = Column(DECIMAL(20, 4))
    stock_num = Column(DECIMAL(20, 4))
    a_stock_num = Column(DECIMAL(20, 4))
    b_stock_num = Column(DECIMAL(20, 4))
    total_share = Column(DECIMAL(20, 4))
    a_total_share = Column(DECIMAL(20, 4))
    b_total_share = Column(DECIMAL(20, 4))
    circulating_share = Column(DECIMAL(20, 4))
    a_circulating_share = Column(DECIMAL(20, 4))
    b_circulating_share = Column(DECIMAL(20, 4))
    total_value = Column(DECIMAL(20, 4))
    a_total_value = Column(DECIMAL(20, 4))
    b_total_value = Column(DECIMAL(20, 4))
    circulation_value = Column(DECIMAL(20, 4))
    a_circulation_value = Column(DECIMAL(20, 4))
    b_circulation_value = Column(DECIMAL(20, 4))
    amount = Column(DECIMAL(20, 4))
    a_amount = Column(DECIMAL(20, 4))
    b_amount = Column(DECIMAL(20, 4))
    volume = Column(DECIMAL(20, 4))
    a_volume = Column(DECIMAL(20, 4))
    b_volume = Column(DECIMAL(20, 4))
    sh_composite_index_high = Column(DECIMAL(20, 4))
    sh_composite_index_low = Column(DECIMAL(20, 4))
    sh_composite_index_close = Column(DECIMAL(20, 4))
    sz_composite_index_high = Column(DECIMAL(20, 4))
    sz_composite_index_low = Column(DECIMAL(20, 4))
    sz_composite_index_close = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)