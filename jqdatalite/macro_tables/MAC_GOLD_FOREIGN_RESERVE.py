# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_GOLD_FOREIGN_RESERVE(Base):
    """
    黄金和外汇储备
    """

    __tablename__ = "MAC_GOLD_FOREIGN_RESERVE"

    id = Column(Integer, primary_key=True)
    stat_date = Column(String(10), nullable=False)
    gold = Column(DECIMAL(10, 4))
    foreign = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)