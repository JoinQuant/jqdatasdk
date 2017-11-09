# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCAL_TAX_YEAR(Base):
    """
    各项税收表（年度）
    """
    __tablename__ = "MAC_FISCAL_TAX_YEAR"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    tax = Column(DECIMAL(20, 4))
    add_value_tax = Column(DECIMAL(20, 4))
    business_tax = Column(DECIMAL(20, 4))
    consumption_tax = Column(DECIMAL(20, 4))
    tariff = Column(DECIMAL(20, 4))
    individual_tax = Column(DECIMAL(20, 4))
    corporate_tax = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)