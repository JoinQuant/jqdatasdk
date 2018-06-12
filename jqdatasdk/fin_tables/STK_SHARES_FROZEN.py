# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_SHARES_FROZEN(Base):

    __tablename__ = 'STK_SHARES_FROZEN'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    company_name = Column(String(100), nullable=False, comment="公司名称")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    code = Column(String(12), nullable=False, comment="股票代码")
    frozen_person_id = Column(Integer, comment="被冻结当事人ID")
    frozen_person = Column(String(100), comment="被冻结当事人")
    frozen_reason = Column(String(600), comment="冻结事项")
    frozen_share_nature_id = Column(Integer, comment="被冻结股份性质编码")
    frozen_share_nature = Column(String(120), comment="被冻结股份性质")
    frozen_number = Column(DECIMAL(20, 4), comment="冻结数量")
    frozen_total_ratio = Column(DECIMAL(10, 4), comment="占总股份比例")
    freeze_applicant = Column(String(100), comment="冻结申请人")
    freeze_executor = Column(String(100), comment="冻结执行人")
    change_reason_id = Column(Integer, comment="变动原因编码")
    change_reason = Column(String(120), comment="变动原因")
    start_date = Column(Date, comment="冻结起始日")
    end_date = Column(Date, comment="冻结终止日")
    unfrozen_date = Column(Date, comment="解冻日期")
    unfrozen_number = Column(DECIMAL(20, 4), comment="累计解冻数量")
    unfrozen_detail = Column(String(1000), comment="解冻处理说明")
    # status = Column(TINYINT(display_width=4), default=0, comment="是否同步,0:未同步,1:已同步")
    # addTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="插入时间")
    # modTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="最后修改时间")
