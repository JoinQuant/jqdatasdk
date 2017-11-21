# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_ENTERPRISE_BOOM_CONFIDENCE_IDX(Base):
    """
    企业景气及企业家信心指数
    """

    __tablename__ = "MAC_ENTERPRISE_BOOM_CONFIDENCE_IDX"

    id = Column(Integer, primary_key=True)
    stat_quarter = Column(String(20), nullable=False)
    boom_idx = Column(DECIMAL(10, 4))
    boom_idx_yoy = Column(DECIMAL(10, 4))
    boom_idx_mom = Column(DECIMAL(10, 4))
    confidence_idx = Column(DECIMAL(10, 4))
    confidence_idx_yoy = Column(DECIMAL(10, 4))
    confidence_idx_mom = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)