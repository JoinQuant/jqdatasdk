# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_GROWTH(Base):
    """
    全国工业增长速度
    """
    __tablename__ = "MAC_INDUSTRY_GROWTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    growth_yoy = Column(DECIMAL(10, 4))
    growth_acc = Column(DECIMAL(10, 4))
    state_owned_yoy = Column(DECIMAL(10, 4))
    state_owned_acc = Column(DECIMAL(10, 4))
    private_yoy = Column(DECIMAL(10, 4))
    private_acc = Column(DECIMAL(10, 4))
    collective_yoy = Column(DECIMAL(10, 4))
    collective_acc = Column(DECIMAL(10, 4))
    stock_cooperate_yoy = Column(DECIMAL(10, 4))
    stock_cooperate_acc = Column(DECIMAL(10, 4))
    joint_stock_yoy = Column(DECIMAL(10, 4))
    joint_stock_acc = Column(DECIMAL(10, 4))
    foreign_yoy = Column(DECIMAL(10, 4))
    foreign_acc = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)