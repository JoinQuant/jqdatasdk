# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_PARAMETER(Base):
    """
    宏观经济数据-编码表
    """
    __tablename__ = "MAC_PARAMETER"

    id = Column(Integer, primary_key=True)
    class_code = Column(Integer, nullable=False)
    class_name = Column(String(100), nullable=False)
    parameter_code = Column(Integer, nullable=False)
    parameter_name = Column(String(100), nullable=False)
    description = Column(String(200))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)