# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_CAPITAL_CHANGE(Base):

    __tablename__ = "STK_CAPITAL_CHANGE"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    company_name = Column(String(100), nullable=False, comment="公司名称")
    code = Column(String(12), nullable=False, comment="股票代码")
    change_date = Column(Date, nullable=False, comment="变动日期")
    pub_date = Column(Date, nullable=False, comment="公告日期")
    change_reason_id = Column(Integer, comment="变动原因编码")
    change_reason = Column(String(120), comment="变动原因")
    share_total = Column(DECIMAL(20, 4), comment="总股本")
    share_non_trade = Column(DECIMAL(20, 4), comment="未流通股份")
    share_start = Column(DECIMAL(20, 4), comment="发起人股份")
    share_nation = Column(DECIMAL(20, 4), comment="国家持股")
    share_nation_legal = Column(DECIMAL(20, 4), comment="国有法人持股")
    share_instate_legal = Column(DECIMAL(20, 4), comment="境内法人持股")
    share_outstate_legal = Column(DECIMAL(20, 4), comment="境外法人持股")
    share_natural = Column(DECIMAL(20, 4), comment="自然人持股")
    share_raised = Column(DECIMAL(20, 4), comment="募集法人股")
    share_inside = Column(DECIMAL(20, 4), comment="内部职工股")
    share_convert = Column(DECIMAL(20, 4), comment="转配股")
    share_perferred = Column(DECIMAL(20, 4), comment="优先股")
    share_other_nontrade = Column(DECIMAL(20, 4), comment="其他未流通股")
    share_limited = Column(DECIMAL(20, 4), comment="流通受限股份")
    share_legal_issue = Column(DECIMAL(20, 4), comment="配售法人股")
    share_strategic_investor = Column(DECIMAL(20, 4), comment="战略投资者持股")
    share_fund = Column(DECIMAL(20, 4), comment="证券投资基金持股")
    share_normal_legal = Column(DECIMAL(20, 4), comment="一般法人持股")
    share_other_limited = Column(DECIMAL(20, 4), comment="其他流通受限股份")
    share_nation_limited = Column(DECIMAL(20, 4), comment="国家持股（受限）")
    share_nation_legal_limited = Column(DECIMAL(20, 4), comment="国有法人持股（受限）")
    other_instate_limited = Column(DECIMAL(20, 4), comment="其他内资持股（受限）")
    legal_of_other_instate_limited = Column(DECIMAL(20, 4), comment="其他内资持股（受限）中的境内法人持股")
    natural_of_other_instate_limited = Column(DECIMAL(20, 4), comment="外资持股（受限）境外自然人持股")
    outstate_limited = Column(DECIMAL(20, 4), comment="外资持股（受限）")
    legal_of_outstate_limited = Column(DECIMAL(20, 4), comment="外资持股（受限）中的境外法人持股")
    natural_of_outstate_limited = Column(DECIMAL(20, 4), comment="外资持股（受限）境外自然人持股")
    share_trade_total = Column(DECIMAL(20, 4), comment="已流通股份")
    share_rmb = Column(DECIMAL(20, 4), comment="人民币普通股")
    share_b = Column(DECIMAL(20, 4), comment="境内上市外资股（B股）")
    share_b_limited = Column(DECIMAL(20, 4), comment="限售B股")
    share_h = Column(DECIMAL(20, 4), comment="境外上市外资股（H股）")
    share_h_limited = Column(DECIMAL(20, 4), comment="限售H股")
    share_management = Column(DECIMAL(20, 4), comment="高管股")
    share_management_limited = Column(DECIMAL(20, 4), comment="限售高管股")
    share_other_trade = Column(DECIMAL(20, 4), comment="其他流通股")
    control_shareholder_limited = Column(DECIMAL(20, 4), comment="控股股东、实际控制人(受限)")
    core_employee_limited = Column(DECIMAL(20, 4), comment="核心员工(受限)")
    individual_fund_limited = Column(DECIMAL(20, 4), comment="个人或基金(受限)")
    other_legal_limited = Column(DECIMAL(20, 4), comment="其他法人(受限)")
    other_limited = Column(DECIMAL(20, 4), comment="其他(受限)")
    # status = Column(TINYINT(display_width=4), default=0, comment="是否同步,0:未同步,1:已同步")
    # addTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="插入时间")
    # modTime = Column(TIMESTAMP, default=datetime.datetime.now, comment="最后修改时间")
