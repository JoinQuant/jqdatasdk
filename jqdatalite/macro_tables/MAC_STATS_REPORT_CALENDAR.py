# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_STATS_REPORT_CALENDAR(Base):
    """
    国家统计局发布经济信息的日程表
    """

    __tablename__ = "MAC_STATS_REPORT_CALENDAR"

    id = Column(Integer, primary_key=True)
    report_date = Column(TIMESTAMP)
    content = Column(String(200), nullable=False)
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)