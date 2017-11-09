# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FOREIGN_CAPITAL_YEAR(Base):
    """
    利用外资概况表（年度）
    """
    __tablename__ = "MAC_FOREIGN_CAPITAL_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    total_invest_value = Column(DECIMAL(20, 4))
    invest_value = Column(DECIMAL(20, 4))
    other_invest_value = Column(DECIMAL(20, 4))
    total_contract_project_num = Column(DECIMAL(20, 4))
    total_contract_invest_value = Column(DECIMAL(20, 4))
    contract_project_num = Column(DECIMAL(20, 4))
    contract_invest_value = Column(DECIMAL(20, 4))
    contract_other_invest_value = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)