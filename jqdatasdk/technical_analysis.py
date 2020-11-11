# coding=utf-8
from .utils import assert_auth, to_date_str
from .client import JQDataClient
import sys


@assert_auth
def ATR(security_list, check_date, timeperiod=14, unit='1d', include_now=True):
    '''
        计算公式：
            MTR:MAX(MAX((HIGH-LOW),ABS(REF(CLOSE,1)-HIGH)),ABS(REF(CLOSE,1)-LOW));
            ATR:MA(MTR,N);
            输出MTR:(最高价-最低价)和1日前的收盘价-最高价的绝对值的较大值和1日前的收盘价-最低价的绝对值的较大值
            输出真实波幅ATR:MTR的N日简单移动平均
        输入：
            security_list:股票列表
            check_date：要查询数据的日期
            timeperiod：统计的天数 timeperiod
        输出：
            MTR和ATR 的值。
        输出结果类型：
            字典(dict)：键(key)为股票代码，值(value)为数据。
        '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def BIAS(security_list, check_date, N1=6, N2=12, N3=24, unit='1d', include_now=True):
    '''
    计算公式：
        BIAS1 :(CLOSE-MA(CLOSE,N1))/MA(CLOSE,N1)*100;
        BIAS2 :(CLOSE-MA(CLOSE,N2))/MA(CLOSE,N2)*100;
        BIAS3 :(CLOSE-MA(CLOSE,N3))/MA(CLOSE,N3)*100;
        输出BIAS1 = (收盘价-收盘价的N1日简单移动平均)/收盘价的N1日简单移动平均*100
        输出BIAS2 = (收盘价-收盘价的N2日简单移动平均)/收盘价的N2日简单移动平均*100
        输出BIAS3 = (收盘价-收盘价的N3日简单移动平均)/收盘价的N3日简单移动平均*100
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
        N2: 统计的天数 N2
        N3: 统计的天数 N3
    输出：
        BIAS1, BIAS2, BIAS3 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CCI(security_list, check_date, N=14, unit='1d', include_now=True):
    '''
    计算公式：
        TYP:=(HIGH+LOW+CLOSE)/3;
        CCI:(TYP-MA(TYP,N))/(0.015*AVEDEV(TYP,N));
        TYP赋值:(最高价+最低价+收盘价)/3
        输出CCI = (TYP-TYP的N日简单移动平均)/(0.015*TYP的N日平均绝对偏差)
        其中，绝对平均偏差= 1/n * (SUM(|xi-x均|), i=1,2,3...n)
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        CCI 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def KDJ(security_list, check_date, N=9, M1=3, M2=3, unit='1d', include_now=True):
    '''
    计算公式：
        RSV:=(CLOSE- LLV(LOW,N) )/(HHV(HIGH,N)-LLV(LOW,N))*100;
        K:SMA(RSV,M1,1);
        D:SMA(K,M2,1);
        J:3*K-2*D;
        RSV赋值:(收盘价-N日内最低价的最低值)/(N日内最高价的最高值-N日内最低价的最低值)*100
        输出K = RSV的M1日[1日权重]移动平均
        输出D = K的M2日[1日权重]移动平均
        输出J = 3*K-2*D
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M1：统计的天数 M1
        M2：统计的天数 M2
    输出：
        K，D和J 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def MFI(security_list, check_date, timeperiod=14, unit='1d', include_now=True):
    '''
    计算公式：
        TYP = (最高价 + 最低价 + 收盘价)/3
        V1 = 如果TYP>1日前的TYP,返回TYP*成交量(手),否则返回0的N日累和/如果TYP<1日前的TYP,返回TYP*成交量(手),否则返回0的N日累和
        MFI = 100-(100/(1+V1))
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数 N
    输出：
        MFI 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def MTM(security_list, check_date, timeperiod=12, unit='1d', include_now=True):
    '''
    计算公式：
        动量线:收盘价-N日前的收盘价
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数 N
    输出：
        MTM 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ROC(security_list, check_date, timeperiod=12, unit='1d', include_now=True):
    '''
    计算公式：
        ROC = 100*(收盘价-N日前的收盘价)/N日前的收盘价
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数 N
    输出：
        ROC 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def RSI(security_list, check_date, N1=6, unit='1d', include_now=True):
    '''
    计算公式：
        LC:=REF(CLOSE,1);
        RSI1:SMA(MAX(CLOSE-LC,0),N1,1)/SMA(ABS(CLOSE-LC),N1,1)*100;
        LC赋值:1日前的收盘价
        输出RSI1:收盘价-LC和0的较大值的N1日[1日权重]移动平均/收盘价-LC的绝对值的N1日[1日权重]移动平均*100
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
    输出：
        RSI 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ACCER(security_list, check_date, N=8, unit='1d', include_now=True):
    '''
    计算公式：
        ACCER:SLOPE(CLOSE,N)/CLOSE;
        输出幅度涨速:收盘价的N日线性回归斜率/收盘价
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        ACCER 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ADTM(security_list, check_date, N=23, M=8, unit='1d', include_now=True):
    '''
    计算公式：
        DTM:=IF(OPEN<=REF(OPEN,1),0,MAX((HIGH-OPEN),(OPEN-REF(OPEN,1))));
        DBM:=IF(OPEN>=REF(OPEN,1),0,MAX((OPEN-LOW),(OPEN-REF(OPEN,1))));
        STM:=SUM(DTM,N);
        SBM:=SUM(DBM,N);
        ADTM:IF(STM>SBM,(STM-SBM)/STM,IF(STM=SBM,0,(STM-SBM)/SBM));
        MAADTM:MA(ADTM,M);
        DTM赋值:如果开盘价<=1日前的开盘价,返回0,否则返回(最高价-开盘价)和(开盘价-1日前的开盘价)的较大值
        DBM赋值:如果开盘价>=1日前的开盘价,返回0,否则返回(开盘价-最低价)和(开盘价-1日前的开盘价)的较大值
        STM赋值:DTM的N日累和
        SBM赋值:DBM的N日累和
        输出动态买卖气指标:如果STM>SBM,返回(STM-SBM)/STM,否则返回如果STM=SBM,返回0,否则返回(STM-SBM)/SBM
        输出MAADTM:ADTM的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        ADTM和MAADTM 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def BIAS_QL(security_list, check_date, N=6, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        BIAS :(CLOSE-MA(CLOSE,N))/MA(CLOSE,N)*100;
        BIASMA :MA(BIAS,M);
        输出乖离率BIAS :(收盘价-收盘价的N日简单移动平均)/收盘价的N日简单移动平均*100
        输出BIASMA :乖离率的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        BIAS和BIASMA 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def BIAS_36(security_list, check_date, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        BIAS36:MA(CLOSE,3)-MA(CLOSE,6);
        BIAS612:MA(CLOSE,6)-MA(CLOSE,12);
        MABIAS:MA(BIAS36,M);
        输出三六乖离:收盘价的3日简单移动平均-收盘价的6日简单移动平均
        输出BIAS612:收盘价的6日简单移动平均-收盘价的12日简单移动平均
        输出MABIAS:BIAS36的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        M：统计的天数 M
    输出：
        BIAS36, BIAS612和MABIAS 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def DKX(security_list, check_date, M=10, unit='1d', include_now=True):
    '''
    计算公式：
        MID:=(3*CLOSE+LOW+OPEN+HIGH)/6;
        DKX:(20*MID+19*REF(MID,1)+18*REF(MID,2)+17*REF(MID,3)+
        16*REF(MID,4)+15*REF(MID,5)+14*REF(MID,6)+
        13*REF(MID,7)+12*REF(MID,8)+11*REF(MID,9)+
        10*REF(MID,10)+9*REF(MID,11)+8*REF(MID,12)+
        7*REF(MID,13)+6*REF(MID,14)+5*REF(MID,15)+
        4*REF(MID,16)+3*REF(MID,17)+2*REF(MID,18)+REF(MID,20))/210;
        MADKX:MA(DKX,M);
        MID赋值:(3*收盘价+最低价+开盘价+最高价)/6
        输出多空线:(20*MID+19*1日前的MID+18*2日前的MID+17*3日前的MID+16*4日前的MID+15*5日前的MID+14*6日前的MID+13*7日前的MID+12*8日前的MID+11*9日前的MID+10*10日前的MID+9*11日前的MID+8*12日前的MID+7*13日前的MID+6*14日前的MID+5*15日前的MID+4*16日前的MID+3*17日前的MID+2*18日前的MID+20日前的MID)/210
        输出MADKX:DKX的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        M：统计的天数 M
    输出：
        DKX和MADKX 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def KD(security_list, check_date, N=9, M1=3, M2=3, unit='1d', include_now=True):
    '''
    计算公式：
        RSV:=(CLOSE-LLV(LOW,N))/(HHV(HIGH,N)-LLV(LOW,N))*100;
        K:SMA(RSV,M1,1);
        D:SMA(K,M2,1);
        RSV赋值:(收盘价-N日内最低价的最低值)/(N日内最高价的最高值-N日内最低价的最低值)*100
        输出K:RSV的M1日[1日权重]移动平均
        输出D:K的M2日[1日权重]移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M1：统计的天数 M1
        M2：统计的天数 M2
    输出：
        K和D 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def LWR(security_list, check_date, N=9, M1=3, M2=3, unit='1d', include_now=True):
    '''
    计算公式：
        RSV:= (HHV(HIGH,N)-CLOSE)/(HHV(HIGH,N)-LLV(LOW,N))*100;
        LWR1:SMA(RSV,M1,1);
        LWR2:SMA(LWR1,M2,1);
        RSV赋值: (N日内最高价的最高值-收盘价)/(N日内最高价的最高值-N日内最低价的最低值)*100
        输出LWR1:RSV的M1日[1日权重]移动平均
        输出LWR2:LWR1的M2日[1日权重]移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M1：统计的天数 M1
        M2：统计的天数 M2
    输出：
        LWR1和LWR2 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def MARSI(security_list, check_date, M1=10, M2=6, unit='1d', include_now=True):
    '''
    计算公式：
        DIF:=CLOSE-REF(CLOSE,1);
        VU:=IF(DIF>=0,DIF,0);
        VD:=IF(DIF<0,-DIF,0);
        MAU1:=MEMA(VU,M1);
        MAD1:=MEMA(VD,M1);
        MAU2:=MEMA(VU,M2);
        MAD2:=MEMA(VD,M2);
        # MEMA(X, N)相当于SMA(X, N, 1)
        RSI10:MA(100*MAU1/(MAU1+MAD1),M1);
        RSI6:MA(100*MAU2/(MAU2+MAD2),M2);
        DIF赋值:收盘价-1日前的收盘价
        VU赋值:如果DIF>=0,返回DIF,否则返回0
        VD赋值:如果DIF<0,返回-DIF,否则返回0
        MAU1赋值:VU的M1日平滑移动平均
        MAD1赋值:VD的M1日平滑移动平均
        MAU2赋值:VU的M2日平滑移动平均
        MAD2赋值:VD的M2日平滑移动平均
        输出RSI10:100*MAU1/(MAU1+MAD1)的M1日简单移动平均
        输出RSI6:100*MAU2/(MAU2+MAD2)的M2日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        M1：统计的天数 M1
        M2：统计的天数 M2
    输出：
        RSI10和RSI6 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def OSC(security_list, check_date, N=20, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        OSC:100*(CLOSE-MA(CLOSE,N));
        MAOSC:EXPMEMA(OSC,M);
        输出变动速率线OSC = 100*(收盘价-收盘价的N日简单移动平均)
        输出MAOSC = OSC的M日指数平滑移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        OSC和MAOSC 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def SKDJ(security_list, check_date, N=9, M=3, unit='1d', include_now=True):
    '''
    计算公式：
        LOWV:=LLV(LOW,N);
        HIGHV:=HHV(HIGH,N);
        RSV:=EMA((CLOSE-LOWV)/(HIGHV-LOWV)*100,M);
        K:EMA(RSV,M);
        D:MA(K,M);
        LOWV赋值:N日内最低价的最低值
        HIGHV赋值:N日内最高价的最高值
        RSV赋值:(收盘价-LOWV)/(HIGHV-LOWV)*100的M日指数移动平均
        输出K:RSV的M日指数移动平均
        输出D:K的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        K和D 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def UDL(security_list, check_date, N1=3, N2=5, N3=10, N4=20, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        UDL:(MA(CLOSE,N1)+MA(CLOSE,N2)+MA(CLOSE,N3)+MA(CLOSE,N4))/4;
        MAUDL:MA(UDL,M);
        输出引力线UDL = (收盘价的N1日简单移动平均+收盘价的N2日简单移动平均+收盘价的N3日简单移动平均+收盘价的N4日简单移动平均)/4
        输出MAUDL = UDL的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
        N2：统计的天数 N2
        N3：统计的天数 N3
        N4：统计的天数 N4
        M：统计的天数 M
    输出：
        UDL和MAUDL 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def WR(security_list, check_date, N=10, N1=6, unit='1d', include_now=True):
    '''
    计算公式：
        WR1:100*(HHV(HIGH,N)-CLOSE)/(HHV(HIGH,N)-LLV(LOW,N));
        WR2:100*(HHV(HIGH,N1)-CLOSE)/(HHV(HIGH,N1)-LLV(LOW,N1));
        输出WR1:100*(N日内最高价的最高值-收盘价)/(N日内最高价的最高值-N日内最低价的最低值)
        输出WR2:100*(N1日内最高价的最高值-收盘价)/(N1日内最高价的最高值-N1日内最低价的最低值)
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        WR和MAWR 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CYF(security_list, check_date, N=21, unit='1d', include_now=True):
    '''
    计算公式：
        CYF:100-100/(1+EMA(HSL,N));
        输出市场能量:100-100/(1+换手线的N日指数移动平均)
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        CYF 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def FSL(security_list, check_date):
    '''
    计算公式：
        SWL:(EMA(CLOSE,5)*7+EMA(CLOSE,10)*3)/10;
        SWS:DMA(EMA(CLOSE,12),MAX(1,100*(SUM(VOL,5)/(3*CAPITAL))));
        输出SWL:(收盘价的5日指数移动平均*7+收盘价的10日指数移动平均*3)/10+移动平均
        输出SWS:以1和100*(成交量(手)的5日累和/(3*当前流通股本(手)))的较大值为权重收盘价的12日指数移动平均的动态移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
    输出：
        SWL和SWS 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def TAPI(index_stock, security_list, check_date, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        TAPI:AMOUNT/INDEXC;
        MATAIP:MA(TAPI,M);
        输出加权指数成交值(需下载日线):成交额(元)/大盘的收盘价
        输出MATAIP:TAPI的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        M：统计的天数 M
    输出：
        TAPI和MATAPI 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CHO(security_list, check_date, N1=10, N2=20, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        MID:=SUM(VOL*(2*CLOSE-HIGH-LOW)/(HIGH+LOW),0);
        CHO:MA(MID,N1)-MA(MID,N2);
        MACHO:MA(CHO,M);
        MID赋值 = 成交量(手)*(2*收盘价-最高价-最低价)/(最高价+最低价)的历史累和
        输出佳庆指标 = MID的N1日简单移动平均-MID的N2日简单移动平均
        输出MACHO = CHO的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
        N2：统计的天数 N2
    输出：
        CHO和MACHO的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CYE(security_list, check_date, unit='1d', include_now=True):
    '''
     计算公式：
        MAL:=MA(CLOSE,5);
        MAS:=MA(MA(CLOSE,20),5);
        CYEL:(MAL-REF(MAL,1))/REF(MAL,1)*100;
        CYES:(MAS-REF(MAS,1))/REF(MAS,1)*100;
        MAL赋值:收盘价的5日简单移动平均
        MAS赋值:收盘价的20日简单移动平均的5日简单移动平均
        输出CYEL:(MAL-1日前的MAL)/1日前的MAL*100
        输出CYES:(MAS-1日前的MAS)/1日前的MAS*100
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
    输出：
        CYEL和CYES的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def DBQR(index_stock, security_list, check_date, N=5, M1=10, M2=20, M3=60, unit='1d', include_now=True):
    '''
    计算公式：
        ZS:(INDEXC-REF(INDEXC,N))/REF(INDEXC,N);
        GG:(CLOSE-REF(CLOSE,N))/REF(CLOSE,N);
        MADBQR1:MA(GG,M1);
        MADBQR2:MA(GG,M2);
        MADBQR3:MA(GG,M3);
        输出ZS = (大盘的收盘价-N日前的大盘的收盘价)/N日前的大盘的收盘价  *上证综合指数*
        输出GG = (收盘价-N日前的收盘价)/N日前的收盘价
        输出MADBQR1 = GG的M1日简单移动平均
        输出MADBQR2 = GG的M2日简单移动平均
        输出MADBQR3 = GG的M3日简单移动平均
    输入：
        index_stock:大盘股票代码
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M1：统计的天数 M1
        M2：统计的天数 M2
        M3：统计的天数 M3
    输出：
        ZS, GG, MADBQR1, MADBQR2和MADBQR3的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def DMA(security_list, check_date, N1=10, N2=50, M=10, unit='1d', include_now=True):
    '''
    计算公式：
        DIF:MA(CLOSE,N1)-MA(CLOSE,N2);
        DIFMA:MA(DIF,M);
        输出DIF:收盘价的N1日简单移动平均-收盘价的N2日简单移动平均
        输出DIFMA:DIF的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
        N2: 统计的天数 N2
        M: 统计的天数 M
    输出：
        DIF和DIFMA 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def DMI(security_list, check_date, N=14,  MM=6, unit='1d', include_now=True):
    '''
    计算公式：
        MTR = 最高价-最低价和最高价-1日前的收盘价的绝对值的较大值和1日前的收盘价-最低价的绝对值的较大值的N日指数平滑移动平均
        HD = 最高价-1日前的最高价
        LD = 1日前的最低价-最低价
        DMP = 如果HD>0并且HD>LD,返回HD,否则返回0的N日指数平滑移动平均
        DMM = 如果LD>0并且LD>HD,返回LD,否则返回0的N日指数平滑移动平均
        输出PDI = DMP*100/MTR
        输出MDI = DMM*100/MTR
        输出ADX = MDI-PDI的绝对值/(MDI+PDI)*100的MM日指数平滑移动平均
        输出ADXR = ADX的MM日指数平滑移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        MM：统计的天数 MM
    输出：
        PDI, MDI, ADX, ADXR的值
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def DPO(security_list, check_date, N=20,  M=6, unit='1d', include_now=True):
    '''
    计算公式：
        DPO:CLOSE-REF(MA(CLOSE,N),N/2+1);
        MADPO:MA(DPO,M);
        输出区间震荡线DPO = 收盘价-N/2+1日前的收盘价的N日简单移动平均
        输出MADPO = DPO的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        DPO 和 MADPO 的值
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def EMV(security_list, check_date, N=14, M=9, unit='1d', include_now=True):
    '''
    计算公式：
        VOLUME:=MA(VOL,N)/VOL;
        MID:=100*(HIGH+LOW-REF(HIGH+LOW,1))/(HIGH+LOW);
        EMV:MA(MID*VOLUME*(HIGH-LOW) / MA(HIGH-LOW,N),N);
        MAEMV:MA(EMV,M);
        VOLUME = 成交量(手)的N日简单移动平均/成交量(手)
        MID = 100*(最高价+最低价-1日前的最高价+最低价)/(最高价+最低价)
        输出EMV = MID*VOLUME*(最高价-最低价)/最高价-最低价的N日简单移动平均的N日简单移动平均
        输出MAEMV = EMV的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        EMV和MAEMV的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def GDX(security_list, check_date, N=30, M=9, unit='1d', include_now=True):
    '''
     计算公式：
        AA:=ABS((2*CLOSE+HIGH+LOW)/4-MA(CLOSE,N))/MA(CLOSE,N);
        JAX:DMA(CLOSE,AA);
        压力线:(1+M/100)*JAX;
        支撑线:(1-M/100)*JAX;
        AA赋值:(2*收盘价+最高价+最低价)/4-收盘价的N日简单移动平均的绝对值/收盘价的N日简单移动平均
        输出济安线 = 以AA为权重收盘价的动态移动平均
        输出压力线 = (1+M/100)*JAX
        输出支撑线 = (1-M/100)*JAX
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        济安线、压力线和支撑线的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def JLHB(security_list, check_date, N=7, M=5, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=(CLOSE-LLV(LOW,60))/(HHV(HIGH,60)-LLV(LOW,60))*80;
        B:SMA(VAR1,N,1);
        VAR2:SMA(B,M,1);
        绝路航标:IF(CROSS(B,VAR2) AND B<40,50,0);

        VAR1赋值:(收盘价-60日内最低价的最低值)/(60日内最高价的最高值-60日内最低价的最低值)*80
        输出 B:VAR1的N日[1日权重]移动平均
        输出 VAR2:B的M日[1日权重]移动平均
        输出 绝路航标:如果B上穿VAR2 AND B<40,返回50,否则返回0
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        B, VAR2和绝路航标 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def JS(security_list, check_date, N=5, M1=5, M2=10, M3=20, unit='1d', include_now=True):
    '''
    计算公式：
        JS:100*(CLOSE-REF(CLOSE,N))/(N*REF(CLOSE,N));
        MAJS1:MA(JS,M1);
        MAJS2:MA(JS,M2);
        MAJS3:MA(JS,M3);
        输出加速线 = 100*(收盘价-N日前的收盘价)/(N*N日前的收盘价)
        输出MAJS1 = JS的M1日简单移动平均
        输出MAJS2 = JS的M2日简单移动平均
        输出MAJS3 = JS的M3日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M1：统计的天数 M1
        M2：统计的天数 M2
        M3：统计的天数 M3
    输出：
        JS, MAJS1, MAJS2和MAJS3 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def MACD(security_list, check_date, SHORT=12, LONG=26, MID=9, unit='1d', include_now=True):
    '''
    计算公式：
        DIF:EMA(CLOSE,SHORT)-EMA(CLOSE,LONG);
        DEA:EMA(DIF,MID);
        MACD:(DIF-DEA)*2,COLORSTICK;
        输出DIF = 收盘价的SHORT日指数移动平均-收盘价的LONG日指数移动平均
        输出DEA = DIF的MID日指数移动平均
        输出平滑异同平均 = (DIF-DEA)*2,COLORSTICK
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        SHORT：统计的天数 SHORT
        LONG：统计的天数 LONG
        MID：统计的天数 MID
    输出：
        DIF, DEA和MACD的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def QACD(security_list, check_date, N1=12, N2=26, M=9, unit='1d', include_now=True):
    '''
    计算公式：
        DIF:EMA(CLOSE,N1)-EMA(CLOSE,N2);
        MACD:EMA(DIF,M);
        DDIF:DIF-MACD;
        输出DIF = 收盘价的N1日指数移动平均-收盘价的N2日指数移动平均
        输出平滑异同平均 = DIF的M日指数移动平均
        输出DDIF = DIF-MACD
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
        N2：统计的天数 N2
        M：统计的天数 M
    输出：
        DIF, MACD和DDIF的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def QR(index_stock, security_list, check_date, N=21, unit='1d', include_now=True):
    '''
    计算公式：
        个股: (CLOSE-REF(CLOSE,N))/REF(CLOSE,N)*100;
        大盘: (INDEXC-REF(INDEXC,N))/REF(INDEXC,N)*100;
        强弱值:EMA(个股-大盘,2),COLORSTICK;

        输出个股 = (收盘价-N日前的收盘价)/N日前的收盘价*100
        输出 大盘 = (大盘的收盘价-N日前的大盘的收盘价)/N日前的大盘的收盘价*100
        输出 强弱值 = 个股-大盘的2日指数移动平均,COLORSTICK
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        个股，大盘和强弱指标的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def TRIX(security_list, check_date, N=12, M=9, unit='1d', include_now=True):
    '''
    计算公式：
        MTR = 收盘价的N日指数移动平均的N日指数移动平均的N日指数移动平均
        输出三重指数平均线TRIX = (MTR-1日前的MTR)/1日前的MTR*100
        输出MATRIX = TRIX的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        TRIX和MATRIX的值
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为TRIX和MATRIX。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def UOS(security_list, check_date, N1=7, N2=14, N3=28, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        TH = 最高价和1日前的收盘价的较大值
        TL = 最低价和1日前的收盘价的较小值
        ACC1 = 收盘价-TL的N1日累和/TH-TL的N1日累和
        ACC2 = 收盘价-TL的N2日累和/TH-TL的N2日累和
        ACC3 = 收盘价-TL的N3日累和/TH-TL的N3日累和
        输出终极指标 = (ACC1*N2*N3+ACC2*N1*N3+ACC3*N1*N2)*100/(N1*N2+N1*N3+N2*N3)
        输出MAUOS = UOS的M日指数平滑移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
        N2：统计的天数 N2
        N3：统计的天数 N3
        M：统计的天数 M
    输出：
        终极指标和MAUOS的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def VMACD(security_list, check_date, SHORT=12, LONG=26, MID=9, unit='1d', include_now=True):
    '''
    计算公式：
        DIF:EMA(VOL,SHORT)-EMA(VOL,LONG);
        DEA:EMA(DIF,MID);
        MACD:DIF-DEA,COLORSTICK;
        输出DIF:成交量(手)的SHORT日指数移动平均-成交量(手)的LONG日指数移动平均
        输出DEA:DIF的MID日指数移动平均
        输出平滑异同平均:DIF-DEA,COLORSTICK
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        SHORT：统计的天数 SHORT
        LONG：统计的天数 LONG
        MID：统计的天数 MID
    输出：
        DIF, DEA和MACD 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为DIF, DEA和MACD。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def VPT(security_list, check_date, N=51, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        VPT:SUM(VOL*(CLOSE-REF(CLOSE,1))/REF(CLOSE,1),N);
        MAVPT:MA(VPT,M);
        输出量价曲线VPT = 成交量(手)*(收盘价-1日前的收盘价)/1日前的收盘价的N日累和
        输出MAVPT = VPT的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        VPT 和 MAVPT 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def WVAD(security_list, check_date, N=24, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        WVAD:SUM((CLOSE-OPEN)/(HIGH-LOW)*VOL,N)/10000;
        MAWVAD:MA(WVAD,M);
        输出WVAD:(收盘价-开盘价)/(最高价-最低价)*成交量(手)的N日累和/10000
        输出MAWVAD:WVAD的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        WVAD 和 MAWVAD的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def PSY(security_list, check_date, timeperiod=12, unit='1d', include_now=True):
    '''
    计算公式：
        PSY:统计 N 日中满足收盘价>1日前的收盘价的天数/N*100
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数 N
    输出：0
        PSY 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def VR(security_list, check_date, N=26, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        TH:=SUM(IF(CLOSE>REF(CLOSE,1),VOL,0),N);
        TL:=SUM(IF(CLOSE<REF(CLOSE,1),VOL,0),N);
        TQ:=SUM(IF(CLOSE=REF(CLOSE,1),VOL,0),N);
        VR:100*(TH*2+TQ)/(TL*2+TQ);
        MAVR:MA(VR,M);
        TH赋值:如果收盘价>1日前的收盘价,返回成交量(手),否则返回0的N日累和
        TL赋值:如果收盘价<1日前的收盘价,返回成交量(手),否则返回0的N日累和
        TQ赋值:如果收盘价=1日前的收盘价,返回成交量(手),否则返回0的N日累和
        输出VR:100*(TH*2+TQ)/(TL*2+TQ)
        输出MAVR:VR的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        VR和MAVR 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def BRAR(security_list, check_date, N=26, unit='1d', include_now=True):
    '''
    计算公式：
        BR:SUM(MAX(0,HIGH-REF(CLOSE,1)),N)/SUM(MAX(0,REF(CLOSE,1)-LOW),N)*100;
        AR:SUM(HIGH-OPEN,N)/SUM(OPEN-LOW,N)*100;
        输出BR:0和最高价-1日前的收盘价的较大值的N日累和/0和1日前的收盘价-最低价的较大值的N日累和*100
        输出AR:最高价-开盘价的N日累和/开盘价-最低价的N日累和*100
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        BR和AR 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CR(security_list, check_date, N=26, M1=10, M2=20, M3=40, M4=62, unit='1d', include_now=True):
    '''
    计算公式：
        MID:=REF(HIGH+LOW,1)/2;
        CR:SUM(MAX(0,HIGH-MID),N)/SUM(MAX(0,MID-LOW),N)*100;
        MA1:REF(MA(CR,M1),M1/2.5+1);
        MA2:REF(MA(CR,M2),M2/2.5+1);
        MA3:REF(MA(CR,M3),M3/2.5+1);
        MA4:REF(MA(CR,M4),M4/2.5+1);
        MID赋值:1日前的最高价+最低价/2
        输出带状能量线:0和最高价-MID的较大值的N日累和/0和MID-最低价的较大值的N日累和*100
        输出MA1:M1/2.5+1日前的CR的M1日简单移动平均
        输出均线:M2/2.5+1日前的CR的M2日简单移动平均
        输出MA3:M3/2.5+1日前的CR的M3日简单移动平均
        输出MA4:M4/2.5+1日前的CR的M4日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M1：统计的天数 M1
        M2：统计的天数 M2
        M3：统计的天数 M3
        M4：统计的天数 M4
    输出：
        CR和MA1，MA2，MA3，MA4 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CYR(security_list, check_date, N=13, M=5, unit='1d', include_now=True):
    '''
    计算公式：
        DIVE:=0.01*EMA(AMOUNT,N)/EMA(VOL,N);
        CYR:(DIVE/REF(DIVE,1)-1)*100;
        MACYR:MA(CYR,M);
        DIVE赋值:0.01*成交额(元)的N日指数移动平均/成交量(手)的N日指数移动平均
        输出市场强弱:(DIVE/1日前的DIVE-1)*100
        输出MACYR:CYR的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        CYR和MACYR 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def MASS(security_list, check_date, N1=9, N2=25, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        MASS:SUM(MA(HIGH-LOW,N1)/MA(MA(HIGH-LOW,N1),N1),N2);
        MAMASS:MA(MASS,M);
        输出梅斯线:最高价-最低价的N1日简单移动平均/最高价-最低价的N1日简单移动平均的N1日简单移动平均的N2日累和
        输出MAMASS:MASS的M日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
        N2：统计的天数 N2
        M：统计的天数 M
    输出：
        MASS和MAMASS 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def PCNT(security_list, check_date, M=5, unit='1d', include_now=True):
    '''
    计算公式：
        PCNT:(CLOSE-REF(CLOSE,1))/CLOSE*100;
        MAPCNT:EXPMEMA(PCNT,M);
        输出幅度比:(收盘价-1日前的收盘价)/收盘价*100
        输出MAPCNT:PCNT的M日指数平滑移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        M：统计的天数 M
    输出：
        PCNT和MAPCNT 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def OBV(security_list, check_date, timeperiod=30, unit='1d', include_now=True):
    '''
    计算公式：
        VA = 如果收盘价>1日前的收盘价,返回成交量(手),否则返回-成交量(手)
        OBV = 如果收盘价=1日前的收盘价,返回0,否则返回VA的历史累和
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数 N
    输出：
        OBV 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def AMO(security_list, check_date, M1=5, M2=10, unit='1d', include_now=True):
    '''
    计算公式：
        AMOW:AMOUNT/10000.0,VOLSTICK;
        AMO1:MA(AMOW,M1);
        AMO2:MA(AMOW,M2);
        输出AMOW:成交额(元)/10000.0,VOLSTICK
        输出AMO1:AMOW的M1日简单移动平均
        输出AMO2:AMOW的M2日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        M1：统计的天数 M1
        M2：统计的天数 M2
    输出：
        AMOW，AMO1和AMO2 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CCL(futures_list, check_date, M=5):
    '''
    计算公式：
        持仓量:VOLINSTK;
        MACCL:MA(持仓量,M);
        输出持仓量:持仓量
        输出MACCL:持仓量的M日简单移动平均
    输入：
        futures_list:期货代码列表
        check_date：要查询数据的日期
        M：统计的天数 M
    输出：
        CCL和MACCL 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def DBLB(index_stock, security_list, check_date, N=5, M=5, unit='1d', include_now=True):
    '''
    计算公式：
        GG:=VOL/SUM(REF(VOL,1),N);
        ZS:=INDEXV/SUM(REF(INDEXV,1),N);
        DBLB:GG/ZS;
        MADBLB:MA(DBLB,M);
        GG赋值:成交量(手)/1日前的成交量(手)的N日累和
        ZS赋值:大盘的成交量/1日前的大盘的成交量的N日累和
        输出对比量比(需下载日线):GG/ZS
        输出MADBLB:DBLB的M日简单移动平均
    输入：
        index_stock: 大盘股票代码
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        DBLB和MADBLB 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def DBQRV(index_stock, security_list, check_date, N=5, unit='1d', include_now=True):
    '''
    计算公式：
        ZS:(INDEXV-REF(INDEXV,N))/REF(INDEXV,N);
        GG:(VOL-REF(VOL,N))/REF(VOL,N);
        输出ZS:(大盘的成交量-N日前的大盘的成交量)/N日前的大盘的成交量
        输出GG:(成交量(手)-N日前的成交量(手))/N日前的成交量(手)
    输入：
        index_stock: 大盘股票代码
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        ZS和GG 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def HSL(security_list, check_date, N=5, unit='1d', include_now=True):
    '''
    计算公式：
        HSL:IF((SETCODE==0||SETCODE==1),100*VOL,VOL)/(FINANCE(7)/100);
        MAHSL:MA(HSL,N);
        输出换手线:如果(市场类型(0或者市场类型或者1),返回100*成交量(手),否则返回成交量(手)/(流通股本(股)/100)
        输出MAHSL:HSL的N日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        HSL和MAHSL 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def VOL(security_list, check_date, M1=5, M2=10, unit='1d', include_now=True):
    '''
    计算公式：
        VOLUME:VOL,VOLSTICK;
        MAVOL1:MA(VOLUME,M1);
        MAVOL2:MA(VOLUME,M2);
        输出VOLUME:成交量(手),VOLSTICK
        输出MAVOL1:VOLUME的M1日简单移动平均
        输出MAVOL2:VOLUME的M2日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：统计的天数 M
    输出：
        VOL和MAVOL 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def VRSI(security_list, check_date, N1=6, N2=12, N3=24, unit='1d', include_now=True):
    '''
    计算公式：
        LC:=REF(VOL,1);
        RSI1:SMA(MAX(VOL-LC,0),N1,1)/SMA(ABS(VOL-LC),N1,1)*100;
        RSI2:SMA(MAX(VOL-LC,0),N2,1)/SMA(ABS(VOL-LC),N2,1)*100;
        RSI3:SMA(MAX(VOL-LC,0),N3,1)/SMA(ABS(VOL-LC),N3,1)*100;
        LC赋值:1日前的成交量(手)
        输出RSI1:成交量(手)-LC和0的较大值的N1日[1日权重]移动平均/成交量(手)-LC的绝对值的N1日[1日权重]移动平均*100
        输出RSI2:成交量(手)-LC和0的较大值的N2日[1日权重]移动平均/成交量(手)-LC的绝对值的N2日[1日权重]移动平均*100
        输出RSI3:成交量(手)-LC和0的较大值的N3日[1日权重]移动平均/成交量(手)-LC的绝对值的N3日[1日权重]移动平均*100
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N1：统计的天数 N1
        N2：统计的天数 N2
        N3：统计的天数 N3
    输出：
        RSI1，VRSI2和VRSI3 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def BBI(security_list, check_date, timeperiod1=3, timeperiod2=6, timeperiod3=12, timeperiod4=24, unit='1d', include_now=True):
    '''
    计算公式：
        BBI:(MA(CLOSE,M1)+MA(CLOSE,M2)+MA(CLOSE,M3)+MA(CLOSE,M4))/4;
        输出多空均线BBI:(收盘价的M1日简单移动平均+收盘价的M2日简单移动平均+收盘价的M3日简单移动平均+收盘价的M4日简单移动平均)/4
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod1：统计的天数 N1
        timeperiod2：统计的天数 N2
        timeperiod3：统计的天数 N3
        timeperiod4：统计的天数 N4
    输出：
        BBI 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def MA(security_list, check_date, timeperiod=5, unit='1d', include_now=True):
    '''
    计算公式：
        MA1:MA(CLOSE,M1);
        输出MA1:收盘价的M1日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数timeperiod
    输出：
        MA1 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def EXPMA(security_list, check_date, timeperiod=12, unit='1d', include_now=True):
    '''
    计算公式：
        EXPMA:EMA(CLOSE,timeperiod)
        输出EXP:收盘价的timeperiod日指数移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        EXPMA 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def HMA(security_list, check_date, timeperiod=12, unit='1d', include_now=True):
    '''
    计算公式：
        HMA:MA(HIGH,timeperiod);
        输出HMA:最高价的timeperiod日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        HMA 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def LMA(security_list, check_date, timeperiod=12, unit='1d', include_now=True):
    '''
    计算公式：
        LMA:MA(LOW,timeperiod)
        LMA:最低价的timeperiod日的平均值
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        LMA 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def VMA(security_list, check_date, timeperiod=12, unit='1d', include_now=True):
    '''
    计算公式：
        VV:=(HIGH+OPEN+LOW+CLOSE)/4
        VMA:MA(VV,timeperiod)
        VV赋值:(最高价+开盘价+最低价+收盘价)/4
        输出VMA:VV的timeperiod日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        VMA 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ALLIGAT(security_list, check_date, timeperiod=21, unit='1d', include_now=True):
    '''
    计算公式：
        NN:=(H+L)/2;
        上唇:REF(MA(NN,5),3)
        牙齿:REF(MA(NN,8),5)
        下颚:REF(MA(NN,13),8)
        NN赋值:(最高价+最低价)/2
        输出上唇:3日前的NN的5日简单移动平均
        输出牙齿:5日前的NN的8日简单移动平均
        输出下颚:8日前的NN的13日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        上唇 牙齿 下颚 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def AMV(security_list, check_date, timeperiod=13, unit='1d', include_now=True):
    '''
    计算公式：
        AMOV:=VOL*(OPEN+CLOSE)/2;
        AMV:SUM(AMOV,timeperiod)/SUM(VOL,timeperiod);
        AMOV赋值:成交量(手)*(开盘价+收盘价)/2
        输出AMV:AMOV的timeperiod日累和/成交量(手)的timeperiod日累和
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        AMV 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def BBIBOLL(security_list, check_date, N=11, M=6, unit='1d', include_now=True):
    '''
    计算公式：
        CV:=CLOSE;
        BBIBOLL:(MA(CV,3)+MA(CV,6)+MA(CV,12)+MA(CV,24))/4;
        UPR:BBIBOLL+M*STD(BBIBOLL,N);
        DWN:BBIBOLL-M*STD(BBIBOLL,N);
        CV赋值:收盘价
        输出多空布林线:(CV的3日简单移动平均+CV的6日简单移动平均+CV的12日简单移动平均+CV的24日简单移动平均)/4
        输出UPR:BBIBOLL+M*BBIBOLL的N日估算标准差
        输出DWN:BBIBOLL-M*BBIBOLL的N日估算标准差
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数
        M：统计的天数
    输出：
        BBIBOLL UPR DWN 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def Bollinger_Bands(security_list, check_date, timeperiod=20, nbdevup=2, nbdevdn=2, unit='1d', include_now=True):
    '''
    计算公式：
        LB:BOLL - nbdevup*STD(CLOSE,timeperiod);
        BOLL:MA(CLOSE,timeperiod);
        UB:BOLL + nbdevdn*STD(CLOSE,timeperiod);
        输出BOLL = 收盘价的M日简单移动平均
        输出LB = BOLL - nbdevup*收盘价的M日估算标准差
        输出UB = BOLL + nbdevdn*收盘价的M日估算标准差
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数 timeperiod
        nbdevup：统计的天数 nbdevup
        nbdevdn：统计的天数 nbdevdn
    输出：
        上轨线UB 、中轨线MB、下轨线LB 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ENE(security_list, check_date, N=25, M1=6, M2=6, unit='1d', include_now=True):
    '''
    计算公式：
        UPPER:(1+M1/100)*MA(CLOSE,N);
        LOWER:(1-M2/100)*MA(CLOSE,N);
        ENE:(UPPER+LOWER)/2;
        输出UPPER:(1+M1/100)*收盘价的N日简单移动平均
        输出LOWER:(1-M2/100)*收盘价的N日简单移动平均
        输出轨道线:(UPPER+LOWER)/2
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数
        M1：统计的天数
        M2：统计的天数
    输出：
        UPPER LOWER ENE 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def MIKE(security_list, check_date, timeperiod=10, unit='1d', include_now=True):
    '''
    计算公式：
        HLC:=REF(MA((HIGH+LOW+CLOSE)/3,timeperiod),1);
        HV:=EMA(HHV(HIGH,timeperiod),3);
        LV:=EMA(LLV(LOW,timeperiod),3);
        STOR:EMA(2*HV-LV,3);
        MIDR:EMA(HLC+HV-LV,3);
        WEKR:EMA(HLC*2-LV,3);
        WEKS:EMA(HLC*2-HV,3);
        MIDS:EMA(HLC-HV+LV,3);
        STOS:EMA(2*LV-HV,3);
        HLC赋值:1日前的(最高价+最低价+收盘价)/3的timeperiod日简单移动平均
        HV赋值:timeperiod日内最高价的最高值的3日指数移动平均
        LV赋值:timeperiod日内最低价的最低值的3日指数移动平均
        输出STOR:2*HV-LV的3日指数移动平均
        输出MIDR:HLC+HV-LV的3日指数移动平均
        输出WEKR:HLC*2-LV的3日指数移动平均
        输出WEKS:HLC*2-HV的3日指数移动平均
        输出MIDS:HLC-HV+LV的3日指数移动平均
        输出STOS:2*LV-HV的3日指数移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        STOR, MIDR, WEKR, WEKS, MIDS, STOS 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def PBX(security_list, check_date, timeperiod=9, unit='1d', include_now=True):
    '''
    计算公式：
        PBX:(EMA(CLOSE,timeperiod)+MA(CLOSE,timeperiod*2)+MA(CLOSE,timeperiod*4))/3;
        输出PBX:(收盘价的timeperiod日指数移动平均+收盘价的timeperiod*2日简单移动平均+收盘价的timeperiod*4日简单移动平均)/3
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        PBX 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def XS(security_list, check_date, timeperiod=13, unit='1d', include_now=True):
    '''
    计算公式：
        VAR2:=CLOSE*VOL;
        VAR3:=EMA((EMA(VAR2,3)/EMA(VOL,3)+EMA(VAR2,6)/EMA(VOL,6)+EMA(VAR2,12)/EMA(VOL,12)+EMA(VAR2,24)/EMA(VOL,24))/4,N);
        SUP:1.06*VAR3;
        SDN:VAR3*0.94;
        VAR4:=EMA(CLOSE,9);
        LUP:EMA(VAR4*1.14,5);
        LDN:EMA(VAR4*0.86,5);
        VAR2赋值:收盘价*成交量(手)
        VAR3赋值:(VAR2的3日指数移动平均/成交量(手)的3日指数移动平均+VAR2的6日指数移动平均/成交量(手)的6日指数移动平均+VAR2的12日指数移动平均/成交量(手)的12日指数移动平均+VAR2的24日指数移动平均/成交量(手)的24日指数移动平均)/4的N日指数移动平均
        输出SUP:1.06*VAR3
        输出SDN:VAR3*0.94
        VAR4赋值:收盘价的9日指数移动平均
        输出LUP:VAR4*1.14的5日指数移动平均
        输出LDN:VAR4*0.86的5日指数移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        SUP SDN LUP LDN 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def XS2(security_list, check_date, N=102, M=7, unit='1d', include_now=True):
    '''
    计算公式：
        AA:=MA((2*CLOSE+HIGH+LOW)/4,5);
        通道1:AA*N/100;
        通道2:AA*(200-N)/100;
        CC:=ABS((2*CLOSE+HIGH+LOW)/4-MA(CLOSE,20))/MA(CLOSE,20);
        DD:=DMA(CLOSE,CC);
        通道3:(1+M/100)*DD;
        通道4:(1-M/100)*DD;
        AA赋值:(2*收盘价+最高价+最低价)/4的5日简单移动平均
        输出 通道1:AA*N/100
        输出 通道2:AA*(200-N)/100
        CC赋值:(2*收盘价+最高价+最低价)/4-收盘价的20日简单移动平均的绝对值/收盘价的20日简单移动平均
        DD赋值:以CC为权重收盘价的动态移动平均
        输出 通道3:(1+M/100)*DD
        输出 通道4:(1-M/100)*DD
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数
        M：统计的天数
    输出：
        PASS1, PASS2, PASS3, PASS4 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def EMA(security_list, check_date, timeperiod=30, unit='1d', include_now=True):
    '''
    计算公式：
        若Y=EMA(X,N)，则Y=[(2/N+1) * X+(N-1/N+1) * Y'],其中Y'表示上一周期Y值。
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数 timeperiod
    输出：
        EMA（指数移动平均）的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def SMA(security_list, check_date, N=7, M=1, unit='1d', include_now=True):
    '''
    计算公式：
        计算SMA(X, N, M)， 即X的N日移动平均，M为权重。
        若Y=SMA(X,N,M) 则 Y = (M*X+(N-M)*Y')/N, 其中Y'表示上一周期Y值,N必须大于M。
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
        M：权重 M
    输出：
        SMA(X的 N 日移动平均) 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def BDZX(security_list, check_date, timeperiod=40, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=(HIGH+LOW+CLOSE*2)/4;
        VAR2:=EMA(VAR1,21);
        VAR3:=STD(VAR1,21);
        VAR4:=((VAR1-VAR2)/VAR3*100+200)/4;
        VAR5:(EMA(VAR4,5)-25)*1.56;
        AK: EMA(VAR5,2)*1.22;
        AD1: EMA(AK,2);
        AJ: 3*AK-2*AD1;
        AA:100;
        BB:0;
        CC:80;
        买进: IF(CROSS(AK,AD1),58,20);
        卖出: IF(CROSS(AD1,AK),58,20);
        VAR1赋值:(最高价+最低价+收盘价*2)/4
        VAR2赋值:VAR1的21日指数移动平均
        VAR3赋值:VAR1的21日估算标准差
        VAR4赋值:((VAR1-VAR2)/VAR3*100+200)/4
        输出VAR5:(VAR4的5日指数移动平均-25)*1.56
        输出AK: VAR5的2日指数移动平均*1.22
        输出AD1: AK的2日指数移动平均
        输出AJ: 3*AK-2*AD1
        输出AA:100
        输出布林极限:0
        输出CC:80
        输出买进: 如果AK上穿AD1,返回58,否则返回20
        输出卖出: 如果AD1上穿AK,返回58,否则返回20
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        AK AD1 AJ AA BB CC BUY SELL的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CDP_STD(security_list, check_date, timeperiod=2, unit='1d', include_now=True):
    '''
    计算公式：
        CH:=REF(H,1);
        CL:=REF(L,1);
        CC:=REF(C,1);
        CDP:(CH+CL+CC)/3;
        AH:2*CDP+CH-2*CL;
        NH:CDP+CDP-CL;
        NL:CDP+CDP-CH;
        AL:2*CDP-2*CH+CL;
        CH赋值:1日前的最高价
        CL赋值:1日前的最低价
        CC赋值:1日前的收盘价
        输出CDP:(CH+CL+CC)/3
        输出AH:2*CDP+CH-2*CL
        输出NH:CDP+CDP-CL
        输出NL:CDP+CDP-CH
        输出AL:2*CDP-2*CH+CL
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        CDP AH NH NL AL的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CJDX(security_list, check_date, timeperiod=16, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=(2*CLOSE+HIGH+LOW)/4;
        VAR2:=EMA(EMA(EMA(VAR1,4),4),4);
        J: (VAR2-REF(VAR2,1))/REF(VAR2,1)*100, COLORSTICK;
        D: MA(J,3);
        K: MA(J,1);
        VAR1赋值:(2*收盘价+最高价+最低价)/4
        VAR2赋值:VAR1的4日指数移动平均的4日指数移动平均的4日指数移动平均
        输出J: (VAR2-1日前的VAR2)/1日前的VAR2*100, COLORSTICK
        输出D: J的3日简单移动平均
        输出K: J的1日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        J D X 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CYHT(security_list, check_date, timeperiod=60, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=(2*CLOSE+HIGH+LOW+OPEN)/5;
        高抛: 80;
        VAR2:=LLV(LOW,34);
        VAR3:=HHV(HIGH,34);
        SK: EMA((VAR1-VAR2)/(VAR3-VAR2)*100,13);
        SD: EMA(SK,3);
        低吸: 20;
        强弱分界: 50;
        VAR4:=IF(CROSS(SK,SD),40,22);
        VAR5:=IF(CROSS(SD,SK),60,78);
        卖出: VAR5;
        买进: VAR4;
        VAR1赋值:(2*收盘价+最高价+最低价+开盘价)/5
        输出高抛: 80
        VAR2赋值:34日内最低价的最低值
        VAR3赋值:34日内最高价的最高值
        输出SK: (VAR1-VAR2)/(VAR3-VAR2)*100的13日指数移动平均
        输出SD: SK的3日指数移动平均
        输出低吸: 20
        输出强弱分界: 50
        VAR4赋值:如果SK上穿SD,返回40,否则返回22
        VAR5赋值:如果SD上穿SK,返回60,否则返回78
        输出卖出: VAR5
        输出买进: VAR4
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        高抛 SK SD 低吸 强弱分界 卖出 买进的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def JAX(security_list, check_date, timeperiod=30, unit='1d', include_now=True):
    '''
    计算公式：
        AA:=ABS((2*CLOSE+HIGH+LOW)/4-MA(CLOSE,N))/MA(CLOSE,N);
        济安线:DMA((2*CLOSE+LOW+HIGH)/4,AA)
        CC:=(CLOSE/济安线);
        MA1:=MA(CC*(2*CLOSE+HIGH+LOW)/4,3);
        MAAA:=((MA1-济安线)/济安线)/3;
        TMP:=MA1-MAAA*MA1;
        J:IF(TMP<=济安线,济安线,DRAWNULL)
        A:TMP
        X:IF(TMP<=济安线,TMP,DRAWNULL)
        AA赋值:(2*收盘价+最高价+最低价)/4-收盘价的timeperiod日简单移动平均的绝对值/收盘价的timeperiod日简单移动平均
        输出济安线:以AA为权重(2*收盘价+最低价+最高价)/4的动态移动平均
        CC赋值:(收盘价/济安线)
        MA1赋值:CC*(2*收盘价+最高价+最低价)/4的3日简单移动平均
        MAAA赋值:((MA1-济安线)/济安线)/3
        TMP赋值:MA1-MAAA*MA1
        输出J:如果TMP<=济安线,返回济安线,否则返回无效数
        输出A:TMP
        输出X:如果TMP<=济安线,返回TMP,否则返回无效数
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        JAX J A X 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def JFZX(security_list, check_date, timeperiod=30, unit='1d', include_now=True):
    '''
    计算公式：
        VAR2:=SUM(IF(CLOSE>OPEN,VOL,0),timeperiod)/SUM(VOL,timeperiod)*100;
        VAR3:=100-SUM(IF(CLOSE>OPEN,VOL,0),timeperiod)/SUM(VOL,timeperiod)*100;
        多头力量: VAR2;
        空头力量: VAR3;
        多空平衡: 50;
        VAR2赋值:如果收阳线,返回成交量(手),否则返回0的timeperiod日累和/成交量(手)的timeperiod日累和*100
        VAR3赋值:100-如果收阳线,返回成交量(手),否则返回0的timeperiod日累和/成交量(手)的timeperiod日累和*100
        输出多头力量: VAR2
        输出空头力量: VAR3
        输出多空平衡: 50
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        多头力量 空头力量 多空平衡的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def JYJL(security_list, check_date, N=120, M=5, unit='1d', include_now=True):
    '''
    计算公式：
        单位时间总量: SUM(VOL,N)*100
        单位时间内均量: 单位时间总量/(N/M);
        输出单位时间总量: 成交量(手)的N日累和*100
        输出单位时间内均量: 单位时间总量/(N/M)
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数
        M：统计的天数
    输出：
        单位时间总量 单位时间内均量的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def LHXJ(security_list, check_date, timeperiod=100, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=(CLOSE*2+HIGH+LOW)/4;
        VAR2:=EMA(VAR1,13)-EMA(VAR1,34);
        VAR3:=EMA(VAR2,5);
        主力弃盘: (-2)*(VAR2-VAR3)*3.8;
        主力控盘: 2*(VAR2-VAR3)*3.8;
        VAR1赋值:(收盘价*2+最高价+最低价)/4
        VAR2赋值:VAR1的13日指数移动平均-VAR1的34日指数移动平均
        VAR3赋值:VAR2的5日指数移动平均
        输出主力弃盘: (-2)*(VAR2-VAR3)*3.8
        输出主力控盘: 2*(VAR2-VAR3)*3.8
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        弃盘 控盘 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def LYJH(security_list, check_date, M=80, M1=50, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=(HHV(HIGH,36)-CLOSE)/(HHV(HIGH,36)-LLV(LOW,36))*100;
        机构做空能量线: SMA(VAR1,2,1);
        VAR2:=(CLOSE-LLV(LOW,9))/(HHV(HIGH,9)-LLV(LOW,9))*100;
        机构做多能量线: SMA(VAR2,5,1)-8;
        LH: M;
        LH1: M1;
        VAR1赋值:(36日内最高价的最高值-收盘价)/(36日内最高价的最高值-36日内最低价的最低值)*100
        输出机构做空能量线: VAR1的2日[1日权重]移动平均
        VAR2赋值:(收盘价-9日内最低价的最低值)/(9日内最高价的最高值-9日内最低价的最低值)*100
        输出机构做多能量线: VAR2的5日[1日权重]移动平均-8
        输出LH: M
        输出LH1: M1
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        M：统计的天数
        M1：统计的天数
    输出：
        EMPTY MOST LH LH1的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def TBP_STD(security_list, check_date, timeperiod=30, unit='1d', include_now=True):
    '''
    计算公式：
        APX:=(H+L+C)/3;
        TR0:=MAX(H-L,MAX(ABS(H-REF(C,1)),ABS(L-REF(C,1))));
        MF0:=C-REF(C,2);
        MF1:=REF(MF0,1);
        MF2:=REF(MF0,2);
        DIRECT1:=BARSLAST(MF0>MF1 AND MF0>MF2);
        DIRECT2:=BARSLAST(MF0<MF1 AND MF0<MF2);
        DIRECT0:=IF(DIRECT1<DIRECT2,100,-100);
        TBP:REF(REF(C,1)+IF(DIRECT0>50,MIN(MF0,MF1),MAX(MF0,MF1)),1);
        多头获利:REF(IF(DIRECT0>50,APX*2-L,DRAWNULL),1),NODRAW;
        多头停损:REF(IF(DIRECT0>50,APX-TR0,DRAWNULL),1),NODRAW;
        空头回补:REF(IF(DIRECT0<-50,APX*2-H,DRAWNULL),1),NODRAW;
        空头停损:REF(IF(DIRECT0<-50,APX+TR0,DRAWNULL),1),NODRAW;
        APX赋值:(最高价+最低价+收盘价)/3
        TR0赋值:最高价-最低价和最高价-1日前的收盘价的绝对值和最低价-1日前的收盘价的绝对值的较大值的较大值
        MF0赋值:收盘价-2日前的收盘价
        MF1赋值:1日前的MF0
        MF2赋值:2日前的MF0
        DIRECT1赋值:上次MF0>MF1ANDMF0>MF2距今天数
        DIRECT2赋值:上次MF0<MF1ANDMF0<MF2距今天数
        DIRECT0赋值:如果DIRECT1<DIRECT2,返回100,否则返回-100
        输出TBP:1日前的1日前的收盘价+如果DIRECT0>50,返回MF0和MF1的较小值,否则返回MF0和MF1的较大值
        输出多头获利:1日前的如果DIRECT0>50,返回APX*2-最低价,否则返回无效数,NODRAW
        输出多头停损:1日前的如果DIRECT0>50,返回APX-TR0,否则返回无效数,NODRAW
        输出空头回补:1日前的如果DIRECT0<-50,返回APX*2-最高价,否则返回无效数,NODRAW
        输出空头停损:1日前的如果DIRECT0<-50,返回APX+TR0,否则返回无效数,NODRAW
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        tbp，多头获利，多头停损，空头回补和空头停损 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ZBCD(security_list, check_date, timeperiod=10, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=money/VOL/7;
        VAR2:=(3*HIGH+LOW+OPEN+2*CLOSE)/7;
        VAR3:=SUM(money,timeperiod)/VAR1/7;
        VAR4:=DMA(VAR2,VOL/VAR3);
        抄底:(CLOSE-VAR4)/VAR4*100
        VAR1赋值:成交额(元)/成交量(手)/7
        VAR2赋值:(3*最高价+最低价+开盘价+2*收盘价)/7
        VAR3赋值:成交额(元)的timeperiod日累和/VAR1/7
        VAR4赋值:以成交量(手)/VAR3为权重VAR2的动态移动平均
        输出抄底:(收盘价-VAR4)/VAR4*100
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        timeperiod：统计的天数
    输出：
        抄底 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def SG_SMX(index_stock, security_list, check_date, N=50, unit='1d', include_now=True):
    '''
    计算公式：
        H1:=HHV(HIGH,N);
        L1:=LLV(LOW,N);
        H2:=HHV(INDEXH,N);
        L2:=LLV(INDEXL,N);
        ZY:=CLOSE/INDEXC*2000;
        ZY1:EMA(ZY,3);
        ZY2:EMA(ZY,17);
        ZY3:EMA(ZY,34);
        H1赋值:N日内最高价的最高值
        L1赋值:N日内最低价的最低值
        H2赋值:N日内大盘的最高价的最高值
        L2赋值:N日内大盘的最低价的最低值
        ZY赋值:收盘价/大盘的收盘价*2000
        输出ZY1:ZY的3日指数移动平均
        输出ZY2:ZY的17日指数移动平均
        输出ZY3:ZY的34日指数移动平均
    输入：
        index_stock: 大盘股票代码
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        ZY1,ZY2和ZY3 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def XDT(index_stock, security_list, check_date, P1=5, P2=10, unit='1d', include_now=True):
    '''
    计算公式：
        QR:CLOSE/INDEXC*1000;
        MQR1:MA(QR,P1);
        MQR2:MA(QR,P2);
        输出强弱指标(需下载日线):收盘价/大盘的收盘价*1000
        输出MQR1:QR的P1日简单移动平均
        输出MQR2:QR的P2日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        P1：统计的天数 P1
        P2：统计的天数 P2
    输出：
        QR，MQR1和MAQR2 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def SG_LB(index_stock, security_list, check_date, unit='1d', include_now=True):
    '''
    计算公式：
        ZY2:=VOL/INDEXV*1000;
        量比:ZY2;
        MA5:MA(ZY2,5);
        MA10:MA(ZY2,10);
        ZY2赋值:成交量(手)/大盘的成交量*1000
        输出量比:ZY2
        输出MA5:ZY2的5日简单移动平均
        输出MA10:ZY2的10日简单移动平均
    输入：
        index_stock: 大盘股票代码
        security_list:股票列表
        check_date：要查询数据的日期
    输出：
        SG_LB,MA5和MA10的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def SG_PF(index_stock, security_list, check_date, unit='1d', include_now=True):
    '''
    计算公式：
        ZY1:=CLOSE/INDEXC*1000;
        A1:=IF(ZY1>=HHV(ZY1,3),10,0);
        A2:=IF(ZY1>=HHV(ZY1,5),15,0);
        A3:=IF(ZY1>=HHV(ZY1,10),20,0);
        A4:=IF(ZY1>=HHV(ZY1,2),10,0);
        A5:=COUNT(ZY1>REF(ZY1,1) ,9)*5;
        强势股评分:A1+A2+A3+A4+A5;
        ZY1赋值:收盘价/大盘的收盘价*1000
        A1赋值:如果ZY1>3日内ZY1的最高值,返回10,否则返回0
        A2赋值:如果ZY1>5日内ZY1的最高值,返回15,否则返回0
        A3赋值:如果ZY1>10日内ZY1的最高值,返回20,否则返回0
        A4赋值:如果ZY1>2日内ZY1的最高值,返回10,否则返回0
        A5赋值:统计9日中满足ZY1>1日前的ZY1的天数*5
        输出强势股评分:A1+A2+A3+A4+A5
    输入：
        index_stock：大盘股票代码
        security_list:股票列表
        check_date：要查询数据的日期
    输出：
        强势股评分 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ZLMM(security_list, check_date, unit='1d', include_now=True):
    '''
    计算公式：
        LC :=REF(CLOSE,1);
        RSI2:=SMA(MAX(CLOSE-LC,0),12,1)/SMA(ABS(CLOSE-LC),12,1)*100;
        RSI3:=SMA(MAX(CLOSE-LC,0),18,1)/SMA(ABS(CLOSE-LC),18,1)*100;
        MMS:MA(3*RSI2-2*SMA(MAX(CLOSE-LC,0),16,1)/SMA(ABS(CLOSE-LC),16,1)*100,3);
        MMM:EMA(MMS,8);
        MML:MA(3*RSI3-2*SMA(MAX(CLOSE-LC,0),12,1)/SMA(ABS(CLOSE-LC),12,1)*100,5);
        赋值:1日前的收盘价
        RSI2赋值:收盘价-LC和0的较大值的12日[1日权重]移动平均/收盘价-LC的绝对值的12日[1日权重]移动平均*100
        RSI3赋值:收盘价-LC和0的较大值的18日[1日权重]移动平均/收盘价-LC的绝对值的18日[1日权重]移动平均*100
        输出MMS:3*RSI2-2*收盘价-LC和0的较大值的16日[1日权重]移动平均/收盘价-LC的绝对值的16日[1日权重]移动平均*100的3日简单移动平均
        输出MMM:MMS的8日指数移动平均
        输出MML:3*RSI3-2*收盘价-LC和0的较大值的12日[1日权重]移动平均/收盘价-LC的绝对值的12日[1日权重]移动平均*100的5日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
    输出：
        MMS, MMM和MML 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def RAD(index_stock, security_list, check_date, D=3, S=30, M=30, unit='1d', include_now=True):
    '''
    计算公式：
        SM:=(OPEN+HIGH+CLOSE+LOW)/4;
        SMID:=MA(SM,D);
        IM:=(INDEXO+INDEXH+INDEXL+INDEXC)/4;
        IMID:=MA(IM,D);
        SI1:=(SMID-REF(SMID,1))/SMID;
        II:=(IMID-REF(IMID,1))/IMID;
        RADER1:SUM((SI1-II)*2,S)*1000;
        RADERMA:SMA(RADER1,M,1);
        SM赋值:(开盘价+最高价+收盘价+最低价)/4
        SMID赋值:SM的D日简单移动平均
        IM赋值:(大盘的开盘价+大盘的最高价+大盘的最低价+大盘的收盘价)/4
        IMID赋值:IM的D日简单移动平均
        SI1赋值:(SMID-1日前的SMID)/SMID
        II赋值:(IMID-1日前的IMID)/IMID
        输出RADER1:(SI1-II)*2的S日累和*1000
        输出RADERMA:RADER1的M日[1日权重]移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        D：统计的天数 D
        S：统计的天数 S
        M：统计的天数 M
    输出：
        RADER1和RADERMA 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def SHT(security_list, check_date, N=5, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=MA((VOL-REF(VOL,1))/REF(VOL,1),5);
        VAR2:=(CLOSE-MA(CLOSE,24))/MA(CLOSE,24)*100;
        MY: VAR2*(1+VAR1);
        SHT: MY, COLORSTICK;
        SHTMA: MA(SHT,N);
        VAR1赋值:(成交量(手)-1日前的成交量(手))/1日前的成交量(手)的5日简单移动平均
        VAR2赋值:(收盘价-收盘价的24日简单移动平均)/收盘价的24日简单移动平均*100
        输出MY: VAR2*(1+VAR1)
        输出龙系短线: MY, COLORSTICK
        输出SHTMA: SHT的N日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        SHT和SHTMA 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CYW(security_list, check_date, unit='1d', include_now=True):
    '''
    计算公式：
        VAR1:=CLOSE-LOW;
        VAR2:=HIGH-LOW;
        VAR3:=CLOSE-HIGH;
        VAR4:=IF(HIGH>LOW,(VAR1/VAR2+VAR3/VAR2)*VOL,0);
        CYW: SUM(VAR4,10)/10000, COLORSTICK;
        VAR1赋值:收盘价-最低价
        VAR2赋值:最高价-最低价
        VAR3赋值:收盘价-最高价
        VAR4赋值:如果最高价>最低价,返回(VAR1/VAR2+VAR3/VAR2)*成交量(手),否则返回0
        输出主力控盘: VAR4的10日累和/10000, COLORSTICK
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
    输出：
        主力控盘 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CYS(security_list, check_date, unit='1d', include_now=True):
    '''
    计算公式：
        CYC13:=0.01*EMA(AMOUNT,13)/EMA(VOL,13);
        CYS:(CLOSE-CYC13)/CYC13*100;
        CYC13赋值:0.01*成交额(元)的13日指数移动平均/成交量(手)的13日指数移动平均
        输出市场盈亏:(收盘价-CYC13)/CYC13*100
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
    输出：
        市场盈亏 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ZSDB(index_stock, check_date, unit='1d', include_now=True):
    '''
    计算公式：
        A:=REF(INDEXC,1);
        指数涨幅:IF(A>0,(INDEXC-A)*100/A,0),NODRAW;
        输出A:1日前的大盘的收盘价
        输出指数涨幅:如果A>0,返回(大盘的收盘价-A)*100/A,否则返回0,NODRAW
    输入：
        index_stock：大盘股票代码
        check_date：要查询数据的日期
    输出：
        A和指数涨幅 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def AROON(security_list, check_date, N=25, unit='1d', include_now=True):
    '''
    计算公式：
        上轨:(N-HHVBARS(H,N))/N*100,COLORRED;
        下轨:(N-LLVBARS(H,N))/N*100,COLORGREEN;
        输出上轨:(N-N日内最高价的最大值距今天数)/N*100,画红色
        输出下轨:(N-N日内最高价的最小值距今天数)/N*100,画绿色
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        上轨和下轨 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def CFJT(security_list, check_date, MM=200, unit='1d', include_now=True):
    '''
    计算公式：
        突破:=REF(EMA(C,14),1);
        A1X:=(EMA(C,10)-突破)/突破*100;
        多方:=IF(A1X>=0,REF(EMA(C,10),BARSLAST(CROSS(A1X,0))+1),DRAWNULL);
        空方:=IF(A1X<0,REF(EMA(C,10),BARSLAST(CROSS(0,A1X))+1),DRAWNULL);
        突破赋值:1日前的收盘价的14日指数移动平均
        A1X赋值:(收盘价的10日指数移动平均-突破)/突破*100
        多方赋值:如果A1X>=0,返回上次A1X上穿0距今天数+1日前的收盘价的10日指数移动平均,否则返回无效数
        空方赋值:如果A1X<0,返回上次0上穿A1X距今天数+1日前的收盘价的10日指数移动平均,否则返回无效数
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        MM：统计的天数 MM
    输出：
        突破，A1X，多方和空方 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def ZX(security_list, check_date, unit='1d', include_now=True):
    '''
    计算公式：
        AV:0.01*AMOUNT/VOL;
        输出AV:0.01*成交额(元)/成交量(手)
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
    输出：
        AV 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def PUCU(security_list, check_date, N=24, unit='1d', include_now=True):
    '''
    计算公式：
        PU:MA(CLOSE,N);
        CU:MA(VOL,N);
        输出PU:收盘价的N日简单移动平均
        输出CU:成交量(手)的N日简单移动平均
    输入：
        security_list:股票列表
        check_date：要查询数据的日期
        N：统计的天数 N
    输出：
        PU和CU 的值。
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


@assert_auth
def LB(security_list, check_date, N=5):
    '''
    量比
    计算公式：
        它是指股市开市后平均每分钟的成交量与过去5个交易日平均每分钟成交量之比。
        量比=（当日成交总手数 / 当日累计交易分钟）/（过去N个交易日成交总手数/过去N个交易日的累计交易分钟）
    输入：
        security_list:股票列表
        check_date：要查询数据的日期/时间
        N：统计的天数 N
    输出：
        量比
    输出结果类型：
        字典(dict)：键(key)为股票代码，值(value)为数据。
    '''
    func_name = sys._getframe().f_code.co_name
    check_date = to_date_str(check_date)
    return JQDataClient.instance().get_technical_analysis(**locals())


__all__ = [k for k, v in sorted(globals().items()) if k == k.upper()]
__all__.extend(['Bollinger_Bands'])











