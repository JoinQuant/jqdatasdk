# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_RESOURCES_ECOLOGICAL_ENVIRONMENT(Base):
    """
    生态环境情况信息表
    """
    __tablename__ = "MAC_RESOURCES_ECOLOGICAL_ENVIRONMENT"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    forest_area = Column(DECIMAL(20, 4))
    forest_cover_rate = Column(DECIMAL(10, 4))
    man_made_forest_area = Column(DECIMAL(20, 4))
    nature_reserves_num = Column(DECIMAL(20, 4))
    nature_reserves_area = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)