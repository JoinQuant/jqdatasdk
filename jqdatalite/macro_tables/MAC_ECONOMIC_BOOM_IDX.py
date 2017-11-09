# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_ECONOMIC_BOOM_IDX(Base):
    """
    宏观经济景气指数
    """

    __tablename__ = "MAC_ECONOMIC_BOOM_IDX"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    early_warning_idx = Column(DECIMAL(10, 4))
    consistency_idx = Column(DECIMAL(10, 4))
    leading_idx = Column(DECIMAL(10, 4))
    lagging_idx = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)