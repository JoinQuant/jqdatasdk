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
