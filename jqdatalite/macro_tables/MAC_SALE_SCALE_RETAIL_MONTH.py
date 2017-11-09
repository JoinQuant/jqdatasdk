# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_SALE_SCALE_RETAIL_MONTH(Base):
    """
    限额以上零售分类表
    """

    __tablename__ = "MAC_SALE_SCALE_RETAIL_MONTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    item_name = Column(String(128), nullable=False)
    item_sale_sin = Column(DECIMAL(20, 4))
    item_sale_acc = Column(DECIMAL(20, 4))
    item_sale_sin_rate = Column(DECIMAL(10, 4))
    item_sale_acc_rate = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)