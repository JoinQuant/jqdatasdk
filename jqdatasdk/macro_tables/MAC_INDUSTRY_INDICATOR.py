# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_INDICATOR(Base):
    """
    工业企业主要指标
    """

    __tablename__ = "MAC_INDUSTRY_INDICATOR"

    id = Column(Integer, primary_key=True)
    stat_month = Column(String(20), nullable=False)
    enterprise_value_acc = Column(Integer)
    loss_enterprise_value_acc = Column(Integer)
    loss_enterprise_ratio_acc = Column(DECIMAL(10, 4))
    current_asset_value_acc = Column(DECIMAL(20, 4))
    current_asset_ratio_acc = Column(DECIMAL(10, 4))
    accounts_receivable_value_acc = Column(DECIMAL(20, 4))
    accounts_receivable_ratio_acc = Column(DECIMAL(10, 4))
    inventories_value_acc = Column(DECIMAL(20, 4))
    inventories_ratio_acc = Column(DECIMAL(10, 4))
    finished_product_value_acc = Column(DECIMAL(20, 4))
    finished_product_ratio_acc = Column(DECIMAL(10, 4))
    total_assets_value_acc = Column(DECIMAL(20, 4))
    total_assets_ratio_acc = Column(DECIMAL(10, 4))
    liabilities_value_acc = Column(DECIMAL(20, 4))
    liabilities_ratio_acc = Column(DECIMAL(10, 4))
    main_business_value_acc = Column(DECIMAL(20, 4))
    main_business_ratio_acc = Column(DECIMAL(10, 4))
    main_business_tax_value_acc = Column(DECIMAL(20, 4))
    main_business_tax_ratio_acc = Column(DECIMAL(10, 4))
    sale_expense_value_acc = Column(DECIMAL(20, 4))
    sale_expense_ratio_acc = Column(DECIMAL(10, 4))
    management_cost_value_acc = Column(DECIMAL(20, 4))
    management_cost_ratio_acc = Column(DECIMAL(10, 4))
    financial_expense_value_acc = Column(DECIMAL(20, 4))
    financial_expense_ratio_acc = Column(DECIMAL(10, 4))
    interest_expense_value_acc = Column(DECIMAL(20, 4))
    interest_expense_ratio_acc = Column(DECIMAL(10, 4))
    total_interest_value_acc = Column(DECIMAL(20, 4))
    total_interest_ratio_acc = Column(DECIMAL(10, 4))
    enterprise_total_loss_value_acc = Column(DECIMAL(20, 4))
    enterprise_total_loss_ratio_acc = Column(DECIMAL(10, 4))
    vat_value_acc = Column(DECIMAL(20, 4))
    vat_ratio_acc = Column(DECIMAL(10, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addTime = Column(TIMESTAMP, default=datetime.datetime.now)
    modTime = Column(TIMESTAMP)