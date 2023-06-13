# -*- coding: utf-8 -*-

from __future__ import print_function

import pytest
from jqdatasdk import opt, finance, macro, bond, sup, query, get_server_version


def test_opt():
    df = opt.run_query(query(opt.OPT_CONTRACT_INFO).limit(6).offset(20000))
    print(df)
    assert len(df) == 6
    assert df.iloc[-1, 0] >= 20000  # id 列
    assert df["code"].tolist() == [
        'C2101-C-2780.XDCE', 'C2101-C-2800.XDCE', 'C2101-C-2820.XDCE',
        'C2101-C-2840.XDCE', 'C2101-P-2780.XDCE', 'C2101-P-2800.XDCE'
    ]
    df = df.set_index("code").drop("id", axis=1)
    item = df.loc["C2101-C-2800.XDCE"]
    assert item["name"] == u"玉米购1月2800"
    assert item.underlying_symbol == "C2101.XDCE"
    assert str(item.delist_date) == "2020-12-08"

    df = opt.run_query(query(opt.OPT_CONTRACT_INFO.code).limit(10005))
    assert len(df) <= 10000


def test_fin():
    q = query(finance.FINANCE_BALANCE_SHEET).limit(5).offset(100)
    df = finance.run_query(q)
    print(df)
    assert len(df) == 5
    print(df["report_type"])
    assert df["company_id"].tolist() == [420600000, 420600000, 430000563,
                                         430000563, 430000001]
    assert df["code"].tolist() == ['600000.XSHG', '600000.XSHG', '000563.XSHE',
                                   '000563.XSHE', '000001.XSHE']
    assert df["report_type"].tolist() == [1, 0, 1, 0, 1]


def test_macro():
    df = macro.run_query(query(macro.MAC_AREA_DIV).limit(5).offset(1000))
    print(df)
    assert len(df) == 5
    assert df["area_code"].tolist() == ['330101', '330102', '330103', '330104', '330105']
    assert set(df["province_name"]) == {u"浙江省"}
    assert set(df["city_name"]) == {u"杭州市"}


def test_bond():
    df = bond.run_query(query(bond.BOND_BASIC_INFO).limit(10))
    print(df)
    assert len(df) == 10
    df = df.set_index("code").drop("id", axis=1)
    item = df.loc["131801"]
    assert item.short_name == u"花呗01A1" and str(item.maturity_date) == "2017-06-15"
    item = df.loc["111011"]
    assert item.short_name == u"中铁963" and str(item.maturity_date) == "2000-01-20"


def test_sup():
    if get_server_version() >= "2":
        pytest.skip("new version is not supported")
    df = sup.run_query(query(sup.STK_FINANCE_SUPPLEMENT).limit(10))
    print(df)
    assert len(df) == 10
    assert set(df["company_id"]) == {300000062}
    assert set(df["code"]) == {"002054.XSHE"}
    assert df["report_type"].iloc[3] == 1 and df["report_type"].iloc[8] == 0

    finance_query = query(finance.FINANCE_BALANCE_SHEET)
    finance_df = finance.run_query(finance_query)
    finance_offset_df = finance.run_offset_query(query(finance.FINANCE_BALANCE_SHEET), 0)
    assert type(finance_df) is type(finance_offset_df)
    with pytest.raises(AssertionError):
        # "step 的合法范围为 [0, 5000]"
        finance.run_offset_query(query(finance.FINANCE_BALANCE_SHEET), -1)
        finance.run_offset_query(query(finance.FINANCE_BALANCE_SHEET), 9999)

    bond_empty_query = query(bond.BOND_BASIC_INFO).filter(bond.BOND_BASIC_INFO.last_cash_date > '20250101')
    bond_df = bond.run_query(bond_empty_query)
    bond_offset_df = bond.run_offset_query(bond_empty_query, 250)
    from pandas.testing import assert_frame_equal
    assert_frame_equal(bond_df, bond_offset_df)
