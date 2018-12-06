# coding=utf-8
from functools import wraps
from .utils import *
from .client import JQDataClient


@assert_auth
def get_price(security, start_date=None, end_date=None, frequency='daily',
              fields=None, skip_paused=False, fq='pre', count=None):
    """
    获取一支或者多只证券的行情数据

    :param security 一支证券代码或者一个证券代码的list
    :param count 与 start_date 二选一，不可同时使用.数量, 返回的结果集的行数, 即表示获取 end_date 之前几个 frequency 的数据
    :param start_date 与 count 二选一，不可同时使用. 字符串或者 datetime.datetime/datetime.date 对象, 开始时间
    :param end_date 格式同上, 结束时间, 默认是'2015-12-31', 包含此日期.
    :param frequency 单位时间长度, 几天或者几分钟, 现在支持'Xd','Xm', 'daily'(等同于'1d'), 'minute'(等同于'1m'), X是一个正整数, 分别表示X天和X分钟
    :param fields 字符串list, 默认是None(表示['open', 'close', 'high', 'low', 'volume', 'money']这几个标准字段), 支持以下属性 ['open', 'close', 'low', 'high', 'volume', 'money', 'factor', 'high_limit', 'low_limit', 'avg', 'pre_close', 'paused']
    :param skip_paused 是否跳过不交易日期(包括停牌, 未上市或者退市后的日期). 如果不跳过, 停牌时会使用停牌前的数据填充, 上市前或者退市后数据都为 nan
    :return 如果是一支证券, 则返回pandas.DataFrame对象, 行索引是datetime.datetime对象, 列索引是行情字段名字; 如果是多支证券, 则返回pandas.Panel对象, 里面是很多pandas.DataFrame对象, 索引是行情字段(open/close/…), 每个pandas.DataFrame的行索引是datetime.datetime对象, 列索引是证券代号.
    """
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
    start_date = to_date_str(start_date)
    end_date = to_date_str(end_date)
    security_list = convert_security(security_list)
    return JQDataClient.instance().get_extras(**locals())


@assert_auth
def get_fundamentals(query_object, date=None, statDate=None):
    """
    查询财务数据, 详细的数据字段描述在 https://www.joinquant.com/data/dict/fundamentals 中查看

    :param query_object 一个sqlalchemy.orm.query.Query对象
    :param date 查询日期, 一个字符串(格式类似’2015-10-15’)或者datetime.date/datetime.datetime对象, 可以是None, 使用默认日期
    :param statDate: 财报统计的季度或者年份, 一个字符串, 有两种格式:1.季度: 格式是: 年 + ‘q’ + 季度序号, 例如: ‘2015q1’, ‘2013q4’. 2.年份: 格式就是年份的数字, 例如: ‘2015’, ‘2016’.
    :return 返回一个 pandas.DataFrame, 每一行对应数据库返回的每一行(可能是几个表的联合查询结果的一行), 列索引是你查询的所有字段;为了防止返回数据量过大, 我们每次最多返回10000行;当相关股票上市前、退市后，财务数据返回各字段为空
    """
    from .finance_service import get_fundamentals_sql
    if date is None and statDate is None:
        date = datetime.date.today()
        from .calendar_service import CalendarService
        trade_days = CalendarService.get_all_trade_days()
        date = list(filter(lambda item: item < date, trade_days))[-1]
    elif date:
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        date = min(to_date(date), yesterday)
    sql = get_fundamentals_sql(query_object, date, statDate)
    return JQDataClient.instance().get_fundamentals(sql=sql)


@assert_auth
def get_fundamentals_continuously(query_object, end_date=None, count=None):
    """
    查询财务数据，详细的数据字段描述在 https://www.joinquant.com/data/dict/fundamentals 中查看
    :param query_object:一个sqlalchemy.orm.query.Query对象
    :param end_date:查询日期, 一个字符串(格式类似’2015-10-15’)或者datetime.date/datetime.datetime对象, 可以是None, 使用默认日期
    :param count:获取 end_date 前 count 个日期的数据
    :return:返回一个 pandas.Panel
    """
    assert count, "count is required"
    from .finance_service import fundamentals_redundant_continuously_query_to_sql
    from .calendar_service import CalendarService

    trade_days = CalendarService.get_trade_days(end_date=end_date, count=count)
    sql = fundamentals_redundant_continuously_query_to_sql(query_object, trade_days)
    sql = remove_duplicated_tables(sql)
    df = JQDataClient.instance().get_fundamentals_continuously(sql=sql)
    df3 = df.copy()
    df3["multi"] = df["day"] + "_" + df["code"]
    df3 = df3.drop_duplicates("multi")
    del df3["multi"]
    df3 = df3.set_index(["day", "code"])
    pan = df3.to_panel()
    return pan


@assert_auth
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
def get_industries(name=None):
    """
    按照行业分类获取行业列表
    :param name:行业代码
    :return:pandas.DataFrame, 各column分别为行业代码、行业名称、开始日期
    """
    assert name, "name is required"
    return JQDataClient.instance().get_industries(**locals())


@assert_auth
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
def get_concepts():
    """
    获取概念板块
    :return:pandas.DataFrame, 各column分别为概念代码、概念名称、开始日期
    """
    return JQDataClient.instance().get_concepts(**locals())


@assert_auth
def get_all_securities(types=[], date=None):
    """
    获取平台支持的所有股票、基金、指数、期货信息

    :param types list: 用来过滤securities的类型, list元素可选: ‘stock’, ‘fund’, ‘index’, ‘futures’, ‘etf’, ‘lof’, ‘fja’, ‘fjb’. types为空时返回所有股票, 不包括基金,指数和期货
    :param date 日期, 一个字符串或者 datetime.datetime/datetime.date 对象, 用于获取某日期还在上市的股票信息. 默认值为 None, 表示获取所有日期的股票信息
    :return pandas.DataFrame
    """
    date = to_date_str(date)
    return JQDataClient.instance().get_all_securities(**locals())


@assert_auth
def get_security_info(code):
    """
    获取股票/基金/指数的信息

    :param code 证券代码
    :return Security
    """
    assert code, "code is required"
    result = JQDataClient.instance().get_security_info(**locals())
    if result:
        return Security(**result)


@assert_auth
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
def get_margincash_stocks(dt=None):
    """
    返回上交所、深交所最近一次披露的的可融资标的列表的list
    :return: list
    """
    return JQDataClient.instance().get_margincash_stocks(**locals())


@assert_auth
def get_marginsec_stocks(dt=None):
    """
    返回上交所、深交所最近一次披露的的可融券标的列表的list
    :return:list
    """
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
def get_dominant_future(underlying_symbol, date=None):
    """
    获取主力合约对应的标的

    :param underlying_symbol 期货合约品种，如 ‘AG’(白银)
    :return 主力合约对应的期货合约
    """
    dt = to_date_str(date)
    return JQDataClient.instance().get_dominant_future(underlying_symbol=underlying_symbol, dt=dt)


@assert_auth
def get_ticks(security, start_dt=None, end_dt=None, count=None, fields=None):
    """
    获取tick数据
    :param security: 股票or期货标的代码,仅限单只
    :param start_dt: 开始日期
    :param end_dt: 截止日期
    :param count: 统计个数
    :param fields: 期货：[time current high low volume money position a1_v a1_p b1_v b1_p]
                    股票：[time current high low volume money a1_v-a5_v a1_p-a5_p b1_v-b5_v b1_p-b5_p]
                    为None时，默认返回对应类型的所有字段
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
def get_industry(security, date=None):
    """
    查询股票所属行业

    :param security 标的代码
    :date 查询的日期，默认为空
    :return 字典格式
    """
    assert security, "security is required"
    security = convert_security(security)
    date = to_date_str(date)
    return JQDataClient.instance().get_industry(**locals())


@assert_auth
def get_bars(security, count, unit="1d", fields=("open", "high", "low", "close"), include_now=False, end_dt=None,
             fq_ref_date=None):
    """
    获取历史数据(包含快照数据), 可查询单个标的多个数据字段

    :param security 股票代码
    :param count 大于0的整数，表示获取bar的个数。如果行情数据的bar不足count个，返回的长度则小于count个数。
    :param unit bar的时间单位, 支持如下周期：'1m', '5m', '15m', '30m', '60m', '120m', '1d', '1w', '1M'。'1w' 表示一周，‘1M' 表示一月。
    :param fields 获取数据的字段， 支持如下值：'date', 'open', 'close', 'high', 'low', 'volume', 'money'
    :param include_now 取值True 或者False。 表示是否包含当前bar, 比如策略时间是9:33，unit参数为5m， 如果 include_now=True,则返回9:30-9:33这个分钟 bar。
    :param end_dt: 查询的截止时间
    :param fq_ref_date: 复权基准日期，为None时为不复权数据
    :return numpy.ndarray格式
    """
    assert security, "security is required"
    security = convert_security(security)
    assert isinstance(security, six.string_types), "security's type must be string"
    end_dt = to_date_str(end_dt)
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


@assert_auth
def get_current_tick(security):
    """
    获取最新的 tick 数据

    :param security 标的代码
    :return:
    """
    assert security, "security is required"
    assert isinstance(security, six.string_types), "security's type must be string"
    security = convert_security(security)
    return JQDataClient.instance().get_current_tick(**locals())


@assert_auth
def get_current_tick_engine(security):
    assert security, "security is required"
    if not (isinstance(security, six.string_types) or isinstance(security, (tuple, list))):
        raise Exception('security 必须是字符串 或者 字符串数组')
    security = convert_security(security)
    return JQDataClient.instance().get_current_tick_engine(**locals())


@assert_auth
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


def read_file(path):
    """
    读取文件
    """
    with open(path, 'rb') as f:
        return f.read()


def write_file(path, content, append=False):
    """
    写入文件
    """
    if isinstance(content, six.text_type):
        content = content.encode('utf-8')
    with open(path, 'ab' if append else 'wb') as f:
        return f.write(content)


__all__ = ["get_price", "get_trade_days", "get_all_trade_days", "get_extras", "get_fundamentals_continuously",
           "get_index_stocks", "get_industry_stocks", "get_concept_stocks", "get_all_securities",
           "get_security_info", "get_money_flow", "get_locked_shares", "get_fundamentals", "get_mtss",
           "get_concepts", "get_industries", "get_margincash_stocks", "get_marginsec_stocks",
           "get_future_contracts", "get_dominant_future", "normalize_code", "get_baidu_factor",
           "get_billboard_list", "get_ticks", "read_file", "write_file", "get_factor_values", "get_index_weights",
           "get_bars", "get_current_tick", "get_fund_info", "get_query_count", "get_price_engine",
           "history_engine", "attribute_history_engine", "get_bars_engine", "get_ticks_engine",
           "get_current_tick_engine", "get_daily_info_engine","get_industry"]
