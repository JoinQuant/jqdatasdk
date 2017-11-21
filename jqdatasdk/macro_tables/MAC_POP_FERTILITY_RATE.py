# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_POP_FERTILITY_RATE(Base):
    """
    育龄妇女分年龄、孩次的生育状况表
    """
    __tablename__ = "MAC_POP_FERTILITY_RATE"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    age = Column(String(30), nullable=False)
    rate = Column(DECIMAL(10, 8))
    population = Column(DECIMAL(20, 4))
    births = Column(DECIMAL(20, 4))
    first_births = Column(DECIMAL(20, 4))
    second_births = Column(DECIMAL(20, 4))
    third_births = Column(DECIMAL(20, 4))
    fertility_rate = Column(DECIMAL(20, 4))
    first_fertility_rate = Column(DECIMAL(10, 4))
    second_fertility_rate = Column(DECIMAL(10, 4))
    third_fertility_rate = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)