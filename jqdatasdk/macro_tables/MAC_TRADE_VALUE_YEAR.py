# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_TRADE_VALUE_YEAR(Base):
    """
    货物进出口总额表（年度）
    """
    __tablename__ = "MAC_TRADE_VALUE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    total_rmb = Column(DECIMAL(20, 4))
    export_rmb = Column(DECIMAL(20, 4))
    import_rmb = Column(DECIMAL(20, 4))
    balance_rmb = Column(DECIMAL(20, 4))
    total_dollar = Column(DECIMAL(20, 4))
    export_dollar = Column(DECIMAL(20, 4))
    import_dollar = Column(DECIMAL(20, 4))
    balance_dollar = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)