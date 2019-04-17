# -*- coding: utf-8 -*-
from jqdatasdk import *

with open("/home/server/etc/jqdatasdk/import_debug_account.py") as f:
    exec (f.read())


def test_ssymmetry():
    df = ssymmetry.run_query(query(ssymmetry.ecommerce_data))
    assert len(df) == 5000
    assert set(df.columns) - set(
        [
            "date", "market", "industry", "stock_code",
            "company", "brand", "sales", "gmv",
            "average_price", "is_mall",
        ]) == set()
    assert ssymmetry.__dict__["_DBTable__table_names"] == ['ecommerce_data', 'guba_sentiment_daily',
                                                           'guba_sentiment_hourly', 'weibo_sentiment_daily',
                                                           'xueqiu_sentiment_daily', 'xueqiu_sentiment_hourly']

def test_bond():
    df = bond.run_query(query(bond.BOND_BASIC_INFO).limit(10))
    assert len(df) == 10
    assert df.iloc[0].to_json() == ('{"id":1,"code":"041453001","short_name":"14\\u8499\\u4e1c\\u8fbeCP001",'
                                   '"full_name":"2014\\u5e74\\u5185\\u8499\\u53e4\\u4e1c\\u8fbe\\u8499\\u53e4\\u738b\\u'
                                    '96c6\\u56e2\\u6709\\u9650\\u516c\\u53f8\\u7b2c\\u4e00\\u671f\\u77ed\\u671f\\u878d'
                                    '\\u8d44\\u5238","list_status_id":301006.0,"list_status":"\\u7ec8\\u6b62\\u4e0a\\u5'
                                    'e02","issuer":"\\u5185\\u8499\\u53e4\\u4e1c\\u8fbe\\u8499\\u53e4\\u738b\\u96c6\\u5'
                                    '6e2\\u6709\\u9650\\u516c\\u53f8","company_code":null,"exchange_code":705007,'
                                    '"exchange":"\\u94f6\\u884c\\u95f4\\u503a\\u5238\\u5e02\\u573a","currency_id":'
                                    '"\\u4eba\\u6c11\\u5e01","coupon_type_id":701001,"coupon_type":"\\u5229\\u968f\\u6'
                                    '72c\\u6e05","coupon_frequency":null,"payment_type_id":702001,"payment_type":"\\u523'
                                    '0\\u671f\\u4e00\\u6b21\\u4ed8\\u606f","par":100.0,"repayment_period":12.0,"bond_t'
                                    'ype_id":703001,"bond_type":"\\u77ed\\u671f\\u878d\\u8d44\\u5238","bond_form_id":7'
                                    '04001,"bond_form":"\\u8bb0\\u8d26\\u5f0f","list_date":1389225600000,"delist_Date'
                                    '":1420416000000,"interest_begin_date":1389139200000,"maturity_date":1420675200000,'
                                    '"interest_date":null,"last_cash_date":1420675200000,"cash_comment":null}')
