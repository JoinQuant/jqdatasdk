# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FOREIGN_COOPERATE_YEAR(Base):
    """
    对外经济合作表（年度）
    """
    __tablename__ = "MAC_FOREIGN_COOPERATE_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    project_contract_num = Column(DECIMAL(20, 4))
    project_value = Column(DECIMAL(20, 4))
    project_turnover = Column(DECIMAL(20, 4))
    project_abroad_person_num = Column(DECIMAL(20, 4))
    labour_dispatch_num = Column(DECIMAL(20, 4))
    labour_abroad_person_num = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)