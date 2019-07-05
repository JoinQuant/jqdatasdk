# coding=utf-8
from .utils import assert_auth, to_date_str
from .client import JQDataClient
import sys


@assert_auth
def alpha_001(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
    (rank(Ts_ArgMax(SignedPower(((returns < 0) ? stddev(returns, 20) : close), 2.), 5)) - 0.5)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_002(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*correlation(rank(delta(log(volume), 2)), rank(((close - open) / open)), 6))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_003(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*correlation(rank(open), rank(volume), 10)) 
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_004(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*Ts_Rank(rank(low), 9))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_005(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (rank((open - (sum(vwap, 10) / 10)))\*(-1\*abs(rank((close - vwap)))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_006(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*correlation(open, volume, 10))
     """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_007(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values：符合条件的为公式里的数值，不符合条件的为-1
    公式:
        ((adv20 < volume) ? ((-1\*ts_rank(abs(delta(close, 7)), 60))\*sign(delta(close, 7))) : (-1\*1))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_008(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*rank(((sum(open, 5)\*sum(returns, 5)) - delay((sum(open, 5)\*sum(returns, 5)), 10))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_009(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((0 < ts_min(delta(close, 1), 5)) ? delta(close, 1) : ((ts_max(delta(close, 1), 5) < 0) ? delta(close, 1) : (-1\*delta(close, 1))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_010(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        rank(((0 < ts_min(delta(close, 1), 4)) ? delta(close, 1) : ((ts_max(delta(close, 1), 4) < 0) ? delta(close, 1) : (-1\*delta(close, 1)))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_011(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((rank(ts_max((vwap - close), 3)) + rank(ts_min((vwap - close), 3)))\*rank(delta(volume, 3)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_012(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (sign(delta(volume, 1))\*(-1 * delta(close, 1)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_013(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*rank(covariance(rank(close), rank(volume), 5)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_014(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((-1\*rank(delta(returns, 3)))\*correlation(open, volume, 10))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_015(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*sum(rank(correlation(rank(high), rank(volume), 3)), 3))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_016(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*rank(covariance(rank(high), rank(volume), 5)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_017(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为对应的因子值，取值有问题的股票对应值为-0.0
    公式:
        (((-1\*rank(ts_rank(close, 10)))\*rank(delta(delta(close, 1), 1)))\*rank(ts_rank((volume / adv20), 5)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_018(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\*rank(((stddev(abs((close - open)), 5) + (close - open)) + correlation(close, open, 10))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_019(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((-1\*sign(((close - delay(close, 7)) + delta(close, 7))))\*(1 + rank((1 + sum(returns, 250)))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_020(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (((-1\*rank((open - delay(high, 1))))\* rank((open - delay(close, 1))))\* rank((open - delay(low, 1))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_021(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，取决于满不满足某些因子中的条件
    公式:
        ((((sum(close, 8) / 8) + stddev(close, 8)) < (sum(close, 2) / 2)) ? (-1\* 1) : (((sum(close, 2) / 2) < ((sum(close, 8) / 8) - stddev(close, 8))) ? 1 : (((1 < (volume / adv20)) or ((volume / adv20) == 1)) ? 1 : (-1\* 1))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_022(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\* (delta(correlation(high, volume, 5), 5)\* rank(stddev(close, 20))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_023(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为对应因子值或0.00，当不满足条件时为0.00
    公式:
        (((sum(high, 20) / 20) < high) ? (-1\* delta(high, 2)) : 0)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_024(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((((delta((sum(close, 100) / 100), 100) / delay(close, 100)) < 0.05) or ((delta((sum(close, 100) / 100), 100) / delay(close, 100)) == 0.05)) ? (-1\* (close - ts_min(close, 100))) : (-1\* delta(close, 3)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_025(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        rank(((((-1\* returns)\* adv20)\* vwap)\* (high - close)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_026(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\* ts_max(correlation(ts_rank(volume, 5), ts_rank(high, 5), 5), 3))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_027(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，满足条件为-1，不满足为1
    公式:
        ((0.5 < rank((sum(correlation(rank(volume), rank(vwap), 6), 2) / 2.0))) ? (-1\* 1) : 1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_028(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        scale(((correlation(adv20, low, 5) + ((high + low) / 2)) - close))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_029(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (min(product(rank(rank(scale(log(sum(ts_min(rank(rank((-1\*rank(delta((close - 1), 5))))), 2), 1))))), 1), 5) + ts_rank(delay((-1\* returns), 6), 5))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_030(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (((1.0 - rank(((sign((close - delay(close, 1))) + sign((delay(close, 1) - delay(close, 2)))) + sign((delay(close, 2) - delay(close, 3))))))\* sum(volume, 5)) / sum(volume, 20))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_031(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((rank(rank(rank(decay_linear((-1\* rank(rank(delta(close, 10)))), 10)))) + rank((-1\* delta(close, 3)))) + sign(scale(correlation(adv20, low, 12))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_032(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (scale(((sum(close, 7) / 7) - close)) + (20\* scale(correlation(vwap, delay(close, 5), 230))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_033(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        rank((-1\* ((1 - (open / close))^1)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_034(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        rank(((1 - rank((stddev(returns, 2) / stddev(returns, 5)))) + (1 - rank(delta(close, 1)))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_035(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((Ts_Rank(volume, 32)\* (1 - Ts_Rank(((close + high) - low), 16)))\* (1 - Ts_Rank(returns, 32)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_036(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (((((2.21\* rank(correlation((close - open), delay(volume, 1), 15))) + (0.7\* rank((open - close)))) + (0.73\* rank(Ts_Rank(delay((-1\* returns), 6), 5)))) + rank(abs(correlation(vwap, adv20, 6)))) + (0.6\* rank((((sum(close, 200) / 200) - open)\* (close - open)))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_037(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (rank(correlation(delay((open - close), 1), close, 200)) + rank((open - close)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_038(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((-1\* rank(Ts_Rank(close, 10)))\* rank((close / open)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_039(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((-1\* rank((delta(close, 7)\* (1 - rank(decay_linear((volume / adv20), 9))))))\* (1 + rank(sum(returns, 250))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_040(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((-1\* rank(stddev(high, 10)))\* correlation(high, volume, 10))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_041(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (((high\* low)^0.5) - vwap)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_042(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (rank((vwap - close)) / rank((vwap + close)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_043(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (ts_rank((volume / adv20), 20)\* ts_rank((-1\* delta(close, 7)), 8))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_044(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\* correlation(high, rank(volume), 5))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_045(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\* ((rank((sum(delay(close, 5), 20) / 20))\* correlation(close, volume, 2))\* rank(correlation(sum(close, 5), sum(close, 20), 2))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_046(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1或对应因子值，取决于满不满足某些因子中的条件
    公式:
        ((0.25 < (((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10))) ? (-1\* 1) : (((((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)) < 0) ? 1 : ((-1\* 1)\* (close - delay(close, 1)))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_047(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((((rank((1 / close))\* volume) / adv20)\* ((high\* rank((high - close))) / (sum(high, 5) / 5))) - rank((vwap - delay(vwap, 5))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_048(enddate, index='all'):
    """
    未实现
    公式:
        (indneutralize(((correlation(delta(close, 1), delta(delay(close, 1), 1), 250)\* delta(close, 1)) / close), IndClass.subindustry) / sum(((delta(close, 1) / delay(close, 1))^2), 250))
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_049(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为对应因子值或1，当满足条件时为1
    公式:
        (((((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)) < (-1\* 0.1)) ? 1 : ((-1\* 1)\* (close - delay(close, 1))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_050(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\* ts_max(rank(correlation(rank(volume), rank(vwap), 5)), 5))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_051(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为对应因子值或1，当满足条件时为1
    公式:
        (((((delay(close, 20) - delay(close, 10)) / 10) - ((delay(close, 10) - close) / 10)) < (-1\* 0.05)) ? 1 : ((-1\* 1)\* (close - delay(close, 1))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_052(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((((-1\* ts_min(low, 5)) + delay(ts_min(low, 5), 5))\* rank(((sum(returns, 240) - sum(returns, 20)) / 220)))\* ts_rank(volume, 5))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_053(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\* delta((((close - low) - (high - close)) / (close - low)), 9))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_054(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((-1\* ((low - close)\* (open^5))) / ((low - high)\* (close^5)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_055(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (-1\* correlation(rank(((close - ts_min(low, 12)) / (ts_max(high, 12) - ts_min(low, 12)))), rank(volume), 6))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_056(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (0 - (1\* (rank((sum(returns, 10) / sum(sum(returns, 2), 3)))\* rank((returns\* cap)))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_057(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (0 - (1\* ((close - vwap) / decay_linear(rank(ts_argmax(close, 30)), 2))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_058(enddate, index='all'):
    """
    未实现
    公式:
        (-1\* Ts_Rank(decay_linear(correlation(IndNeutralize(vwap, IndClass.sector), volume, 3.92795), 7.89291), 5.50322))
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_059(enddate, index='all'):
    """
    未实现
    公式:
        (-1\* Ts_Rank(decay_linear(correlation(IndNeutralize(((vwap\* 0.728317) + (vwap\* (1 - 0.728317))), IndClass.industry), volume, 4.25197), 16.2289), 8.19648))
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_060(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (0 - (1\* ((2\* scale(rank(((((close - low) - (high - close)) / (high - low))\* volume)))) - scale(rank(ts_argmax(close, 10))))))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_061(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为1，否则为-1
    公式:
        (rank((vwap - ts_min(vwap, 16.1219))) < rank(correlation(vwap, adv180, 17.9282)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_062(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为-1，否则为1
    公式:
        ((rank(correlation(vwap, sum(adv20, 22.4101), 9.91009)) < rank(((rank(open) + rank(open)) < (rank(((high + low) / 2)) + rank(high)))))\*-1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_063(enddate, index='all'):
    """
    未实现
    公式:
        ((rank(decay_linear(delta(IndNeutralize(close, IndClass.industry), 2.25164), 8.22237)) - rank(decay_linear(correlation(((vwap\* 0.318108) + (open\* (1 - 0.318108))), sum(adv180, 37.2467), 13.557), 12.2883)))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_064(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为-1，否则为1
    公式:
        ((rank(correlation(sum(((open\* 0.178404) + (low\* (1 - 0.178404))), 12.7054), sum(adv120, 12.7054), 16.6208)) < rank(delta(((((high + low) / 2)\* 0.178404) + (vwap\* (1 - 0.178404))), 3.69741)))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_065(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为-1，否则为1
    公式:
         ((rank(correlation(((open\* 0.00817205) + (vwap\* (1 - 0.00817205))), sum(adv60, 8.6911), 6.40374)) < rank((open - ts_min(open, 13.635))))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_066(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((rank(decay_linear(delta(vwap, 3.51013), 7.23052)) + Ts_Rank(decay_linear(((((low\* 0.96633) + (low\* (1 - 0.96633))) - vwap) / (open - ((high + low) / 2))), 11.4157), 6.72611))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_067(enddate, index='all'):
    """
    未实现
    公式:
        ((rank((high - ts_min(high, 2.14593)))^rank(correlation(IndNeutralize(vwap, IndClass.sector), IndNeutralize(adv20, IndClass.subindustry), 6.02936)))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_068(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为-1，否则为1
    公式:
        ((Ts_Rank(correlation(rank(high), rank(adv15), 8.91644), 13.9333) < rank(delta(((close\* 0.518371) + (low\* (1 - 0.518371))), 1.06157)))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_069(enddate, index='all'):
    """
    未实现
    公式:
        ((rank(ts_max(delta(IndNeutralize(vwap, IndClass.industry), 2.72412), 4.79344))^Ts_Rank(correlation(((close\* 0.490655) + (vwap\* (1 - 0.490655))), adv20, 4.92416), 9.0615))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_070(enddate, index='all'):
    """
    未实现
    公式:
        ((rank(delta(vwap, 1.29456))^Ts_Rank(correlation(IndNeutralize(close, IndClass.industry), adv50, 17.8256), 17.9171))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_071(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        max(Ts_Rank(decay_linear(correlation(Ts_Rank(close, 3.43976), Ts_Rank(adv180, 12.0647), 18.0175), 4.20501), 15.6948), Ts_Rank(decay_linear((rank(((low + open) - (vwap + vwap)))^2), 16.4662), 4.4388))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_072(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (rank(decay_linear(correlation(((high + low) / 2), adv40, 8.93345), 10.1519)) / rank(decay_linear(correlation(Ts_Rank(vwap, 3.72469), Ts_Rank(volume, 18.5188), 6.86671), 2.95011)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_073(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (max(rank(decay_linear(delta(vwap, 4.72775), 2.91864)), Ts_Rank(decay_linear(((delta(((open\* 0.147155) + (low\* (1 - 0.147155))), 2.03608) / ((open\* 0.147155) + (low\* (1 - 0.147155))))\* -1), 3.33829), 16.7411))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_074(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为-1，否则为1
    公式:
        ((rank(correlation(close, sum(adv30, 37.4843), 15.1365)) < rank(correlation(rank(((high\* 0.0261661) + (vwap\* (1 - 0.0261661)))), rank(volume), 11.4791)))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_075(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为1，否则为-1 
    公式:
        (rank(correlation(vwap, volume, 4.24304)) < rank(correlation(rank(low), rank(adv50), 12.4413)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_076(enddate, index='all'):
    """
    未实现
    公式:
        (max(rank(decay_linear(delta(vwap, 1.24383), 11.8259)), Ts_Rank(decay_linear(Ts_Rank(correlation(IndNeutralize(low, IndClass.sector), adv81, 8.14941), 19.569), 17.1543), 19.383))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_077(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        min(rank(decay_linear(((((high + low) / 2) + high) - (vwap + high)), 20.0451)), rank(decay_linear(correlation(((high + low) / 2), adv40, 3.1614), 5.64125)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_078(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (rank(correlation(sum(((low\* 0.352233) + (vwap\* (1 - 0.352233))), 19.7428), sum(adv40, 19.7428), 6.83313))^rank(correlation(rank(vwap), rank(volume), 5.77492)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_079(enddate, index='all'):
    """
    未实现
    公式:
        (rank(delta(IndNeutralize(((close\* 0.60733) + (open\* (1 - 0.60733))), IndClass.sector), 1.23438)) < rank(correlation(Ts_Rank(vwap, 3.60973), Ts_Rank(adv150, 9.18637), 14.6644)))
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_080(enddate, index='all'):
    """
    未实现
    公式:
        ((rank(Sign(delta(IndNeutralize(((open\* 0.868128) + (high\* (1 - 0.868128))), IndClass.industry), 4.04545)))^Ts_Rank(correlation(high, adv10, 5.11456), 5.53756))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_081(enddate, index='all'):
    """
    未实现
    公式:
        ((rank(Log(product(rank((rank(correlation(vwap, sum(adv10, 49.6054), 8.47743))^4)), 14.9655))) < rank(correlation(rank(vwap), rank(volume), 5.07914)))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_082(enddate, index='all'):
    """
    未实现
    公式:
        (min(rank(decay_linear(delta(open, 1.46063), 14.8717)), Ts_Rank(decay_linear(correlation(IndNeutralize(volume, IndClass.sector), ((open\* 0.634196) + (open\* (1 - 0.634196))), 17.4842), 6.92131), 13.4283))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_083(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((rank(delay(((high - low) / (sum(close, 5) / 5)), 2))\* rank(rank(volume))) / (((high - low) / (sum(close, 5) / 5)) / (vwap - close)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_084(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        SignedPower(Ts_Rank((vwap - ts_max(vwap, 15.3217)), 20.7127), delta(close, 4.96796))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_085(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (rank(correlation(((high\* 0.876703) + (close\* (1 - 0.876703))), adv30, 9.61331))^rank(correlation(Ts_Rank(((high + low) / 2), 3.70596), Ts_Rank(volume, 10.1595), 7.11408)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_086(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为-1，否则为1
    公式:
        ((Ts_Rank(correlation(close, sum(adv20, 14.7444), 6.00049), 20.4195) < rank(((open + close) - (vwap + open))))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_087(enddate, index='all'):
    """
    未实现
    公式:
        (max(rank(decay_linear(delta(((close\* 0.369701) + (vwap\* (1 - 0.369701))), 1.91233), 2.65461)), Ts_Rank(decay_linear(abs(correlation(IndNeutralize(adv81, IndClass.industry), close, 13.4132)), 4.89768), 14.4535))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_088(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        min(rank(decay_linear(((rank(open) + rank(low)) - (rank(high) + rank(close))), 8.06882)), Ts_Rank(decay_linear(correlation(Ts_Rank(close, 8.44728), Ts_Rank(adv60, 20.6966), 8.01266), 6.65053), 2.61957))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_089(enddate, index='all'):
    """
    未实现
    公式:
        (Ts_Rank(decay_linear(correlation(((low\* 0.967285) + (low\* (1 - 0.967285))), adv10, 6.94279), 5.51607), 3.79744) - Ts_Rank(decay_linear(delta(IndNeutralize(vwap, IndClass.industry), 3.48158), 10.1466), 15.3012))
    """
    raise Exception("该因子未实现")



@assert_auth
def alpha_090(enddate, index='all'):
    """
    未实现
    公式:
        ((rank((close - ts_max(close, 4.66719)))^Ts_Rank(correlation(IndNeutralize(adv40, IndClass.subindustry), low, 5.38375), 3.21856))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_091(enddate, index='all'):
    """
    未实现
    公式:
        ((Ts_Rank(decay_linear(decay_linear(correlation(IndNeutralize(close, IndClass.industry), volume, 9.74928), 16.398), 3.83219), 4.8667) - rank(decay_linear(correlation(vwap, adv30, 4.01303), 2.6809)))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_092(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        min(Ts_Rank(decay_linear(((((high + low) / 2) + close) < (low + open)), 14.7221), 18.8683), Ts_Rank(decay_linear(correlation(rank(low), rank(adv30), 7.58555), 6.94024), 6.80584))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_093(enddate, index='all'):
    """
    未实现
    公式:
        (Ts_Rank(decay_linear(correlation(IndNeutralize(vwap, IndClass.industry), adv81, 17.4193), 19.848), 7.54455) / rank(decay_linear(delta(((close\* 0.524434) + (vwap\* (1 - 0.524434))), 2.77377), 16.2664)))
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_094(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((rank((vwap - ts_min(vwap, 11.5783)))^Ts_Rank(correlation(Ts_Rank(vwap, 19.6462), Ts_Rank(adv60, 4.02992), 18.0926), 2.70756))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_095(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        eries：index为成分股代码，values为1或-1，当满足条件时为1，否则为-1
    公式:
        (rank((open - ts_min(open, 12.4105))) < Ts_Rank((rank(correlation(sum(((high + low) / 2), 19.1351), sum(adv40, 19.1351), 12.8742))^5), 11.7584))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_096(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (max(Ts_Rank(decay_linear(correlation(rank(vwap), rank(volume), 3.83878), 4.16783), 8.38151), Ts_Rank(decay_linear(Ts_ArgMax(correlation(Ts_Rank(close, 7.45404), Ts_Rank(adv60, 4.13242), 3.65459), 12.6556), 14.0365), 13.4143))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_097(enddate, index='all'):
    """
    未实现
    公式: 
        ((rank(decay_linear(delta(IndNeutralize(((low\* 0.721001) + (vwap\* (1 - 0.721001))), IndClass.industry), 3.3705), 20.4523)) - Ts_Rank(decay_linear(Ts_Rank(correlation(Ts_Rank(low, 7.87871), Ts_Rank(adv60, 17.255), 4.97547), 18.5925), 15.7152), 6.71659))\* -1)
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_098(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        (rank(decay_linear(correlation(vwap, sum(adv5, 26.4719), 4.58418), 7.18088)) - rank(decay_linear(Ts_Rank(Ts_ArgMin(correlation(rank(open), rank(adv15), 20.8187), 8.62571), 6.95668), 8.07206)))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())

@assert_auth
def alpha_099(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series: index为成分股代码，values为1或-1，当满足条件时为-1，否则为1
    公式:
        ((rank(correlation(sum(((high + low) / 2), 19.8975), sum(adv60, 19.8975), 8.8136)) < rank(correlation(low, volume, 6.28259)))\* -1)
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


@assert_auth
def alpha_100(enddate, index='all'):
    """
    未实现
    公式:
        (0 - (1\* (((1.5\* scale(indneutralize(indneutralize(rank(((((close - low) - (high - close)) / (high - low))\* volume)), IndClass.subindustry), IndClass.subindustry))) - scale(indneutralize((correlation(close, rank(adv20), 5) - rank(ts_argmin(close, 30))), IndClass.subindustry)))\* (volume / adv20))))
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_101(enddate, index='all'):
    """
    Inputs:
        enddate: 必选参数，计算哪一天的因子  
        index: 默认参数，股票指数，默认为所有股票'all' 
    Outputs:
        Series：index 为成分股代码，values为对应的因子值
    公式:
        ((close - open) / ((high - low) + .001))
    """
    enddate = to_date_str(enddate)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_101(**locals())


__all__ = [k for k, v in sorted(globals().items()) if k.startswith("alpha_")]


