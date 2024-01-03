# -*- coding: utf-8 -*-

from __future__ import print_function

import pytest
from jqdatasdk import opt, finance, macro, bond, sup, query, get_server_version


def test_load_table_class():
    assert finance.FUND_MF_DAILY_PROFIT is not None
    assert finance.FUND_MF_DAILY_PROFIT.code is not None
    assert finance.FUND_MF_DAILY_PROFIT.name is not None


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
    assert (df["company_id"] >= 100016047).all()
    assert df["code"].str.endswith(('XSHE', 'XSHG')).all()

    df = finance.run_query(query(finance.FUT_CHARGE))
    print(df)
    assert len(df) > 0
    df = finance.run_query(query(finance.FUT_MARGIN))
    assert len(df) > 0
    df = finance.run_query(query(finance.STK_AUDIT_OPINION))
    assert len(df) > 0


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
    item = df.iloc[0]
    assert item.short_name and str(item.maturity_date) >= "2000-01-01"
    item = df.iloc[-1]
    assert item.short_name and str(item.maturity_date) >= "2000-01-01"


def test_sup():
    if get_server_version() >= "2":
        pytest.skip("new version is not supported")
    df = sup.run_query(query(sup.STK_FINANCE_SUPPLEMENT).limit(10))
    print(df)
    assert len(df) == 10
    assert set(df["company_id"]) == {300000062}
    assert set(df["code"]) == {"002054.XSHE"}
    assert df["report_type"].iloc[3] == 1 and df["report_type"].iloc[8] == 0


def test_offset_query():
    opt_query = query(opt.OPT_DAILY_PRICE)
    opt_df = opt.run_query(opt_query)
    with pytest.warns(UserWarning):
        opt_offset_df = opt.run_offset_query(opt_query)
    assert len(opt_df) == 5000
    assert len(opt_offset_df) == 10000 * 20
    assert list(opt_df.columns) == list(opt_offset_df.columns)

    finance_query = query(finance.FINANCE_BALANCE_SHEET)
    finance_df = finance.run_query(finance_query)
    finance_offset_df = finance.run_offset_query(query(finance.FINANCE_BALANCE_SHEET))
    assert type(finance_df) is type(finance_offset_df)

    bond_empty_query = query(
        bond.BOND_BASIC_INFO
    ).filter(
        bond.BOND_BASIC_INFO.last_cash_date > '22001231'
    )
    bond_df = bond.run_query(bond_empty_query)
    bond_offset_df = bond.run_offset_query(bond_empty_query)
    assert len(bond_df) == len(bond_offset_df)

    dup_oft_df = finance.run_offset_query(query(finance.STK_FIN_FORCAST))
    assert len(dup_oft_df[dup_oft_df.duplicated(keep=False)].sort_values('id')) == 0
