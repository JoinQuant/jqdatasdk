# -*- coding: utf-8 -*-
from jqdatasdk import *

with open("/home/server/etc/jqdatasdk/import_debug_account.py") as f:
    exec (f.read())


def test_bond():
    df = bond.run_query(query(bond.BOND_BASIC_INFO).limit(10))
    assert len(df) == 10
    assert df.iloc[0].to_json() == ('{"id":1,"code":"041453001","short_name":"14\\u8499\\u4e1c\\u8fbeCP001","full_name":"2014\\u5e74\\u5185\\u8499\\u53e4\\u4e1c\\u8fbe\\u8499\\u53e4\\u738b\\u96c6\\u56e2\\u6709\\u9650\\u516c\\u53f8\\u7b2c\\u4e00\\u671f\\u77ed\\u671f\\u878d\\u8d44\\u5238","list_status_id":301006,"list_status":"\\u7ec8\\u6b62\\u4e0a\\u5e02","issuer":"\\u5185\\u8499\\u53e4\\u4e1c\\u8fbe\\u8499\\u53e4\\u738b\\u96c6\\u56e2\\u6709\\u9650\\u516c\\u53f8","company_code":null,"exchange_code":705007,"exchange":"\\u94f6\\u884c\\u95f4\\u503a\\u5238\\u5e02\\u573a","currency_id":"\\u4eba\\u6c11\\u5e01","coupon_type_id":701001,"coupon_type":"\\u5229\\u968f\\u672c\\u6e05","coupon_frequency":null,"payment_type_id":702001,"payment_type":"\\u5230\\u671f\\u4e00\\u6b21\\u4ed8\\u606f","par":100.0,"repayment_period":12.0,"bond_type_id":703001,"bond_type":"\\u77ed\\u671f\\u878d\\u8d44\\u5238","bond_form_id":704001,"bond_form":"\\u8bb0\\u8d26\\u5f0f","list_date":1389225600000,"delist_Date":1420416000000,"interest_begin_date":1389139200000,"maturity_date":1420675200000,"interest_date":null,"last_cash_date":1420675200000,"cash_comment":null}')


def test_sup():
    df = sup.run_query(query(sup.STK_FINANCE_SUPPLEMENT).limit(10))
    assert len(df) == 10
    assert df.iloc[0].to_json() == ('{"id":1,"company_id":300000062,"company_name":"\\u5e7f\\u4e1c\\u5fb7\\u7f8e\\u7cbe\\u7ec6\\u5316\\u5de5\\u96c6\\u56e2\\u80a1\\u4efd\\u6709\\u9650\\u516c\\u53f8","code":"002054.XSHE","a_code":"002054","b_code":null,"h_code":null,"pub_date":1151020800000,"start_date":1041379200000,"end_date":1072828800000,"report_date":1072828800000,"report_type":0,"source_id":321001,"source":"\\u62db\\u52df\\u8bf4\\u660e\\u4e66","bill_and_account_receivable":null,"bill_and_account_payable":null,"rd_expenses":null}')
