import sys
sys.path.append("..")

from jqdatalite import *
import unittest
import datetime


class TestDataLite(unittest.TestCase):

    def test_get_price(self):
        df = get_price(security=["000001.XSHE", "000002.XSHE"], 
            start_date="2017-10-01", end_date="2017-10-26")
        print(df)

    def test_history(self):
        df = history(300, security_list=["000001.XSHE"], field="avg")
        print(df)

    def test_attribute_history(self):
        df = attribute_history(security="000001.XSHE", count=300)
        print(df)

    def test_get_trade_days(self):
        df = get_trade_days(start_date="2015-01-01")
        print(df)

    def test_get_all_trade_days(self):
        ret = get_all_trade_days()
        print(ret)

    def test_get_extras(self):
        print(get_extras('acc_net_value', ['510300.XSHG', '510050.XSHG'], start_date='2015-12-01', end_date='2015-12-03'))

    def test_get_index_stocks(self):
        print(get_index_stocks('000300.XSHG'))

    def test_get_industry_stocks(self):
        print(get_industry_stocks('I64'))

    def test_get_concept_stocks(self):
        print(get_concept_stocks('GN036', datetime.date(2017, 6, 12)))

    def test_get_all_securities(self):
        print(get_all_securities())

    def test_get_security_info(self):
        print(get_security_info('000001.XSHE'))

    def test_get_history_name(self):
        print(get_history_name('000001.XSHE', datetime.date(2016, 9, 5)))

    def test_get_money_flow(self):
        print(get_money_flow('000001.XSHE', '2016-02-01', '2016-02-04'))

    def test_get_fundamentals(self):
        df = get_fundamentals(query(income).limit(10), datetime.date(2015, 1, 1))
        print(df)

    def test_get_mtss(self):
        df = get_mtss('000001.XSHE', '2016-01-01', '2016-04-01')
        print(df)

    def test_gta_query(self):
        df = gta.run_query(query(
                gta.STK_STOCKINFO
            ).filter(
                gta.STK_STOCKINFO.ISSUEPRICE > 10,
                gta.STK_STOCKINFO.SHARETYPE == 'A'
            ).limit(20))
        print(df)


if __name__ == "__main__":
    init("admin", "admin")
    unittest.main()
    # TestDataLite().test_get_money_flow()




