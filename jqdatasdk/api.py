# coding=utf-8

from io import StringIO
import requests
import pandas as pd
from .utils import *  # noqa
from .client import JQDataClient


@assert_auth
def get_price(security, start_date=None, end_date=None, frequency='daily', fields=None,
              skip_paused=False, fq='pre', count=None, panel=True, fill_paused=True, round=True):
    """
    获取一支或者多只证券的行情数据

    :param security 一支证券代码或者一个证券代码的list
    :param count 与 start_date 二选一，不可同时使用.数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据
    :param start_date 与 count 二选一，不可同时使用. 字符串或者 datetime.datetime/datetime.date 对象, 开始时间
    :param end_date 格式同上, 结束时间, 默认是'2015-12-31', 包含此日期.
    :param frequency 单位时间长度, 几天或者几分钟, 现在支持'Xd','Xm', 'daily'(等同于'1d'), 'minute'(等同于'1m'), X是一个正整数, 分别表示X天和X分钟
    :param fields 字符串list, 默认是None(表示['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段), 支持以下属性 ['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit', 'low_limit', 'avg', 'pre_close', 'paused']
    :param skip_paused 是否跳过不交易日期(包括停牌, 未上市或者退市后的日期). 如果不跳过, 停牌时会使用停牌前的数据填充, 上市前或者退市后数据都为 nan
    :param panel: 当传入一个标的列表的时候，是否返回一个panel对象，默认为True，表示返回一个panel对象
           注意：
               当security为一个标的列表，且panel=False的时候，会返回一个dataframe对象，
               在这个对象中额外多出code、time两个字段，分别表示该条数据对应的标的、时间
    :param fill_paused : False 表示使用NAN填充停牌的数据，True表示用close价格填充，默认True
    :return 如果是一支证券, 则返回pandas.DataFrame对象, 行索引是datetime.datetime对象, 列索引是行情字段名字; 如果是多支证券, 则返回pandas.Panel对象, 里面是很多pandas.DataFrame对象, 索引是行情字段(open/close/…), 每个pandas.DataFrame的行索引是datetime.datetime对象, 列索引是证券代号.
    """
    if panel and PandasChecker.check_version():
        panel = False
    security = convert_security(security)
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    if (not count) and (not start_date):
        start_date = "2015-01-01"
    if count and start_date:
        raise ParamsError("(start_date, count) only one param is required")
    return JQDataClient.instance().get_price(**locals())


@assert_auth
def get_price_engine(security, start_date=None, end_date=None,
                     frequency='daily', fields=None, skip_paused=False,
                     fq='pre', count=None, pre_factor_ref_date=None):
    security = convert_security(security)
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    pre_factor_ref_date = to_date_str(end_date)
    return JQDataClient.instance().get_price_engine(**locals())


@assert_auth
def get_extras(info, security_list, start_date=None, end_date=None, df=True, count=None):
    """
    得到多只标的在一段时间的如下额外的数据

    :param info ['is_st', 'acc_net_value', 'unit_net_value', 'futures_sett_price', 'futures_positions'] 中的一个
    :param security_list 证券列表
    :param start_date 开始日期
    :param end_date 结束日期
    :param df 返回pandas.DataFrame对象还是一个dict
    :param count 数量, 与 start_date 二选一, 不可同时使用, 必须大于 0
    :return <df=True>:pandas.DataFrame对象, 列索引是股票代号, 行索引是datetime.datetime；<df=False>:一个dict, key是基金代号, value是numpy.ndarray
    """
    assert security_list, "security_list is required"
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    security_list = convert_security(security_list)
    return JQDataClient.instance().get_extras(**locals())


@assert_auth
def get_fundamentals(query_object, date=None, statDate=None):
    """
    查询财务数据, 详细的数据字段描述在 https://www.joinquant.com/data/dict/fundamentals 中查看

    :param query_object 一个sqlalchemy.orm.query.Query对象
    :param date 查询日期, 一个字符串(格式类似’2015-10-15’)或者datetime.date/datetime.datetime对象,
                可以是None, 使用默认日期
    :param statDate: 财报统计的季度或者年份, 一个字符串, 有两种格式:1.季度: 格式是: 年 + ‘q’ + 季度序号,
                     例如: ‘2015q1’, ‘2013q4’. 2.年份: 格式就是年份的数字, 例如: ‘2015’, ‘2016’.
    :return 返回一个 pandas.DataFrame, 每一行对应数据库返回的每一行(可能是几个表的联合查询结果的一行),
            列索引是你查询的所有字段;为了防止返回数据量过大, 我们每次最多返回10000行;
            当相关股票上市前、退市后，财务数据返回各字段为空
    """
    if date:
        date = to_date(date)
    if date is None and statDate is None:
        date = datetime.date.today() - datetime.timedelta(days=1)

    from .finance_service import get_fundamentals_sql
    sql = get_fundamentals_sql(query_object, date, statDate)
    if date == datetime.date.today() or date == datetime.date.today().strftime("%Y-%m-%d"):
        """ 当天的数据可能变化,不用缓存 """
        return JQDataClient.instance().get_fundamentals(sql=sql)
    return exec_fundamentals(sql)

@hashable_lru(maxsize=3)
def exec_fundamentals(sql):
    return JQDataClient.instance().get_fundamentals(sql=sql)


@assert_auth
@hashable_lru(maxsize=3)
def get_fundamentals_continuously(query_object, end_date=None, count=1, panel=True):
    """
    查询财务数据，详细的数据字段描述在 https://www.joinquant.com/data/dict/fundamentals 中查看
    :param query_object:一个sqlalchemy.orm.query.Query对象
    :param end_date:查询日期, 一个字符串(格式类似’2015-10-15’)或者datetime.date/datetime.datetime对象, 可以是None, 使用默认日期
    :param count:获取 end_date 前 count 个日期的数据
    :param panel:是否返回panel对象，默认为True，表示返回panel对象。
    :return
    :panel=true: pd.Panel, 三维分别是 field, date, security.
    :panel=False: pd.Fataframe, index是pandas默认的整数，并且始终会返回'day', 'code'这两个字段
    """
    assert count, "count is required"
    from .finance_service import fundamentals_redundant_continuously_query_to_sql
    from .calendar_service import CalendarService

    if panel and PandasChecker.check_version():
        panel = False

    trade_days = CalendarService.get_trade_days(end_date=end_date, count=count)
    sql = fundamentals_redundant_continuously_query_to_sql(query_object, trade_days)
    sql = remove_duplicated_tables(sql)
    df = JQDataClient.instance().get_fundamentals_continuously(sql=sql)
    if panel:
        newdf = df.set_index(['day', 'code'])
        pan = newdf.to_panel()
        return pan
    else:
        try:
            df.sort(columns=['code', 'day'], inplace=True)
        except AttributeError:
            df.sort_values(by=['code', 'day'], inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df

@assert_auth
@hashable_lru(maxsize=3)
def get_valuation(security_list, start_date=None, end_date=None, fields=None, count=None):
    """ 获取多个标的在指定交易日范围内的市值表数据
    Args:
        security_list: 标的code字符串列表或者单个标的字符串
        end_date: 查询结束时间
        start_date: 查询开始时间，不能与count共用
        count: 表示往前查询每一个标的count个交易日的数据，如果期间标的停牌，则该标的返回的市值数据数量小于count
        fields: 财务数据中市值表的字段，返回结果中总会包含code、day字段，可用字段如下：
            code	股票代码	带后缀.XSHE/.XSHG
            day	日期	取数据的日期
            capitalization	总股本(万股)
            circulating_cap	流通股本(万股)
            market_cap	总市值(亿元)
            circulating_market_cap	流通市值(亿元)
            turnover_ratio	换手率(%)
            pe_ratio	市盈率(PE, TTM)
            pe_ratio_lyr	市盈率(PE)s
            pb_ratio	市净率(PB)
            ps_ratio	市销率(PS, TTM)
            pcf_ratio	市现率(PCF, 现金净流量TTM)
    Returns:
        返回一个dataframe，索引默认是pandas的整数索引，返回的结果中总会包含code、day字段。
    """
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    security_list = convert_security(security_list)
    return JQDataClient.instance().get_valuation(**locals())


@assert_auth
def get_history_fundamentals(security, fields, watch_date=None, stat_date=None,
                             count=1, interval='1q', stat_by_year=False):
    """ 获取多个季度/年度的三大财务报表和财务指标数据. 可指定单季度数据, 也可以指定年度数据.
            可以指定观察日期, 也可以指定最后一个报告期的结束日期.
    Args:
        security: 股票代码或者股票代码列表。
        fields: 要查询的财务数据的列, 季度数据和年度数据可选择的列不同. 示例:
            [
                balance.cash_equivalents,
                cash_flow.net_deposit_increase,
                income.total_operating_revenue,
            ]
        watch_date: 观察日期, 如果指定, 将返回 watch_date 日期前(包含该日期)发布的报表数据
        stat_date: 统计日期, 可以是 '2019'/'2019q1'/'2018q4' 等格式, 如果指定, 将返回 stat_date 对应报告期及之前的历史报告期的报表数据,
            注意: watch_date 和 stat_date 只能指定一个, 而且必须指定一个
                如果没有 stat_date 指定报告期的数据, 则该数据会缺失一行.
        count: 查询历史的多个报告期时, 指定的报告期数量. 如果股票历史报告期的数量小于 count, 则该股票返回的数据行数将小于 count
        interval: 查询多个报告期数据时, 指定报告期间隔, 可选值: '1q'/'1y', 表示间隔一季度或者一年, 举例说明:
            stat_date='2019q1', interval='1q', count=4, 将返回 2018q2,2018q3,2018q4,2019q1 的数据
            stat_date='2019q1', interval='1y', count=4, 将返回 2016q1,2017q1,2018q1,2019q1 的数据
            stat_by_year=True, stat_date='2018', interval='1y', count=4 将返回 2015/2016/2017/2018 年度的年报数据
        stat_by_year: bool, 是否返回年度数据. 默认返回的按季度统计的数据(比如income表中只有单个季度的利润).
            如果返回年度数据:
                interval必须是 '1y'
                如果指定了 stat_date 的话, stat_date 必须是一个数字, 表明统计的年份
            stat_by_year 是 True 时, fields 可以选择 balance/income/cash_flow/indicator/bank_indicator/security_indicator/insurance_indicator 表中的列
                        是 False 时, fields 可以选择 balance/income/cash_flow/indicator 表中的列
    Returns:
        pandas.DataFrame, 数据库查询结果. 数据格式同 get_fundamentals. 每个股票每个报告期(一季度或者一年)的数据占用一行.
    Others:
        推荐用户对结果使用df.groupby来进行分组分析数据
    """
    assert security, "security is required"
    assert fields, "fields is required"
    assert (not watch_date) or (not stat_date), "watch_date与stat_date有且只能有一个不是None"
    assert watch_date or stat_date, "watch_date与stat_date有且只能有一个不是None"

    watch_date = to_date_str(watch_date)
    security = convert_security(security)
    fields = convert_fields_to_str(fields)
    return JQDataClient.instance().get_history_fundamentals(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_billboard_list(stock_list=None, start_date=None, end_date=None, count=None):
    """
    获取指定日期区间内的龙虎榜数据

    :param stock_list:一个股票代码的 list。 当值为 None 时， 返回指定日期的所有股票。
    :param start_date:开始日期
    :param end_date:结束日期
    :param count:交易日数量， 可以与 end_date 同时使用， 表示获取 end_date 前 count 个交易日的数据(含 end_date 当日)
    :return:回一个 pandas.DataFrame
    """
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    stock_list = convert_security(stock_list)
    return JQDataClient.instance().get_billboard_list(**locals())


@assert_auth
def get_locked_shares(stock_list=None, start_date=None, end_date=None, forward_count=None):
    """
    获取指定日期区间内的限售解禁数据

    :param stock_list:一个股票代码的 list
    :param start_date:开始日期
    :param end_date:结束日期
    :param forward_count:交易日数量， 可以与 start_date 同时使用， 表示获取 start_date 到 forward_count 个交易日区间的数据
    :return:
    """
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    stock_list = convert_security(stock_list)
    return JQDataClient.instance().get_locked_shares(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_index_stocks(index_symbol, date=today()):
    """
    获取一个指数给定日期在平台可交易的成分股列表，请点击 https://www.joinquant.com/indexData 查看指数信息

    :param index_symbol 指数代码
    :param date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者datetime.date/datetime.datetime对象, 可以是None, 使用默认日期.
    :return 股票代码的list
    """
    assert index_symbol, "index_symbol is required"
    date = to_date_str(date)
    return JQDataClient.instance().get_index_stocks(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_industry_stocks(industry_code, date=today()):
    """
    获取在给定日期一个行业的所有股票，行业分类列表见 https://www.joinquant.com/data/dict/plateData

    :param industry_code 行业编码
    :param date 查询日期, 一个字符串(格式类似’2015-10-15’)或者datetime.date/datetime.datetime对象, 可以是None, 使用默认日期.
    :return 股票代码的list
    """
    assert industry_code, "industry_code is required"
    date = to_date_str(date)
    return JQDataClient.instance().get_industry_stocks(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_industries(name='zjw', date=None):
    """
    按照行业分类获取行业列表
    :param name:行业代码
    :param date:获取数据的日期，默认为None
    :return:pandas.DataFrame, 各column分别为行业代码、行业名称、开始日期
    """
    assert name, "name is required"
    date = to_date_str(date)
    return JQDataClient.instance().get_industries(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_concept_stocks(concept_code, date=today()):
    """
    获取在给定日期一个概念板块的所有股票，概念板块分类列表见 https://www.joinquant.com/data/dict/plateData

    :param concept_code 概念板块编码
    :param date: 查询日期, 一个字符串(格式类似’2015-10-15’)或者datetime.date/datetime.datetime对象, 可以是None, 使用默认日期.
    :return 股票代码的list
    """
    assert concept_code, "concept_code is required"
    date = to_date_str(date)
    return JQDataClient.instance().get_concept_stocks(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_concepts():
    """
    获取概念板块
    :return:pandas.DataFrame, 各column分别为概念代码、概念名称、开始日期
    """
    return JQDataClient.instance().get_concepts(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_concept(security, date):
    """
    获取股票所属概念板块。

    :param security 标的代码或标的列表
    :param date 要查询的提起, 日期字符串/date对象/datetime对象, 注意传入datetime对象时忽略日内时间
    :return:返回dict, key为标的代码, value为概念板块信息
    """
    date = to_date_str(date)
    return JQDataClient.instance().get_concept(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_all_securities(types=[], date=None):
    """
    获取平台支持的所有股票、基金、指数、期货信息

    :param types list: 用来过滤securities的类型, list元素可选: ‘stock’, ‘fund’, ‘index’, ‘futures’, ‘etf’, ‘lof’, ‘fja’, ‘fjb’. types为空时返回所有股票, 不包括基金,指数和期货
    :param date 日期, 一个字符串或者 datetime.datetime/datetime.date 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息
    :return pandas.DataFrame
    """
    date = to_date_str(date)
    return JQDataClient.instance().get_all_securities(**locals())


def get_all_securities2(types=[], date=None, exchange=None):
    """
    获取平台支持的所有股票、基金、指数、期货、期权等信息

    :param types list: 用来过滤 securities 的类型, list 元素可选:
        stock, fund, index, futures, etf, lof, fja, fjb.
        types 为空时返回所有股票, 即不包括基金, 指数和期货等
    :param date 日期, 一个日期字符串或者 datetime.datetime/datetime.date 对象,
        用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息
    :param exchange: 用来过滤交易所，可以一个字符串，多个交易所时用逗号分割，或者为一个 list
    :return pandas.DataFrame
    """
    df = get_all_securities(types, date)
    if not exchange:
        return df

    exchanges = tuple(
        exchange.split(',') if isinstance(exchange, six.string_types)
        else exchange
    )
    return df[df.index.str.endswith(exchanges)]


@assert_auth
@hashable_lru(maxsize=3)
def get_security_info(code, date=None):
    """
    获取股票/基金/指数的信息

    :param code 证券代码
    :param date 查询日期: 日期字符串/date对象/datetime对象, 注意传入datetime对象时忽略日内时间
    :return Security
    """
    assert code, "code is required"
    date = to_date_str(date)
    result = JQDataClient.instance().get_security_info(**locals())
    if result:
        return Security(**result)


@assert_auth
@hashable_lru(maxsize=3)
def get_security_info2(code, date=None):
    """
    获取标的信息

    :param code 证券代码
    :param date 查询日期: 日期字符串/date对象/datetime对象, 注意传入datetime对象时忽略日内时间
    :return Security2
    """
    assert code, "code is required"
    date = to_date_str(date)
    result = JQDataClient.instance().get_security_info(**locals())
    if result:
        return Security2(**result)


@assert_auth
@hashable_lru(maxsize=3)
def get_all_trade_days():
    """
    获取所有交易日

    :return 包含所有交易日的 numpy.ndarray, 每个元素为一个 datetime.date 类型.
    """
    data = JQDataClient.instance().get_all_trade_days()
    if str(data.dtype) != "object":
        data = data.astype(datetime.datetime)
    return data


@assert_auth
@hashable_lru(maxsize=3)
def get_trade_days(start_date=None, end_date=None, count=None):
    """
    获取指定日期范围内的所有交易日

    :return numpy.ndarray, 包含指定的 start_date 和 end_date, 默认返回至 datatime.date.today() 的所有交易日
    """
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    data = JQDataClient.instance().get_trade_days(**locals())
    if str(data.dtype) != "object":
        data = data.astype(datetime.datetime)
    return data


@assert_auth
@hashable_lru(maxsize=3)
def get_money_flow(security_list, start_date=None, end_date=None, fields=None, count=None):
    """
    获取一只或者多只股票在一个时间段内的资金流向数据

    :param security_list 一只股票代码或者一个股票代码的 list
    :param start_date 开始日期, 与 count 二选一, 不可同时使用, 一个字符串或者 datetime.datetime/datetime.date 对象, 默认为平台提供的数据的最早日期
    :param end_date 结束日期, 一个字符串或者 datetime.date/datetime.datetime 对象, 默认为 datetime.date.today()
    :param count 数量, 与 start_date 二选一，不可同时使用, 必须大于 0. 表示返回 end_date 之前 count 个交易日的数据, 包含 end_date
    :param fields 字段名或者 list, 可选
    :return pandas.DataFrame
    """
    assert security_list, "security_list is required"
    security_list = convert_security(security_list)
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return JQDataClient.instance().get_money_flow(**locals())


@assert_auth
def get_money_flow_pro(security_list, start_date=None, end_date=None,
                       frequency='daily', fields=None, count=None, data_type='money'):
    """
    获取资金流向数据, 停牌时无数据

    :param security_list 标的列表或单个标的代码的字符串
    :param end_date 数据截止日期, 必须指定
    :param start_date/count 二选一, start_date 和 end_date 可以精确到分钟, count 代表 end_date 往前推的交易日/分钟个数, 且单次数据返回条数小于200万条(获取分钟数据时, 单次获取的数据区间不可超过30个交易日)
    :param frequency 只支持 minutes/1m 或 daily/1d ;数据按天储存,建议按天进行获取
    :param fields 支持 ['inflow_xl', 'inflow_l', 'inflow_m', 'inflow_s', 'outflow_xl', 'outflow_l', 'outflow_m', 'outflow_s', 'netflow_xl', 'netflow_l', 'netflow_m', 'netflow_s'] , netflow = inflow - outflow, 默认不返回
    :param data_type 统计字段三选一 (1) money 成交额 (2) volume 成交量 (3) deal 成交笔数

    :return dataframe, columns 是 time, code 以及对应的 fields(处理后的)
    总是返回 time(timestamp), 当 securiy_list 为多个标的时总是返回 code
    """
    assert security_list, "security_list is required"
    security_list = convert_security(security_list)
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    if (not count) and (not start_date):
        start_date = "2015-01-01"
    if count and start_date:
        raise ParamsError("(start_date, count) only one param is required")
    return JQDataClient.instance().get_money_flow_pro(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_mtss(security_list, start_date=None, end_date=None, fields=None, count=None):
    """
    获取一只或者多只股票在一个时间段内的融资融券信息

    :param security_list 一只股票代码或者一个股票代码的 list
    :param start_date 开始日期, 与 count 二选一, 不可同时使用.
    :param end_date 结束日期, 一个字符串或者 datetime.date/datetime.datetime 对象, 默认为 datetime.date.today()
    :param count 数量, 与 start_date 二选一，不可同时使用, 必须大于 0. 表示返回 end_date 之前 count 个交易日的数据, 包含 end_date
    :param fields 字段名或者 list, 可选. 默认为 None, 表示取全部字段
    :return pandas.DataFrame
    """
    assert (not start_date) ^ (not count), "(start_date, count) only one param is required"
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    security_list = convert_security(security_list)
    return JQDataClient.instance().get_mtss(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_margincash_stocks(date=None):
    """
    返回上交所、深交所最近一次披露的的可融资标的列表的list
    :return: list
    """
    date = to_date_str(date)
    return JQDataClient.instance().get_margincash_stocks(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_marginsec_stocks(date=None):
    """
    返回上交所、深交所最近一次披露的的可融券标的列表的list
    :return:list
    """
    date = to_date_str(date)
    return JQDataClient.instance().get_marginsec_stocks(**locals())


@assert_auth
def get_future_contracts(underlying_symbol, date=None):
    """
    获取某期货品种在策略当前日期的可交易合约标的列表

    :param security 期货合约品种，如 ‘AG’(白银)
    :return 某期货品种在策略当前日期的可交易合约标的列表
    """
    assert underlying_symbol, "underlying_symbol is required"
    dt = to_date_str(date)
    return JQDataClient.instance().get_future_contracts(underlying_symbol=underlying_symbol, dt=dt)


@assert_auth
def get_dominant_future(underlying_symbol, date=None, end_date=None):
    """
    获取主力合约对应的标的

    :param underlying_symbol 期货合约品种，如 ‘AG’(白银)
    :param date 日期（默认为当前时刻，当指定 end_date 时则表示开始日期）
    :param end_date 结束日期，当指定该参数时表示获取一段时间的主力合约
    :return 主力合约对应的期货合约（指定 end_date 时返回 pandas.Series，否则返回字符串）
    """
    dt = to_date_str(date)
    cli = JQDataClient.instance()
    if not end_date:
        return cli.get_dominant_future(underlying_symbol=underlying_symbol, dt=dt)
    end_dt = to_date_str(end_date)
    return cli.get_dominant_future(underlying_symbol=underlying_symbol, dt=dt, end_dt=end_dt)


@assert_auth
def get_ticks(security, start_dt=None, end_dt=None, count=None, fields=None, skip=True, df=True):
    """
    获取tick数据
    :param security: 股票or期货标的代码,仅限单只
    :param start_dt: 开始日期
    :param end_dt: 截止日期
    :param count: 统计个数
    :param fields: 期货：[time current high low volume money position a1_v a1_p b1_v b1_p]
                    股票：[time current high low volume money a1_v-a5_v a1_p-a5_p b1_v-b5_v b1_p-b5_p]
                    为None时，默认返回对应类型的所有字段
    :param skip: 是否过滤掉无成交的tick
    :param df: 默认为True，传入单个标的返回的是一个dataframe, 当df=False的时候，当单个标的的时候，返回一个np.ndarray
    :return:
    """
    start_dt = to_date_str(start_dt)
    end_dt = to_date_str(end_dt)
    return JQDataClient.instance().get_ticks(**locals())


@assert_auth
def get_ticks_engine(security, start_dt=None, end_dt=None, count=None, fields=None):
    start_dt = to_date_str(start_dt)
    end_dt = to_date_str(end_dt)
    return JQDataClient.instance().get_ticks_engine(**locals())


@assert_auth
def get_baidu_factor(category=None, day=None, stock=None, province=None):
    """
    获取百度因子搜索量数据
    :param category:数据类别，中证800的数据类别为"csi800"
    :param stock: 一只股票或一个股票list。如果为空，则包含中证800所有的成分股。
    :param day:日期，date、datetime或字符串类型。如果day为空，则返回最新的数据。
    :param province:省份名称或省份代码，如北京或110000。如果为空，则返回PC端和手机端的数据汇总。
    如果不为空，则返回指定省份的数据。
    :return:
    """

    day = to_date_str(day)
    stock = normal_security_code(stock)
    return JQDataClient.instance().get_baidu_factor(**locals())


@assert_auth
def normalize_code(code):
    """
    归一化证券代码

    :param code 如000001
    :return 证券代码的全称 如000001.XSHE
    """
    return JQDataClient.instance().normalize_code(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_factor_values(securities, factors, start_date=None, end_date=None, count=None):
    """
    获取因子数据

    返回字典类型
    :return:
    """

    securities = convert_security(securities)
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    if (not count) and (not start_date):
        start_date = "2015-01-01"
    if count and start_date:
        raise ParamsError("(start_date, count) only one param is required")
    return JQDataClient.instance().get_factor_values(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_index_weights(index_id, date=None):
    """
    获取指数成分股权重

    :param index_id 必选参数，代表指数的标准形式代码
    :param date 可选参数， 查询权重信息的日期
    :return
    """
    assert index_id, "index_id is required"
    date = to_date_str(date)
    return JQDataClient.instance().get_index_weights(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_industry(security, date=None, df=False):
    """
    查询股票所属行业

    :param security 标的代码
    :date 查询的日期，默认为空
    :df 是否返回 DataFrame 类型
    :return 返回类型, dict 或 DataFrane
    """
    assert security, "security is required"
    security = convert_security(security)
    date = to_date_str(date)
    return JQDataClient.instance().get_industry(**locals())


@assert_auth
def get_bars(security, count=None, unit="1d", fields=("date", "open", "high", "low", "close"),
             include_now=False, end_dt=None, fq_ref_date=None, df=True,
             start_dt=None, skip_paused=True):
    """
    获取历史数据(包含快照数据), 可查询单个标的多个数据字段

    :param security 股票代码
    :param count 大于0的整数，表示获取bar的个数。如果行情数据的bar不足count个，返回的长度则小于count个数。
    :param unit bar的时间单位, 支持如下周期：'1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'。'1w' 表示一周，‘1M' 表示一月。
    :param fields 获取数据的字段， 支持如下值：'date', 'open', 'close', 'high', 'low', 'volume', 'money'
    :param include_now 取值True 或者False。 表示是否包含当前bar, 比如策略时间是9:33，unit参数为5m， 如果 include_now=True,则返回9:30-9:33这个分钟 bar。
    :param end_dt: 查询的截止时间
    :param fq_ref_date: 复权基准日期，为None时为不复权数据
    :param df: 默认为True，传入单个标的返回的是一个dataframe，传入多个标的返回的是一个multi-index dataframe
            当df=False的时候，当单个标的的时候，返回一个np.ndarray，多个标的返回一个字典，key是code，value是np.array；
    :param start_dt: 查询的开始时间
    :param skip_paused: 是否跳过停牌
    :return numpy.ndarray格式
    """
    assert security, "security is required"
    security = convert_security(security)
    end_dt = to_date_str(end_dt)
    fq_ref_date = to_date_str(fq_ref_date)
    return JQDataClient.instance().get_bars(**locals())


@assert_auth
def get_bars_engine(security, count, unit="1d", fields=("open", "high", "low", "close"), include_now=False, end_dt=None,
                    fq_ref_date=None):
    security = convert_security(security)
    fq_ref_date = to_date_str(fq_ref_date)
    if not (isinstance(security, six.string_types) or isinstance(security, (tuple, list))):
        raise Exception('security 必须是字符串 或者 字符串数组')
    end_dt = to_date_str(end_dt)
    return JQDataClient.instance().get_bars_engine(**locals())


def get_current_tick(security):
    """
    获取最新的 tick 数据

    :param security 标的代码
    :return:
    """
    if not JQDataClient.instance() or JQDataClient.instance().get_http_token() == "":
        raise Exception("Please run jqdatasdk.auth first")

    if isinstance(security, six.string_types):
        security = [security]
    elif isinstance(security, Security):
        security = [str(security)]
    res = request_data(security)
    if not res or res.text == "":
        return None
    content = res.text
    if content[:5] == 'error':
        if content in ["error: token无效，请重新获取","error: token过期，请重新获取"]:
            JQDataClient.instance().set_http_token()
            res = request_data(security)  # 重试一次
            if not res or res.text == "":
                return None
            content = res.text
            if content[:5] == 'error':
                raise Exception(content)
        else:
            raise Exception(content)

    stock_tick_fields = ['datetime', 'current', 'high', 'low', 'volume', 'money',
                         'a1_p', 'a1_v', 'a2_p', 'a2_v', 'a3_p', 'a3_v', 'a4_p', 'a4_v', 'a5_p', 'a5_v',
                         'b1_p', 'b1_v', 'b2_p', 'b2_v', 'b3_p', 'b3_v', 'b4_p', 'b4_v', 'b5_p', 'b5_v']
    option_tick_fields = ['datetime', 'current', 'high', 'low', 'volume', 'money', 'position',
                         'a1_v', 'a2_v', 'a3_v', 'a4_v', 'a5_v', 'a1_p', 'a2_p', 'a3_p', 'a4_p', 'a5_p',
                         'b1_v', 'b2_v', 'b3_v', 'b4_v', 'b5_v', 'b1_p', 'b2_p', 'b3_p', 'b4_p', 'b5_p']
    future_tick_fields = ['datetime', 'current', 'high', 'low', 'volume', 'money', 'position', 'a1_p', 'a1_v', 'b1_p', 'b1_v']
    index_tick_fields = ['datetime', 'current', 'high', 'low', 'volume', 'money']

    tick_fields_list = [stock_tick_fields,future_tick_fields,stock_tick_fields,index_tick_fields,option_tick_fields]
    # content[0]返回数据第一个字符为标的类型  "0":"stock","1":"future","2":"fund","3":"index","4":"option"
    tick_fields = tick_fields_list[int(content[0])]

    str2time = lambda x: datetime.datetime.strptime(x, '%Y%m%d%H%M%S.%f') if x else pd.NaT
    data = StringIO(content)
    data.seek(1)  # 跳过第一个字符，从第二个开始取数据
    df = pd.read_csv(data, index_col=0, converters={"datetime": str2time})
    df = df[tick_fields]
    if len(security) <= 1:
        df.index = [0]
    return df

def request_data(security):
    http_token = JQDataClient.instance().get_http_token()
    codes = ",".join(security)
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive'
    }
    body = {
        "method": "get_current_ticks2",
        "token": http_token,
        "code": codes
    }
    data_api_url = JQDataClient.instance().get_data_api_url()
    res = requests.post(
        data_api_url,
        data=json.dumps(body),
        headers=headers,
        timeout=JQDataClient.request_timeout
    )
    return res

@assert_auth
def get_current_tick_engine(security):
    assert security, "security is required"
    if not (isinstance(security, six.string_types) or isinstance(security, (tuple, list))):
        raise Exception('security 必须是字符串 或者 字符串数组')
    security = convert_security(security)
    return JQDataClient.instance().get_current_tick_engine(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_fund_info(security, date=None):
    """
    基金基础信息数据接口

    :param security 基金代码
    :param date 查询日期
    :return 字典格式
    """
    assert security, "security is required"
    security = convert_security(security)
    date = to_date_str(date)
    return JQDataClient.instance().get_fund_info(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_futures_info(securities=None, fields=('contract_multiplier',
                                              'tick_size',
                                              'trade_time')):
    """
    期货信息数据接口

    :param securities: 一个或多个标的
    :param fields: 期货属性字段：['contract_multiplier', 'tick_size', 'trade_time']
    :return: {}
    """
    assert securities, "securities is required"
    securities = convert_security(securities)
    return JQDataClient.instance().get_futures_info(**locals())


@assert_auth
def get_query_count(field=None):
    """
    查询当日可请求条数/剩余请求条数

    :param field
        默认为None，返回当日可请求条数/剩余请求条数，字典格式
        "total", 返回当日可请求条数, int格式
        "spare", 返回当日剩余请求条数, int格式
    """
    assert field in ["total", "spare", None], "field参数必须为total,spare,None中的一个"
    return JQDataClient.instance().get_query_count(**locals())


@assert_auth
def history_engine(end_dt, count, unit='1d', field='avg', security_list=None,
                   df=True, skip_paused=False, fq='pre', pre_factor_ref_date=None):
    security_list = convert_security(security_list)
    end_dt = to_date_str(end_dt)
    pre_factor_ref_date = to_date_str(pre_factor_ref_date)
    return JQDataClient.instance().history_engine(**locals())


@assert_auth
def attribute_history_engine(end_dt, security, count, unit='1d',
                             fields=('open', 'close', 'high', 'low', 'volume', 'money'),
                             skip_paused=True,
                             df=True,
                             fq='pre',
                             pre_factor_ref_date=None):
    security = convert_security(security)
    end_dt = to_date_str(end_dt)
    pre_factor_ref_date = to_date_str(pre_factor_ref_date)
    return JQDataClient.instance().attribute_history_engine(**locals())


@assert_auth
def get_daily_info_engine(security, date=None):
    """
    查询复权因子

    :param security 代码，string or list
    :param date 日期，默认空，取当日数据
    :return 一个股票代码返回str，多个股票代码返回dict，
            str: 日期，状态，复权因子
    """
    security = convert_security(security)
    date = to_date_str(date)
    return JQDataClient.instance().get_daily_info_engine(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_factor_effect(security, start_date, end_date, period, factor, group_num=5):
    """获取因子分层回测效果
    以因子值升序分组股票, 以period为周期，获取每组股票收益情况
    :param security 一支指数代码
    :param start_date 开始日期
    :param end_date 结束日期
    :param period 周期，xD, xW, xM > 几日, 几周, 几月
    :param factor 因子名称
    :param group_num 分组数；default 5
    :return dataframe
    """
    security = convert_security(security)
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    assert group_num > 0, "group_num must be a positive numbe"
    assert isinstance(security, six.string_types), "security must be a inde code"
    assert period[-1] in ["D", "W", "M"], "period must be end with one of (\"D\", \"W\", \"M\")"
    return JQDataClient.instance().get_factor_effect(**locals())


@assert_auth
@hashable_lru(maxsize=3)
def get_all_factors():
    return JQDataClient.instance().get_all_factors(**locals())


@assert_auth
def get_call_auction(security, start_date, end_date, fields=None):
    """ 获取指定时间区间内集合竞价时的tick数据
    Args:
        security: 标的代码或者标的代码组成的列表
        start_date: 开始日期，一个时间字符串, 比如"2019-01-01"
        end_date: 结束日期，一个时间字符, 比如"2019-02-01"
        fields:选择要获取的行情字段(类似tick数据的每一个字段)，字段介绍如下:
            字段名         说明              字段类型
            time	      时间	            datetime
            current	      当前价	            float
            volume	      累计成交量（股）  	float
            money	      累计成交额	        float
            b1_v~b5_v	  五档买量          	float
            b1_p~b5_v	  五档买价	        float
            a1_v~a5_v	  五档卖量	        float
            a1_p~a5_p	  五档卖价	        float

        比如:
            get_call_auction(['000001.XSHE', '000002.XSHE'], satrt_date='2019-01-01', end_date='2019-10-10',
                              fields=['time', 'current', 'a1_v', 'b1_v'])

    Return:
        返回一个dataframe，索引为pandas默认的整数索引

    Notice:
        1. field为None的时候，默认获取全部字段
            get_call_auction('000001.XSHE','2019-08-10','2019-08-12')
        2. start_date和end_date不能为None，否则将抛出异常
    """
    if str(end_date) >= str(datetime.datetime.today()):
        if datetime.datetime.now().time() < datetime.time(9, 30):
            # 当天9:30之前数据可能变化, 不用缓存
            return JQDataClient.instance().get_call_auction(**locals())
    return exec_call_auction(security, start_date=start_date, end_date=end_date, fields=fields)


@hashable_lru(maxsize=3)
def exec_call_auction(security,start_date=None, end_date=None, fields=None):
    return JQDataClient.instance().get_call_auction(security=security,
                                                    start_date=start_date,
                                                    end_date=end_date,
                                                    fields=fields)


@assert_auth
def get_factor_kanban_values(universe=None, bt_cycle=None, category=None, model='long_only', **kwargs):
    """获取因子面板数据
    Args:
        universe: 股票池
            'hs300': 沪深300
            'zz500': 中证500
            'zz800': 中证800
            'zz1000': 中证1000
            'zzqz': 中证全指
        bt_cycle: 测试周期
            'month_3':近三个月
            'year_1': 近一年
            'year_3': 近三年
            'year_10': 近十年
        category: 分类
            'basics': 基础类
            'quality': 质量类
            'pershare': 每股类
            'emotion': 情绪类
            'growth': 成长类
            'risk': 风险类
            'barra': 风险因子 - 风格因子
            'technical': 技术类
            'momentum': 动量类
            'style_pro': 新风格因子
        model: 组合构建模型
            'long_only': 纯多头组合
            'long_short': 多空组合
        **kwargs: 其他约束条件详见
            https://www.joinquant.com/help/api/help?name=api#get_factor_kanban_values

    """
    assert  model in ('long_only', 'long_short'),\
            "model 的值应为 'long_only', 'long_short' 中的一个"
    return JQDataClient.instance().get_factor_kanban_values(
            universe=universe,
            bt_cycle=bt_cycle,
            category=category,
            model=model,
            **kwargs
        )


@assert_auth
def get_factor_style_returns(factors=None, start_date=None,
                             end_date=None, count=None,
                             universe=None, industry='sw_l1'):
    """获取风格因子暴露收益率

    参数：
        factors : 因子名称，单个因子（字符串）或一个因子列表,支持风格因子如 "size" 及申万/聚宽一级行业如 "801010" 和 "HY001", 以及国家因子 "country", 注意为了避免混淆, 风格因子仅支持传递 style 和 style_pro 中的一类
        start_date : 开始日期，字符串或 datetime 对象
        end_date : 结束日期，字符串或 datetime 对象，可以与 start_date 或 count 配合使用
        count: 截止 end_date 之前交易日的数量（含 end_date 当日）
        universe : 市场范围, 默认为 None 代表全市场, 可选 : 'hs300':沪深300; 'zz500':中证500'; zz800':中证800; 'zz1000':中证1000; 'zzqz':中证全指; 'zz2000':中证2000
        industry : 行业选取, 默认为 'sw_l1',可选 : 'sw_l1':申万一级, 'jq_l1':聚宽一级; 为了避免混淆, factors 中的行业因子仅返回 industy 下的行业

    返回：
        一个 DataFrame, index 是日期, columns为因子名, 值为因子暴露收益率
    """
    if count and start_date:
        raise ParamsError("(start_date, count) only one param is required")
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return JQDataClient.instance().get_factor_style_returns(**locals())


@assert_auth
def get_factor_specific_returns(security, start_date=None, end_date=None, count=None,
                                category="style"):
    """获取风格因子的特异收益率

    参数:
        security : 股票代码, 或者股票代码组成的list
        start_date : 开始日期，字符串或 datetime 对象
        end_date : 结束日期，字符串或 datetime 对象，可以与 start_date 或 count 配合使用
        count : 截止 end_date 之前交易日的数量（含 end_date 当日）
        category : 风格因子分类, 可选 'style' 和 'style_pro', 默认 'style'
    返回:
        个股在风格因子上的特异收益率
    """
    if count and start_date:
        raise ParamsError("(start_date, count) only one param is required")
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return JQDataClient.instance().get_factor_specific_returns(**locals())


@assert_auth
def get_factor_stats(factor_names=None, universe_type='hs300',
                     start_date=None, end_date=None, count=None,
                     skip_paused=False, commision_fee=0.0):
    """ 获取历史收益(多头)
    参数：
        factor_names : 因子名称，单个因子（字符串）或一个因子列表
        universe_type : 股票池包括以下五种：
                                        'hs300': 沪深300
                                        'zz500': 中证500
                                        'zz800': 中证800
                                        'zz1000': 中证1000
                                        'zzqz': 中证全指
                        默认为'hs300'
        start_date : 开始日期，字符串或 datetime 对象
        end_date : 结束日期，字符串或 datetime 对象，可以与 start_date 或 count 配合使用
        count: 截止 end_date 之前交易日的数量（含 end_date 当日）
        skip_paused : 是否跳过停牌，bool，默认为False
        commision_fee : 手续费，float，0.0/0.0008/0.0018, 默认为0.0

    返回：
        一个 dict，其中 key 是因子名称，value 是一个 pandas.DataFrame
        DataFrame 的 index 是日期，column 1,2,3,4,5是一分位、二分位、三分位、四分位、五分位累积收益
    """
    if count and start_date:
        raise ParamsError("(start_date, count) only one param is required")
    assert universe_type in ('zz500', 'zz1000', 'hs300', 'zz800', 'zzqz'),\
            "股票池应为 'zz500', 'zz1000', 'hs300', 'zz800', 'zzqz'中一个"
    assert commision_fee in (0.0, 0.0008, 0.0018), "手续费应为 0.0, 0.0008, 0.0018 中一个"
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return JQDataClient.instance().get_factor_stats(**locals())


def get_factor_cov(start_date, end_date,
                   factors=None, columns=None,
                   industry='sw_l1', universe=None):
    """获取因子协方差矩阵
    参数:
        start_date : 数据开始时间
        end_date : 数据结束时间
        factors : 风格因子名, 默认所有风格因子, 可以自己加上行业名称, 当行业名称和 industry 不匹配时不返回对应的行业, 也可以传递国家因子名 "contry"
        columns : 列名, 默认返回包含 industry 下的所有行业(默认不含国家因子 "contry", 可指定返回)
        industry : 行业, 目前只支持 sw_l1/jq_l1
        universe : 市场, 目前只支持全市场 None

    返回:
        列名 : date,factor,column(1),column(2),...,column(n)
        eg : date,factor_name,size,beta,..... HY001
            '2023-11-16',size,0.001,0.2,.....
            '2023-11-16',beta,0.23,0.0012,....
    """
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    return JQDataClient.instance().get_factor_cov(**locals())


@assert_auth
def get_all_alpha_101(date, code=None, alpha=None):
    """获取全部 alpha101 因子

    :param date 日期
    :param code 标的 code 字符串列表或者单个标的字符串, 默认为全部
    :param alpha 因子名称, 默认为全部

    返回 DataFrame, index 是标的列表, columns 是因子名
    """
    date = to_date_str(date)

    if code is not None:
        code = convert_security(code)

    if alpha is not None:
        if isinstance(alpha, str):
            alpha = [alpha]
        assert isinstance(alpha, list), "不合法的 alpha 类型"

    return JQDataClient.instance().get_all_alpha_101(**locals())


@assert_auth
def get_all_alpha_191(date, code=None, alpha=None):
    """获取全部 alpha191 因子

    :param date 日期
    :param code 标的 code 字符串列表或者单个标的字符串, 默认为全部
    :param alpha 因子名称, 默认为全部

    返回 DataFrame, index 是标的列表, columns 是因子名
    """
    date = to_date_str(date)

    if code is not None:
        code = convert_security(code)

    if alpha is not None:
        if isinstance(alpha, str):
            alpha = [alpha]
        assert isinstance(alpha, list), "不合法的 alpha 类型"

    return JQDataClient.instance().get_all_alpha_191(**locals())


@assert_auth
def get_data(api_name, **kwargs):
    """通用数据获取接口

    获取非 run_query, alpha 因子, technical_analysis 查询的数据
    :param apis_name 接口名称
    :param kwargs 传入参数，且必须是关键字参数
    """
    assert api_name
    return JQDataClient.instance().get_data(api_name=api_name, args=kwargs)


def get_account_info():
    """获取账号明细"""
    return JQDataClient.instance().get_account_info()


def get_privilege():
    """获取当前拥有的权限"""
    return JQDataClient.instance().get_privilege()


def get_now_time():
    """获取服务器当前时间戳"""
    return JQDataClient.instance().get_now_time()


def get_server_version():
    """获取服务器版本"""
    try:
        version = JQDataClient.instance().get_server_version()
    except Exception:
        version = "1.0"
    return version


def get_test():
    """测试连通性"""
    return JQDataClient.instance().get_test()


def test_network_speed(size=10000000, count=5):
    """测试网络下行速度

    参数：
        size: 每次下载的数据大小，默认为 10M
        count: 测试次数

    返回结果单位为 M/s
    """
    return JQDataClient.instance().test_network_speed(size=size, count=count)


def read_file(path):
    """读取文件"""
    with open(path, 'rb') as f:
        return f.read()


def write_file(path, content, append=False):
    """写入文件"""
    if isinstance(content, six.text_type):
        content = content.encode('utf-8')
    with open(path, 'ab' if append else 'wb') as f:
        return f.write(content)


__all__ = [
    "normalize_code",
    "attribute_history_engine",
    "history_engine",
    "test_network_speed"
] + [name for name in globals().keys() if name.startswith("get")]
