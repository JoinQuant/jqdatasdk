# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHAREHOLDERS_SHARE_CHANGE(Base):

    __tablename__ = 'STK_SHAREHOLDERS_SHARE_CHANGE'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    company_name = Column(String(100), nullable=False, comment="公司名称")
    code = Column(String(12), nullable=False, comment="股票代码")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    end_date = Column(Date, nullable=False, comment="增（减）持截止日")
    type = Column(Integer, nullable=False, comment="增（减）持类型")
    shareholder_id = Column(Integer, comment="股东ID")
    shareholder_name = Column(String(100), comment="股东名称")
    change_number = Column(DECIMAL(20, 4), comment="变动数量")
    change_ratio = Column(DECIMAL(20, 4), comment="变动数量占总股本比例")
    price_ceiling = Column(String(100), comment="增（减）持价格上限")
    after_change_ratio = Column(DECIMAL(20, 4), comment="变动后占比")
    # status = Column(TINYINT(display_width=4), default=0, comment="是否同步,0:未同步,1:已同步")
    # addTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="插入时间")
    # modTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="最后修改时间")
