# coding: utf-8
import datetime
from sqlalchemy import Date, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_COMPANY_INFO(Base):

    __tablename__ = 'STK_COMPANY_INFO'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, nullable=False, comment="公司ID")
    code = Column(String(12), nullable=False, comment="公司主证券代码")
    full_name = Column(String(100), comment="公司名称")
    short_name = Column(String(40), comment="公司简称")
    a_code = Column(String(12), comment="A股代码")
    b_code = Column(String(12), comment="B股代码")
    h_code = Column(String(12), comment="H股代码")
    fullname_en = Column(String(100), comment="英文名称")
    shortname_en = Column(String(40), comment="英文简称")
    legal_representative = Column(String(40), comment="法人代表")
    register_location = Column(String(100), comment="注册地址")
    office_address = Column(String(150), comment="办公地址")
    zipcode = Column(String(10), comment="邮政编码")
    register_capital = Column(DECIMAL(20, 4), comment="注册资金")
    currency_id = Column(Integer, comment="货币编码")
    currency = Column(String(32), comment="货币名称")
    establish_date = Column(Date, comment="成立日期")
    website = Column(String(80), comment="机构网址")
    email = Column(String(80), comment="电子信箱")
    contact_number = Column(String(60), comment="联系电话")
    fax_number = Column(String(60), comment="联系传真")
    main_business = Column(String(500), comment="主营业务")
    business_scope = Column(String(4000), comment="经营范围")
    description = Column(String(4000), comment="机构简介")
    tax_number = Column(String(50), comment="税务登记号")
    license_number = Column(String(40), comment="法人营业执照号")
    pub_newspaper = Column(String(120), comment="指定信息披露报刊")
    pub_website = Column(String(120), comment="指定信息披露网站")
    secretary = Column(String(40), comment="董事会秘书")
    secretary_number = Column(String(60), comment="董秘联系电话")
    secretary_fax = Column(String(60), comment="董秘联系传真")
    secretary_email = Column(String(80), comment="董秘电子邮箱")
    security_representative = Column(String(40), comment="证券事务代表")
    province_id = Column(String(12), comment="所属省份编码")
    province = Column(String(60), comment="所属省份")
    city_id = Column(String(12), comment="所属城市编码")
    city = Column(String(60), comment="所属城市")
    industry_id = Column(String(12), comment="证监会行业分类编码")
    industry_1 = Column(String(60), comment="行业门类")
    industry_2 = Column(String(60), comment="行业大类")
    cpafirm = Column(String(200), comment="会计师事务所")
    lawfirm = Column(String(200), comment="律师事务所")
    ceo = Column(String(100), comment="总经理")
    comments = Column(String(300), comment="备注")
