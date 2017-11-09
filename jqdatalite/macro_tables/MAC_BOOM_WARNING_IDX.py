# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_BOOM_WARNING_IDX(Base):
    """
    宏观经济景气预警指数
    """

    __tablename__ = "MAC_BOOM_WARNING_IDX"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    warning_idx = Column(DECIMAL(10, 4))
    industry_idx_sgn = Column(DECIMAL(10, 4))
    fixed_assets_sgn = Column(DECIMAL(10, 4))
    rpi_sgn = Column(DECIMAL(10, 4))
    import_export_sgn = Column(DECIMAL(10, 4))
    gov_revenue_sgn = Column(DECIMAL(10, 4))
    industry_profit_sgn = Column(DECIMAL(10, 4))
    resident_dpi_sgn = Column(DECIMAL(10, 4))
    loan_sgn = Column(DECIMAL(10, 4))
    m2_sgn = Column(DECIMAL(10, 4))
    cpi_sgn = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)