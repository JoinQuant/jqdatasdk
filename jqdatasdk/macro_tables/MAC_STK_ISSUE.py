# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_STK_ISSUE(Base):
    """
    股票发行量和筹资额
    """

    __tablename__ = "MAC_STK_ISSUE"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    shared_issued = Column(DECIMAL(20, 4))
    a_shared_issued = Column(DECIMAL(20, 4))
    hn_shared_issued = Column(DECIMAL(20, 4))
    b_shared_issued = Column(DECIMAL(20, 4))
    stk_financing_amount = Column(DECIMAL(20, 4))
    a_stk_financing_amount = Column(DECIMAL(20, 4))
    allot_financing_amount = Column(DECIMAL(20, 4))
    hn_stk_financing_amount = Column(DECIMAL(20, 4))
    b_stk_financing_amount = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)