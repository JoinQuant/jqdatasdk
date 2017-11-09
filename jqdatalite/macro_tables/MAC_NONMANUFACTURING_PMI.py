# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_NONMANUFACTURING_PMI(Base):
    """
    非制造业采购经理指数
    """

    __tablename__ = "MAC_NONMANUFACTURING_PMI"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    business_idx = Column(DECIMAL(10, 4))
    new_orders_idx = Column(DECIMAL(10, 4))
    new_export_orders_idx = Column(DECIMAL(10, 4))
    order_in_hand_idx = Column(DECIMAL(10, 4))
    inventory_idx = Column(DECIMAL(10, 4))
    input_idx = Column(DECIMAL(10, 4))
    sell_idx = Column(DECIMAL(10, 4))
    employ_idx = Column(DECIMAL(10, 4))
    delivery_time_idx = Column(DECIMAL(10, 4))
    bussiness_activity_expected_idx = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)