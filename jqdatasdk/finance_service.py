# coding=utf-8
from sqlalchemy.orm.query import Query
import re
from .utils import *
from .finance_tables import *
FUNDAMENTAL_RESULT_LIMIT = 10000


def get_tables_from_sql(sql):
    m = re.findall(
            r'cash_flow_statement_day|balance_sheet_day|financial_indicator_day|'
            r'income_statement_day|stock_valuation|bank_indicator_acc|security_indicator_acc|'
            r'insurance_indicator_acc', sql)
    return list(set(m))


def get_table_class(tablename):
    for t in (BalanceSheetDay, CashFlowStatementDay, FinancialIndicatorDay,
              IncomeStatementDay, StockValuation, BankIndicatorAcc, SecurityIndicatorAcc,
              InsuranceIndicatorAcc):
        if t.__tablename__ == tablename:
            return t


def get_stat_date_column(cls):
    if only_year:
        # 只支持按年份查询的表没有 day 字段
        return cls.statDate
    else:
        # valuation表没有statDate
        return getattr(cls, 'statDate', cls.day)


def get_fundamentals_sql(query_object, date=None, statDate=None):
    from .calendar_service import CalendarService

    assert isinstance(query_object, Query), \
    "query_object must be a sqlalchemy's Query object. But what passed in was: " + str(type(query_object))        

    stat_date = statDate
    assert (not date) ^ (not stat_date), "(statDate, date) only one param is required"

    limit = min(FUNDAMENTAL_RESULT_LIMIT, query_object._limit or FUNDAMENTAL_RESULT_LIMIT)
    offset = query_object._offset
    query_object._offset = None
    query_object._limit = None

    tablenames = get_tables_from_sql(str(query_object.statement))
    tables = [get_table_class(name) for name in tablenames]

    by_year = False
    if date:
        date = CalendarService.get_previous_trade_date(date)
    only_year = bool({"bank_indicator_acc", "security_indicator_acc",
                        "insurance_indicator_acc"} & set(tablenames))

    if only_year:
        if date:
            date = None
            stat_date = str(datetime.date.min)
        elif stat_date:
            if isinstance(stat_date, (str, six.string_types)):
                stat_date = stat_date.lower()
                if 'q' in stat_date:
                    stat_date = '0001-01-01'
                else:
                    stat_date = '{}-12-31'.format(int(stat_date))
            elif isinstance(stat_date, int):
                stat_date = '{}-12-31'.format(stat_date)

            stat_date = to_date(stat_date)
        else:
            today = datetime.date.today()
            yesteryear = today.year - 1
            stat_date = datetime.date(yesteryear, 12, 31)
    elif stat_date:
        if isinstance(stat_date, (str, six.string_types)):
            stat_date = stat_date.lower()
            if 'q' in stat_date:
                stat_date = (stat_date.replace('q1', '-03-31')
                             .replace('q2', '-06-30')
                             .replace('q3', '-09-30')
                             .replace('q4', '-12-31'))
            else:
                year = int(stat_date)
                by_year = True
                stat_date = '%s-12-31' % year
        elif isinstance(stat_date, int):
            year = int(stat_date)
            by_year = True
            stat_date = '%s-12-31' % year

        stat_date = to_date(stat_date)

    # 不晚于 stat_date 的一个交易日
    trade_day_not_after_stat_date = None
    for table in tables:
        if date:
            query_object = query_object.filter(table.day == date)
        else:
            if hasattr(table, 'statDate'):
                query_object = query_object.filter(table.statDate == stat_date)
            else:
                # 估值表, 在非交易日没有数据
                # 所以如果传入的非交易日, 就需要取得前一个交易日
                assert table is StockValuation
                if trade_day_not_after_stat_date is None:
                    trade_day_not_after_stat_date = CalendarService.get_previous_trade_date(stat_date)
                query_object = query_object.filter(table.day == trade_day_not_after_stat_date)

    # 连表
    for table in tables[1:]:
        query_object = query_object.filter(table.code == tables[0].code)

    # 恢复 offset, limit
    query_object = query_object.offset(offset)
    query_object = query_object.limit(limit)
    sql = compile_query(query_object)

    if stat_date:
        if by_year:
            sql = sql.replace('balance_sheet_day', 'balance_sheet')\
                     .replace('financial_indicator_day', 'financial_indicator_acc')\
                     .replace('income_statement_day', 'income_statement_acc')\
                     .replace('cash_flow_statement_day', 'cash_flow_statement_acc')
        else:
            for t in ('balance_sheet_day', 'financial_indicator_day', 'income_statement_day',
                      'cash_flow_statement_day'):
                sql = sql.replace(t, t[:-4])
        sql = re.sub(r'(cash_flow_statement|balance_sheet|income_statement|financial_indicator|'
                     r'financial_indicator_acc|income_statement_acc|cash_flow_statement_acc)\.`?day`?\b',
                     r'\1.statDate', sql)
    return sql


def fundamentals_redundant_continuously_query_to_sql(query, trade_day):
    '''
    根据传入的查询对象和起始时间生成sql
    trade_day是要查询的交易日列表
    '''

    from .fundamentals_tables_gen import (
        BalanceSheet, IncomeStatement, CashFlowStatement, FinancialIndicator,
        BankIndicatorAcc, SecurityIndicatorAcc, InsuranceIndicatorAcc, StockValuation)

    limit = min(FUNDAMENTAL_RESULT_LIMIT, query._limit or FUNDAMENTAL_RESULT_LIMIT)
    offset = query._offset
    query._offset = None
    query._limit = None

    def get_table_class(tablename):
        for t in (BalanceSheet, CashFlowStatement, FinancialIndicator,
                  IncomeStatement, StockValuation, BankIndicatorAcc, SecurityIndicatorAcc,
                  InsuranceIndicatorAcc):
            if t.__tablename__ == tablename:
                return t

    def get_tables_from_sql(sql):
        m = re.findall(
            r'cash_flow_statement_day|balance_sheet_day|financial_indicator_day|'
            r'income_statement_day|stock_valuation|bank_indicator_acc|security_indicator_acc|'
            r'insurance_indicator_acc', sql)
        return list(set(m))
    # 从query对象获取表对象
    tablenames = get_tables_from_sql(str(query.statement))
    tables = [get_table_class(name) for name in tablenames]
    query = query.filter(StockValuation.day.in_(trade_day))
    # 根据stock valuation 表的code和day字段筛选
    for table in tables:
            if table is not StockValuation:
                query = query.filter(StockValuation.code == table.code)
                if hasattr(table, 'day'):
                    query = query.filter(StockValuation.day == table.day)
                else:
                    query = query.filter(StockValuation.day == table.statDate)

    # 连表
    for table in tables[1:]:
        query = query.filter(table.code == tables[0].code)

    # 恢复 offset, limit
    query = query.offset(offset)
    query = query.limit(limit)
    # query = query.subquery()
    sql = compile_query(query)
    # 默认添加查询code和day作为panel索引
    sql = sql.replace('SELECT ', 'SELECT DISTINCT stock_valuation.day AS day,stock_valuation.code as code, ')
    return sql


def get_continuously_query_to_sql(query, trade_day):
    '''
    根据传入的查询对象和起始时间生成sql
    trade_day是要查询的交易日列表
    '''

    limit = min(FUNDAMENTAL_RESULT_LIMIT, query._limit or FUNDAMENTAL_RESULT_LIMIT)
    # limit = min(1e5, query._limit or 1e5)
    offset = query._offset
    query._offset = None
    query._limit = None

    def get_table_class(tablename):
        for t in (BalanceSheet, CashFlowStatement, FinancialIndicator,
                  IncomeStatementDay, StockValuation, BankIndicatorAcc, SecurityIndicatorAcc,
                  InsuranceIndicatorAcc):
            if t.__tablename__ == tablename:
                return t

    def get_tables_from_sql(sql):
        m = re.findall(
            r'cash_flow_statement|balance_sheet|financial_indicator|'
            r'income_statement|stock_valuation|bank_indicator_acc|security_indicator_acc|'
            r'insurance_indicator_acc', sql)
        return list(set(m))
    # 从query对象获取表对象
    tablenames = get_tables_from_sql(str(query.statement))
    tables = [get_table_class(name) for name in tablenames]
    query = query.filter(StockValuation.day.in_(trade_day))
    # 根据stock valuation 表的code和day字段筛选
    for table in tables:
            if table is StockValuation:
                query = query.filter(StockValuation.code == table.code)
                query = query.filter(StockValuation.day >= table.periodStart)
                query = query.filter(StockValuation.day <= table.periodEnd)

    # 连表
    for table in tables[1:]:
        query = query.filter(table.code == tables[0].code)

    # 恢复 offset, limit
    query = query.offset(offset)
    query = query.limit(limit)
    sql = compile_query(query)
    # 默认添加查询code和day作为panel索引
    sql = sql.replace('SELECT ', 'SELECT DISTINCT stock_valuation.day AS day,stock_valuation.code as code, ')
    return sql


balance = balance_sheet = BalanceSheetDay
income = income_statement = IncomeStatementDay
cash_flow = cash_flow_statement = CashFlowStatementDay
indicator = financial_indicator = FinancialIndicatorDay

bank_indicator = bank_indicator_acc = BankIndicatorAcc
security_indicator = security_indicator_acc = SecurityIndicatorAcc
insurance_indicator = insurance_indicator_acc = InsuranceIndicatorAcc

valuation = stock_valuation = StockValuation


__all__ = ["query", "balance", "income", "cash_flow", 
            "indicator", "bank_indicator", "security_indicator", 
            "insurance_indicator", "valuation"]


