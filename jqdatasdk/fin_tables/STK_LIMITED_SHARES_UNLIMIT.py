# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_LIMITED_SHARES_UNLIMIT(Base):

    __tablename__ = "STK_LIMITED_SHARES_UNLIMIT"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    company_name = Column(String(100), nullable=False, comment="公司名称")
    code = Column(String(12), nullable=False, comment="股票代码")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    shareholder_name = Column(String(100), nullable=False, comment="股东名称")
    actual_unlimited_date = Column(Date, comment="实际解除限售日期")
    actual_unlimited_number = Column(DECIMAL(20, 4), comment="实际解除限售数量")
    actual_unlimited_ratio = Column(DECIMAL(10, 4), comment="实际解除限售比例")
    limited_reason_id = Column(Integer, comment="限售原因编码")
    limited_reason = Column(String(60), comment="限售原因")
    actual_trade_number = Column(DECIMAL(20, 4), comment="实际可流通数量")
    # status = Column(TINYINT(display_width=4), default=0, comment="是否同步,0:未同步,1:已同步")
    # addTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="插入时间")
    # modTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="最后修改时间")
