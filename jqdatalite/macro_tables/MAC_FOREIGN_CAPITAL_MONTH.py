# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FOREIGN_CAPITAL_MONTH(Base):
    """
    利用外资情况表（月度）
    """
    __tablename__ = "MAC_FOREIGN_CAPITAL_MONTH"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    num_acc = Column(DECIMAL(20, 4))
    num_acc_yoy = Column(DECIMAL(10, 4))
    joint_num_acc = Column(DECIMAL(20, 4))
    joint_num_acc_yoy = Column(DECIMAL(10, 4))
    cooperative_num_acc = Column(DECIMAL(20, 4))
    cooperative_num_acc_yoy = Column(DECIMAL(10, 4))
    foreign_num_acc = Column(DECIMAL(20, 4))
    foreign_num_acc_yoy = Column(DECIMAL(10, 4))
    foreign_share_num_acc = Column(DECIMAL(20, 4))
    foreign_share_num_acc_yoy = Column(DECIMAL(10, 4))
    value_acc = Column(DECIMAL(20, 4))
    value_acc_yoy = Column(DECIMAL(10, 4))
    joint_value_acc = Column(DECIMAL(20, 4))
    joint_value_acc_yoy = Column(DECIMAL(10, 4))
    cooperative_value_acc = Column(DECIMAL(20, 4))
    cooperative_value_acc_yoy = Column(DECIMAL(10, 4))
    foreign_value_acc = Column(DECIMAL(20, 4))
    foreign_value_acc_yoy = Column(DECIMAL(10, 4))
    foreign_share_value_acc = Column(DECIMAL(20, 4))
    foreign_share_value_acc_yoy = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)