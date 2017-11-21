# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_TRADE_VALUE_SITC_YEAR(Base):
    """
    海关进出口货物分类金额表（年度）
    """
    __tablename__ = "MAC_TRADE_VALUE_SITC_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    item_id = Column(String(10), nullable=False)
    item_name = Column(String(128), nullable=False)
    export_dollar = Column(DECIMAL(20, 4))
    import_dollar = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)