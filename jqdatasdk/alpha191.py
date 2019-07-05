# coding=utf-8
from .utils import assert_auth, to_date_str
from .client import JQDataClient
import sys


@assert_auth
def alpha_001(code, end_date=None, fq="pre"):
    """
    公式:
        (-1 * CORR(RANK(DELTA(LOG(VOLUME),1)),RANK(((CLOSE-OPEN)/OPEN)),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_002(code, end_date=None, fq="pre"):
    """
    公式:
        -1 * delta((((close-low)-(high-close))/((high-low)),1))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_003(code, end_date=None, fq="pre"):
    """
    公式:
        SUM((CLOSE=DELAY(CLOSE,1)?0:CLOSE-(CLOSE>DELAY(CLOSE,1)?MIN(LOW,DELAY(CLOSE,1)):MAX(HIGH,DELAY(CLOSE,1)))),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_004(code, end_date=None, fq="pre"):
    """
    公式:
        ((((SUM(CLOSE,8)/8)+STD(CLOSE,8))<(SUM(CLOSE,2)/2))?(-1*1):(((SUM(CLOSE,2)/2)<((SUM(CLOSE,8)/8)-STD(CLOSE,8)))?1:(((1<(VOLUME/MEAN(VOLUME,20)))||((VOLUME/MEAN(VOLUME,20))==1))?1:(-1*1))))
    Inputs:

        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_005(code, end_date=None, fq="pre"):
    """
    公式:
        (-1*TSMAX(CORR(TSRANK(VOLUME,5),YSRANK(HIGH,5),5),3))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_006(code, end_date=None, fq="pre"):
    """
    公式:
        (RANK(SIGN(DELTA((((OPEN*0.85)+(HIGH*0.15))),4)))*-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_007(code, end_date=None, fq="pre"):
    """
    公式:
        ((RANK(MAX((VWAP-CLOSE),3))+RANK(MIN((VWAP-CLOSE),3)))*RANK(DELTA(VOLUME,3)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_008(code, end_date=None, fq="pre"):
    """
    公式:
        RANK(DELTA(((((HIGH+LOW)/2)*0.2)+(VWAP*0.8)),4)*-1
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_009(code, end_date=None, fq="pre"):
    """
    公式:
        SMA(((HIGH+LOW)/2-(DELAY(HIGH,1)+DELAY(LOW,1))/*(HIGH-LOW)/VOLUME,7，2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_010(code, end_date=None, fq="pre"):
    """
    公式:
        (RANK(MAX(((RET<0)?STD(RET,20):CLOSE)^2),5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_011(code, end_date=None, fq="pre"):
    """
    公式:
        SUM(((CLOSE-LOW)-(HIGH-CLOSE))./(HIGH-LOW).*VOLUME,6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_012(code, end_date=None, fq="pre"):
    """
    公式:
        (RANK((OPEN-(SUM(VWAP,10)/10))))*(-1*(RANK(ABS((CLOSE-VWAP)))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_013(code, end_date=None, fq="pre"):
    """
    公式:
        (((HIGH*LOW)^0.5)-VWAP)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_014(code, end_date=None, fq="pre"):
    """
    公式:
        CLOSE-DELAY(CLOSE,5)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_015(code, end_date=None, fq="pre"):
    """
    公式:
        OPEN/DELAY(CLOSE,1)-1
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_016(code, end_date=None, fq="pre"):
    """
    公式:
        (-1*TSMAX(RANK(CORR(RANK(VOLUME),RANK(VWAP),5)),5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_017(code, end_date=None, fq="pre"):
    """
    公式:
        RANK((VWAP-MAX(VWAP,15)))^DELTA(CLOSE,5)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_018(code, end_date=None, fq="pre"):
    """
    公式:
        CLOSE/DELAY(CLOSE,5)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_019(code, end_date=None, fq="pre"):
    """
    公式:
        (CLOSE<DELAY(CLOSE,5)?(CLOSE-DELAY(CLOSE,5))/DELAY(CLOSE,5):(CLOSE=DELAY(CLOSE,5)?0:(CLOSE-DELAY(CLOSE,5))/CLOSE))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_020(code, end_date=None, fq="pre"):
    """
    公式:
        (CLOSE-DELAY(CLOSE,6))/DELAY(CLOSE,6)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_021(code, end_date=None, fq="pre"):
    """
    公式:
        REGBETA(MEAN(CLOSE,6),SEQUENCE(6))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_022(code, end_date=None, fq="pre"):
    """
    公式:
        SMEAN(((CLOSE-MEAN(CLOSE,6))/MEAN(CLOSE,6)-DELAY((CLOSE-MEAN(CLOSE,6))/MEAN(CLOSE,6),3)),12,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_023(code, end_date=None, fq="pre"):
    """
    公式:
        SMA((CLOSE>DELAY(CLOSE,1)?STD(CLOSE:20),0),20,1)/(SMA((CLOSE>DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1
        )+SMA((CLOSE<=DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1))*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())

@assert_auth
def alpha_024(code, end_date=None, fq="pre"):
    """
    公式:
        SMA(CLOSE-DELAY(CLOSE,5),5,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_025(code, end_date=None, fq="pre"):
    """
    公式:
        ((-1  *  RANK((DELTA(CLOSE,  7)  *  (1  -  RANK(DECAYLINEAR((VOLUME  /  MEAN(VOLUME,20)),  9))))))  *  (1  + RANK(SUM(RET, 250))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_026(code, end_date=None, fq="pre"):
    """
    公式:
        ((((SUM(CLOSE, 7) / 7) - CLOSE)) + ((CORR(VWAP, DELAY(CLOSE, 5), 230))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_027(code, end_date=None, fq="pre"):
    """
    公式:
        WMA((CLOSE-DELAY(CLOSE,3))/DELAY(CLOSE,3)*100+(CLOSE-DELAY(CLOSE,6))/DELAY(CLOSE,6)*100,12)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_028(code, end_date=None, fq="pre"):
    """
    公式:
        3*SMA((CLOSE-TSMIN(LOW,9))/(TSMAX(HIGH,9)-TSMIN(LOW,9))*100,3,1)-2*SMA(SMA((CLOSE-TSMIN(LOW,9))/( MAX(HIGH,9)-TSMAX(LOW,9))*100,3,1),3,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_029(code, end_date=None, fq="pre"):
    """
    公式:
       (CLOSE-DELAY(CLOSE,6))/DELAY(CLOSE,6)*VOLUME 
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_030(code, end_date=None, fq="pre"):
    """
    公式:
        WMA((REGRESI(CLOSE/DELAY(CLOSE)-1,MKT,SMB,HML，60))^2,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_031(code, end_date=None, fq="pre"):
    """
    公式:
        LOSE-MEAN(CLOSE,12))/MEAN(CLOSE,12)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_032(code, end_date=None, fq="pre"):
    """
    公式:
        (-1 * SUM(RANK(CORR(RANK(HIGH), RANK(VOLUME), 3)), 3))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_033(code, end_date=None, fq="pre"):
    """
    公式:
        ((((-1  *  TSMIN(LOW,  5))  +  DELAY(TSMIN(LOW,  5),  5))  *  RANK(((SUM(RET,  240)  -  SUM(RET,  20))  /  220)))    * TSRANK(VOLUME, 5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_034(code, end_date=None, fq="pre"):
    """
    公式:
        MEAN(CLOSE,12)/CLOSE
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_035(code, end_date=None, fq="pre"):
    """
    公式:
        (MIN(RANK(DECAYLINEAR(DELTA(OPEN,  1),  15)),  RANK(DECAYLINEAR(CORR((VOLUME),  ((OPEN  *  0.65)  + (OPEN *0.35)), 17),7))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_036(code, end_date=None, fq="pre"):
    """
    公式:
        RANK(SUM(CORR(RANK(VOLUME), RANK(VWAP)), 6), 2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_037(code, end_date=None, fq="pre"):
    """
    公式:
        (-1 * RANK(((SUM(OPEN, 5) * SUM(RET, 5)) - DELAY((SUM(OPEN, 5) * SUM(RET, 5)), 10))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_038(code, end_date=None, fq="pre"):
    """
    公式:
        (((SUM(HIGH, 20) / 20) < HIGH) ? (-1 * DELTA(HIGH, 2)) : 0)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_039(code, end_date=None, fq="pre"):
    """
    公式:
        ((RANK(DECAYLINEAR(DELTA((CLOSE), 2),8)) - RANK(DECAYLINEAR(CORR(((VWAP * 0.3) + (OPEN * 0.7)), SUM(MEAN(VOLUME,180), 37), 14), 12))) * -1
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_040(code, end_date=None, fq="pre"):
    """
    公式:
        SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:0),26)/SUM((CLOSE<=DELAY(CLOSE,1)?VOLUME:0),26)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_041(code, end_date=None, fq="pre"):
    """
    公式:
        (RANK(MAX(DELTA((VWAP), 3), 5))* -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_042(code, end_date=None, fq="pre"):
    """
    公式:
        (-1 * RANK(STD(HIGH, 10))) * CORR(HIGH, VOLUME, 10))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_043(code, end_date=None, fq="pre"):
    """
    公式:
        SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_044(code, end_date=None, fq="pre"):
    """
    公式:
        (TSRANK(DECAYLINEAR(CORR(((LOW )), MEAN(VOLUME,10), 7), 6),4) + TSRANK(DECAYLINEAR(DELTA((VWAP), 3), 10), 15))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_045(code, end_date=None, fq="pre"):
    """
    公式:
        (RANK(DELTA((((CLOSE * 0.6) + (OPEN *0.4))), 1)) * RANK(CORR(VWAP, MEAN(VOLUME,150), 15)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_046(code, end_date=None, fq="pre"):
    """
    公式:
        (MEAN(CLOSE,3)+MEAN(CLOSE,6)+MEAN(CLOSE,12)+MEAN(CLOSE,24))/(4*CLOSE)   
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_047(code, end_date=None, fq="pre"):
    """
    公式:
        SMA((TSMAX(HIGH,6)-CLOSE)/(TSMAX(HIGH,6)-TSMIN(LOW,6))*100,9,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_048(code, end_date=None, fq="pre"):
    """
    公式:
        (-1*((RANK(((SIGN((CLOSE-DELAY(CLOSE,1)))+SIGN((DELAY(CLOSE,1) - DELAY(CLOSE,2))))+SIGN((DELAY(CLOSE,2)-DELAY(CLOSE,3))))))*SUM(VOLUME,5))/SUM(VOLUME,20))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_049(code, end_date=None, fq="pre"):
    """
    公式:
        SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(L OW,1)))),12)/(SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(L OW-DELAY(LOW,1)))),12)+SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HI GH,1)),ABS(LOW-DELAY(LOW,1)))),12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_050(code, end_date=None, fq="pre"):
    """
    公式:
        SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(L OW,1)))),12)/(SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(L OW-DELAY(LOW,1)))),12)+SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HI GH,1)),ABS(LOW-DELAY(LOW,1)))),12))-SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(LOW,1)))),12)/(SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0: MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(LOW,1)))),12)+SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELA Y(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(LOW,1)))),12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_051(code, end_date=None, fq="pre"):
    """
    公式:
        SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(LOW-DELAY(L OW,1)))),12)/(SUM(((HIGH+LOW)<=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HIGH,1)),ABS(L OW-DELAY(LOW,1)))),12)+SUM(((HIGH+LOW)>=(DELAY(HIGH,1)+DELAY(LOW,1))?0:MAX(ABS(HIGH-DELAY(HI GH,1)),ABS(LOW-DELAY(LOW,1)))),12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_052(code, end_date=None, fq="pre"):
    """
    公式:
        SUM(MAX(0,HIGH-DELAY((HIGH+LOW+CLOSE)/3,1)),26)/SUM(MAX(0,DELAY((HIGH+LOW+CLOSE)/3,1)-L),26)* 100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_053(code, end_date=None, fq="pre"):
    """
    公式:
       COUNT(CLOSE>DELAY(CLOSE,1),12)/12*100 
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_054(code, end_date=None, fq="pre"):
    """
    公式:
       (-1 * RANK((STD(ABS(CLOSE - OPEN)) + (CLOSE - OPEN)) + CORR(CLOSE, OPEN,10))) 
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_055(code, end_date=None, fq="pre"):
    """
    公式:
        SUM(16*(CLOSE-DELAY(CLOSE,1)+(CLOSE-OPEN)/2+DELAY(CLOSE,1)-DELAY(OPEN,1))/((ABS(HIGH-DELAY(CL OSE,1))>ABS(LOW-DELAY(CLOSE,1))&ABS(HIGH-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))?ABS(HIGH-DELAY(CLOSE,1))+ABS(LOW-DELAY(CLOS E,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:(ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))   & ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(CLOSE,1))?ABS(LOW-DELAY(CLOSE,1))+ABS(HIGH-DELAY(CLO SE,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:ABS(HIGH-DELAY(LOW,1))+ABS(DELAY(CLOSE,1)-DELAY(OP EN,1))/4)))*MAX(ABS(HIGH-DELAY(CLOSE,1)),ABS(LOW-DELAY(CLOSE,1))),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_056(code, end_date=None, fq="pre"):
    """
    公式:
        (RANK((OPEN-TSMIN(OPEN,12)))<RANK((RANK(CORR(SUM(((HIGH+LOW)/2),19),SUM(MEAN(VOLUME,40),19),13))^5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_057(code, end_date=None, fq="pre"):
    """
    公式:
        SMA((CLOSE-TSMIN(LOW,9))/(TSMAX(HIGH,9)-TSMIN(LOW,9))*100,3,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_058(code, end_date=None, fq="pre"):
    """
    公式:
        COUNT(CLOSE>DELAY(CLOSE,1),20)/20*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_059(code, end_date=None, fq="pre"):
    """
    公式:
        SUM((CLOSE=DELAY(CLOSE,1)?0:CLOSE-(CLOSE>DELAY(CLOSE,1)?MIN(LOW,DELAY(CLOSE,1)):MAX(HIGH,D ELAY(CLOSE,1)))),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_060(code, end_date=None, fq="pre"):
    """
    公式:
        SUM(((CLOSE-LOW)-(HIGH-CLOSE))./(HIGH-LOW).*VOLUME,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_061(code, end_date=None, fq="pre"):
    """
    公式:
        (MAX(RANK(DECAYLINEAR(DELTA(VWAP,   1), 12)),RANK(DECAYLINEAR(RANK(CORR((LOW),MEAN(VOLUME,80), 8)), 17))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_062(code, end_date=None, fq="pre"):
    """
    公式:
        (-1 * CORR(HIGH, RANK(VOLUME), 5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_063(code, end_date=None, fq="pre"):
    """
    公式:
        SMA(MAX(CLOSE-DELAY(CLOSE,1),0),6,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),6,1)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_064(code, end_date=None, fq="pre"):
    """
    公式:
        (MAX(RANK(DECAYLINEAR(CORR(RANK(VWAP),  RANK(VOLUME),   4), 4)),RANK(DECAYLINEAR(MAX(CORR(RANK(CLOSE), RANK(MEAN(VOLUME,60)), 4), 13), 14))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_065(code, end_date=None, fq="pre"):
    """
    公式:
        MEAN(CLOSE,6)/CLOSE
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_066(code, end_date=None, fq="pre"):
    """
    公式:
        (CLOSE-MEAN(CLOSE,6))/MEAN(CLOSE,6)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_067(code, end_date=None, fq="pre"):
    """
    公式:
        SMA(MAX(CLOSE-DELAY(CLOSE,1),0),24,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),24,1)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_068(code, end_date=None, fq="pre"):
    """
    公式:
        SMA(((HIGH+LOW)/2-(DELAY(HIGH,1)+DELAY(LOW,1))/2)*(HIGH-LOW)/VOLUME,15,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_069(code, end_date=None, fq="pre"):
    """
    公式:
        (SUM(DTM,20)>SUM(DBM,20)？(SUM(DTM,20)-SUM(DBM,20))/SUM(DTM,20)：(SUM(DTM,20)=SUM(DBM,20)？0：(SUM(DTM,20)-SUM(DBM,20))/SUM(DBM,20)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_070(code, end_date=None, fq="pre"):
    """
    公式:
        STD(AMOUNT,6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_071(code, end_date=None, fq="pre"):
    """
    公式:
        (CLOSE-MEAN(CLOSE,24))/MEAN(CLOSE,24)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_072(code, end_date=None, fq="pre"):
    """
    公式:
        SMA((TSMAX(HIGH,6)-CLOSE)/(TSMAX(HIGH,6)-TSMIN(LOW,6))*100,15,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_073(code, end_date=None, fq="pre"):
    """
    公式:
        ((TSRANK(DECAYLINEAR(DECAYLINEAR(CORR((CLOSE),  VOLUME, 10),    16),    4), 5)  -RANK(DECAYLINEAR(CORR(VWAP, MEAN(VOLUME,30), 4),3))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_074(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(CORR(SUM(((LOW *   0.35)   +   (VWAP   *   0.65)), 20),    SUM(MEAN(VOLUME,40),    20),    7)) +RANK(CORR(RANK(VWAP), RANK(VOLUME), 6))) 
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_075(code,benchmark='000300.XSHG',end_date=None, fq="pre"):
    """
    公式:
       BANCHMARKINDEXCLOSE<BANCHMARKINDEXOPEN,50)/COUNT(BANCHMARKINDEXCLOSE<BANCHMARKIN DEXOPEN,50)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_076(code, end_date=None, fq="pre"):
    """
    公式:
       STD(ABS((CLOSE/DELAY(CLOSE,1)-1))/VOLUME,20)/MEAN(ABS((CLOSE/DELAY(CLOSE,1)-1))/VOLUME,20) 
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_077(code, end_date=None, fq="pre"):
    """
    公式:
       MIN(RANK(DECAYLINEAR(((((HIGH + LOW) / 2) + HIGH)  -  (VWAP + HIGH)), 20)), RANK(DECAYLINEAR(CORR(((HIGH + LOW) / 2), MEAN(VOLUME,40), 3), 6)))     
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_078(code, end_date=None, fq="pre"):
    """
    公式:
       ((HIGH+LOW+CLOSE)/3-MA((HIGH+LOW+CLOSE)/3,12))/(0.015*MEAN(ABS(CLOSE-MEAN((HIGH+LOW+CLOSE)/3,12)),12)) 
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_079(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_080(code, end_date=None, fq="pre"):
    """
    公式:
       (VOLUME-DELAY(VOLUME,5))/DELAY(VOLUME,5)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_081(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(VOLUME,21,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_082(code, end_date=None, fq="pre"):
    """
    公式:
       SMA((TSMAX(HIGH,6)-CLOSE)/(TSMAX(HIGH,6)-TSMIN(LOW,6))*100,20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_083(code, end_date=None, fq="pre"):
    """
    公式:
       (-1 * RANK(COVIANCE(RANK(HIGH), RANK(VOLUME), 5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_084(code, end_date=None, fq="pre"):
    """
    公式:
       SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_085(code, end_date=None, fq="pre"):
    """
    公式:
       (TSRANK((VOLUME / MEAN(VOLUME,20)), 20) * TSRANK((-1 * DELTA(CLOSE, 7)), 8))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_086(code, end_date=None, fq="pre"):
    """
    公式:
       ((0.25 < (((DELAY(CLOSE, 20) - DELAY(CLOSE, 10)) / 10) - ((DELAY(CLOSE, 10) - CLOSE) / 10))) ? (-1 * 1) :(((((DELAY(CLOSE, 20) - DELAY(CLOSE, 10)) / 10) - ((DELAY(CLOSE, 10) - CLOSE) / 10)) < 0) ? 1 : ((-1 * 1) * (CLOSE - DELAY(CLOSE, 1)))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_087(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK(DECAYLINEAR(DELTA(VWAP, 4), 7)) + TSRANK(DECAYLINEAR(((((LOW * 0.9) + (LOW * 0.1)) - VWAP) / (OPEN - ((HIGH + LOW) / 2))), 11), 7)) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_088(code, end_date=None, fq="pre"):
    """
    公式:
       (CLOSE-DELAY(CLOSE,20))/DELAY(CLOSE,20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_089(code, end_date=None, fq="pre"):
    """
    公式:
       2*(SMA(CLOSE,13,2)-SMA(CLOSE,27,2)-SMA(SMA(CLOSE,13,2)-SMA(CLOSE,27,2),10,2))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_090(code, end_date=None, fq="pre"):
    """
    公式:
       ( RANK(CORR(RANK(VWAP), RANK(VOLUME), 5)) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_091(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK((CLOSE - MAX(CLOSE, 5)))*RANK(CORR((MEAN(VOLUME,40)), LOW, 5))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_092(code, end_date=None, fq="pre"):
    """
    公式:
       (MAX(RANK(DECAYLINEAR(DELTA(((CLOSE  *   0.35)   +   (VWAP   *0.65)),    2), 3)),TSRANK(DECAYLINEAR(ABS(CORR((MEAN(VOLUME,180)), CLOSE, 13)), 5), 15)) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_093(code, end_date=None, fq="pre"):
    """
    公式:
       SUM((OPEN>=DELAY(OPEN,1)?0:MAX((OPEN-LOW),(OPEN-DELAY(OPEN,1)))),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_094(code, end_date=None, fq="pre"):
    """
    公式:
       SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),30)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_095(code, end_date=None, fq="pre"):
    """
    公式:
       STD(AMOUNT,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_096(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(SMA((CLOSE-TSMIN(LOW,9))/(TSMAX(HIGH,9)-TSMIN(LOW,9))*100,3,1),3,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_097(code, end_date=None, fq="pre"):
    """
    公式:
       STD(VOLUME,10)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_098(code, end_date=None, fq="pre"):
    """
    公式:
       ((((DELTA((SUM(CLOSE, 100) / 100), 100) / DELAY(CLOSE, 100)) < 0.05) || ((DELTA((SUM(CLOSE, 100) / 100), 100) /DELAY(CLOSE, 100)) == 0.05)) ? (-1 * (CLOSE - TSMIN(CLOSE, 100))) : (-1 * DELTA(CLOSE, 3)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_099(code, end_date=None, fq="pre"):
    """
    公式:
       (-1 * RANK(COVIANCE(RANK(CLOSE), RANK(VOLUME), 5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_100(code, end_date=None, fq="pre"):
    """
    公式:
       STD(VOLUME,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_101(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK(CORR(CLOSE, SUM(MEAN(VOLUME,30), 37), 15)) < RANK(CORR(RANK(((HIGH * 0.1) + (VWAP * 0.9))),RANK(VOLUME), 11))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_102(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(MAX(VOLUME-DELAY(VOLUME,1),0),6,1)/SMA(ABS(VOLUME-DELAY(VOLUME,1)),6,1)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_103(code, end_date=None, fq="pre"):
    """
    公式:
       ((20-LOWDAY(LOW,20))/20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_104(code, end_date=None, fq="pre"):
    """
    公式:
       (-1 * (DELTA(CORR(HIGH, VOLUME, 5), 5) * RANK(STD(CLOSE, 20))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_105(code, end_date=None, fq="pre"):
    """
    公式:
       (-1 * CORR(RANK(OPEN), RANK(VOLUME), 10))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_106(code, end_date=None, fq="pre"):
    """
    公式:
       CLOSE-DELAY(CLOSE,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_107(code, end_date=None, fq="pre"):
    """
    公式:
       (((-1 * RANK((OPEN - DELAY(HIGH, 1)))) * RANK((OPEN - DELAY(CLOSE, 1)))) * RANK((OPEN - DELAY(LOW, 1))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_108(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK((HIGH - MIN(HIGH, 2)))^RANK(CORR((VWAP), (MEAN(VOLUME,120)), 6))) * -1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_109(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(HIGH-LOW,10,2)/SMA(SMA(HIGH-LOW,10,2),10,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_110(code, end_date=None, fq="pre"):
    """
    公式:
       SUM(MAX(0,HIGH-DELAY(CLOSE,1)),20)/SUM(MAX(0,DELAY(CLOSE,1)-LOW),20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_111(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(VOL*((CLOSE-LOW)-(HIGH-CLOSE))/(HIGH-LOW),11,2)-SMA(VOL*((CLOSE-LOW)-(HIGH-CLOSE))/(HIGH-L OW),4,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_112(code, end_date=None, fq="pre"):
    """
    公式:
       (SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12)-SUM((CLOSE-DELAY(CLOSE,1)<0?ABS(CLOS E-DELAY(CLOSE,1)):0),12))/(SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12)+SUM((CLOSE-DE LAY(CLOSE,1)<0?ABS(CLOSE-DELAY(CLOSE,1)):0),12))*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_113(code, end_date=None, fq="pre"):
    """
    公式:
       (-1 * ((RANK((SUM(DELAY(CLOSE, 5), 20) / 20)) * CORR(CLOSE, VOLUME, 2)) * RANK(CORR(SUM(CLOSE, 5),SUM(CLOSE, 20), 2))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_114(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK(DELAY(((HIGH - LOW) / (SUM(CLOSE, 5) / 5)), 2)) * RANK(RANK(VOLUME))) / (((HIGH - LOW) / (SUM(CLOSE, 5) / 5)) / (VWAP - CLOSE)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_115(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(CORR(((HIGH * 0.9) + (CLOSE * 0.1)), MEAN(VOLUME,30), 10))^RANK(CORR(TSRANK(((HIGH + LOW) /  2), 4), TSRANK(VOLUME, 10), 7)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_116(code, end_date=None, fq="pre"):
    """
    公式:
       REGBETA(CLOSE,SEQUENCE,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_117(code, end_date=None, fq="pre"):
    """
    公式:
       ((TSRANK(VOLUME,32)*(1-TSRANK(((CLOSE+HIGH)-LOW),16)))*(1-TSRANK(RET,32)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_118(code, end_date=None, fq="pre"):
    """
    公式:
       SUM(HIGH-OPEN,20)/SUM(OPEN-LOW,20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_119(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(DECAYLINEAR(CORR(VWAP,SUM(MEAN(VOLUME,5),26),5),7))-RANK(DECAYLINEAR(TSRANK(MIN(CORR(RANK(OPEN),RANK(MEAN(VOLUME,15)),21),9),7),8)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_120(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK((VWAP-CLOSE))/RANK((VWAP+CLOSE)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_121(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK((VWAP-MIN(VWAP,12)))^TSRANK(CORR(TSRANK(VWAP,20),TSRANK(MEAN(VOLUME,60),2),18),3))*-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_122(code, end_date=None, fq="pre"):
    """
    公式:
       (SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2)-DELAY(SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2),1))/DELAY(SM A(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2),1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_123(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK(CORR(SUM(((HIGH+LOW)/2),20),SUM(MEAN(VOLUME,60),20),9))<RANK(CORR(LOW,VOLUME,6)))*-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_124(code, end_date=None, fq="pre"):
    """
    公式:
       (CLOSE-VWAP)/DECAYLINEAR(RANK(TSMAX(CLOSE,30)),2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_125(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(DECAYLINEAR(CORR((VWAP),MEAN(VOLUME,80),17),20))/RANK(DECAYLINEAR(DELTA(((CLOSE*0.5)+ (VWAP*0.5)),3),16)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_126(code, end_date=None, fq="pre"):
    """
    公式:
       (CLOSE+HIGH+LOW)/3
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_127(code, end_date=None, fq="pre"):
    """
    公式:
       (MEAN((100*(CLOSE-MAX(CLOSE,12))/(MAX(CLOSE,12)))^2))^(1/2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_128(code, end_date=None, fq="pre"):
    """
    公式:
       100-(100/(1+SUM(((HIGH+LOW+CLOSE)/3>DELAY((HIGH+LOW+CLOSE)/3,1)?(HIGH+LOW+CLOSE)/3*VOLUM E:0),14)/SUM(((HIGH+LOW+CLOSE)/3<DELAY((HIGH+LOW+CLOSE)/3,1)?(HIGH+LOW+CLOSE)/3*VOLUME:0), 14)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_129(code, end_date=None, fq="pre"):
    """
    公式:
       SUM((CLOSE-DELAY(CLOSE,1)<0?ABS(CLOSE-DELAY(CLOSE,1)):0),12)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_130(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(DECAYLINEAR(CORR(((HIGH+LOW)/2), MEAN(VOLUME,40),9),10))/RANK(DECAYLINEAR(CORR(RANK(VWAP),RANK(VOLUME),7),3)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_131(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(DELAT(VWAP, 1))^TSRANK(CORR(CLOSE,MEAN(VOLUME,50), 18), 18))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_132(code, end_date=None, fq="pre"):
    """
    公式:
       MEAN(AMOUNT,20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_133(code, end_date=None, fq="pre"):
    """
    公式:
       ((20-HIGHDAY(HIGH,20))/20)*100-((20-LOWDAY(LOW,20))/20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_134(code, end_date=None, fq="pre"):
    """
    公式:
       (CLOSE-DELAY(CLOSE,12))/DELAY(CLOSE,12)*VOLUME
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_135(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(DELAY(CLOSE/DELAY(CLOSE,20),1),20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_136(code, end_date=None, fq="pre"):
    """
    公式:
       ((-1*RANK(DELTA(RET,3)))*CORR(OPEN,VOLUME,10))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_137(code, end_date=None, fq="pre"):
    """
    公式:
       16*(CLOSE-DELAY(CLOSE,1)+(CLOSE-OPEN)/2+DELAY(CLOSE,1)-DELAY(OPEN,1))/((ABS(HIGH-DELAY(CLOSE,1))>ABS(LOW-DELAY(CLOSE,1)) &ABS(HIGH-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))?ABS(HIGH-DELAY(CLOSE,1))+ABS(LOW-DELAY(CLOS E,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:(ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(LOW,1))&ABS(LOW-DELAY(CLOSE,1))>ABS(HIGH-DELAY(CLOSE,1))?ABS(LOW-DELAY(CLOSE,1))+ABS(HIGH-DELAY(CLO SE,1))/2+ABS(DELAY(CLOSE,1)-DELAY(OPEN,1))/4:ABS(HIGH-DELAY(LOW,1))+ABS(DELAY(CLOSE,1)-DELAY(OP EN,1))/4)))*MAX(ABS(HIGH-DELAY(CLOSE,1)),ABS(LOW-DELAY(CLOSE,1)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_138(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK(DECAYLINEAR(DELTA((((LOW*0.7)+(VWAP*0.3))),3),20))-TSRANK(DECAYLINEAR(TSRANK(CORR(TSRANK(LOW,8),TSRANK(MEAN(VOLUME,60),17),5),19),16),7))*-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_139(code, end_date=None, fq="pre"):
    """
    公式:
       (-1 * CORR(OPEN, VOLUME, 10))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_140(code, end_date=None, fq="pre"):
    """
    公式:
       MIN(RANK(DECAYLINEAR(((RANK(OPEN)+RANK(LOW))-(RANK(HIGH)+RANK(CLOSE))),8)),TSRANK(DECAYLINEAR(CORR(TSRANK(CLOSE,8),TSRANK(MEAN(VOLUME,60), 20), 8), 7), 3))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_141(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(CORR(RANK(HIGH),RANK(MEAN(VOLUME,15)),9))*-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_142(code, end_date=None, fq="pre"):
    """
    公式:
       (((-1*RANK(TSRANK(CLOSE,10)))*RANK(DELTA(DELTA(CLOSE,1),1)))*RANK(TSRANK((VOLUME/MEAN(VOLUME,20)), 5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_143(code, end_date=None, fq="pre"):
    """
    公式:
       CLOSE>DELAY(CLOSE,1)?(CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)*SELF:SELF
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_144(code, end_date=None, fq="pre"):
    """
    公式:
       SUMIF(ABS(CLOSE/DELAY(CLOSE,1)-1)/AMOUNT,20,CLOSE<DELAY(CLOSE,1))/COUNT(CLOSE<DELAY(CLOSE, 1),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_145(code, end_date=None, fq="pre"):
    """
    公式:
       (MEAN(VOLUME,9)-MEAN(VOLUME,26))/MEAN(VOLUME,12)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_146(code, end_date=None, fq="pre"):
    """
    公式:
       MEAN((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1),61,2),20)*(( CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1),61,2))/SMA(((CLOS E-DELAY(CLOSE,1))/DELAY(CLOSE,1)-((CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)-SMA((CLOSE-DELAY(CLOSE, 1))/DELAY(CLOSE,1),61,2)))^2,60);
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_147(code, end_date=None, fq="pre"):
    """
    公式:
       REGBETA(MEAN(CLOSE,12),SEQUENCE(12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_148(code, end_date=None, fq="pre"):
    """
    公式:
       ((RANK(CORR((OPEN),SUM(MEAN(VOLUME,60),9),6))<RANK((OPEN-TSMIN(OPEN,14))))*-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_149(code,benchmark='000300.XSHG',end_date=None, fq="pre"):
    """
    公式:
       REGBETA(FILTER(CLOSE/DELAY(CLOSE,1)-1,BANCHMARKINDEXCLOSE<DELAY(BANCHMARKINDEXCLOSE,1)),FILTER(BANCHMARKINDEXCLOSE/DELAY(BANCHMARKINDEXCLOSE,1)-1,BANCHMARKINDEXCLOSE<DELAY(BANCHMARKINDEXCLOSE,1)),252)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_150(code, end_date=None, fq="pre"):
    """
    公式:
       (CLOSE+HIGH+LOW)/3*VOLUME
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_151(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(CLOSE-DELAY(CLOSE,20),20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_152(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(MEAN(DELAY(SMA(DELAY(CLOSE/DELAY(CLOSE,9),1),9,1),1),12)-MEAN(DELAY(SMA(DELAY(CLOSE/DELAY(CLOSE,9),1),9,1),1),26),9,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_153(code, end_date=None, fq="pre"):
    """
    公式:
       (MEAN(CLOSE,3)+MEAN(CLOSE,6)+MEAN(CLOSE,12)+MEAN(CLOSE,24))/4
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_154(code, end_date=None, fq="pre"):
    """
    公式:
       (((VWAP-MIN(VWAP,16)))<(CORR(VWAP,MEAN(VOLUME,180),18)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_155(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(VOLUME,13,2)-SMA(VOLUME,27,2)-SMA(SMA(VOLUME,13,2)-SMA(VOLUME,27,2),10,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_156(code, end_date=None, fq="pre"):
    """
    公式:
       (MAX(RANK(DECAYLINEAR(DELTA(VWAP,5),3)),RANK(DECAYLINEAR(((DELTA(((OPEN*0.15)+(LOW*0.85)),2)/((OPEN*0.15)+(LOW*0.85)))*-1),3)))*-1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_157(code, end_date=None, fq="pre"):
    """
    公式:
       (MIN(PROD(RANK(RANK(LOG(SUM(TSMIN(RANK(RANK((-1*RANK(DELTA((CLOSE-1),5))))),2),1)))),1), 5) +TSRANK(DELAY((-1*RET),6),5))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_158(code, end_date=None, fq="pre"):
    """
    公式:
       ((HIGH-SMA(CLOSE,15,2))-(LOW-SMA(CLOSE,15,2)))/CLOSE
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_159(code, end_date=None, fq="pre"):
    """
    公式:
       ((CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),6))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,DELAY(CLOSE,1)),6)*12*24+(CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),12))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,DELAY(CL OSE,1)),12)*6*24+(CLOSE-SUM(MIN(LOW,DELAY(CLOSE,1)),24))/SUM(MAX(HGIH,DELAY(CLOSE,1))-MIN(LOW,D ELAY(CLOSE,1)),24)*6*24)*100/(6*12+6*24+12*24)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_160(code, end_date=None, fq="pre"):
    """
    公式:
       SMA((CLOSE<=DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_161(code, end_date=None, fq="pre"):
    """
    公式:
       MEAN(MAX(MAX((HIGH-LOW),ABS(DELAY(CLOSE,1)-HIGH)),ABS(DELAY(CLOSE,1)-LOW)),12)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_162(code, end_date=None, fq="pre"):
    """
    公式:
       (SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100-MIN(SMA(MAX(CLOS E-DELAY(CLOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12))/(MAX(SMA(MAX(CLOSE-DELAY(C LOSE,1),0),12,1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12)-MIN(SMA(MAX(CLOSE-DELAY(CLOSE,1),0),12, 1)/SMA(ABS(CLOSE-DELAY(CLOSE,1)),12,1)*100,12))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_163(code, end_date=None, fq="pre"):
    """
    公式:
       RANK(((((-1 * RET) * MEAN(VOLUME,20)) * VWAP) * (HIGH - CLOSE)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_164(code, end_date=None, fq="pre"):
    """
    公式:
       SMA((((CLOSE>DELAY(CLOSE,1))?1/(CLOSE-DELAY(CLOSE,1)):1)-MIN(((CLOSE>DELAY(CLOSE,1))?1/(CLOSE-D ELAY(CLOSE,1)):1),12))/(HIGH-LOW)*100,13,2)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_165(code, end_date=None, fq="pre"):
    """
    公式:
       MAX(SUMAC(CLOSE-MEAN(CLOSE,48)))-MIN(SUMAC(CLOSE-MEAN(CLOSE,48)))/STD(CLOSE,48)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_166(code, end_date=None, fq="pre"):
    """
    公式:
       -20*(20-1)^1.5*SUM(CLOSE/DELAY(CLOSE,1)-1-MEAN(CLOSE/DELAY(CLOSE,1)-1,20),20)/((20-1)*(20-2)(SUM((CLOSE/DELA Y(CLOSE,1),20)^2,20))^1.5)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_167(code, end_date=None, fq="pre"):
    """
    公式:
       SUM((CLOSE-DELAY(CLOSE,1)>0?CLOSE-DELAY(CLOSE,1):0),12)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_168(code, end_date=None, fq="pre"):
    """
    公式:
       (-1*VOLUME/MEAN(VOLUME,20))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_169(code, end_date=None, fq="pre"):
    """
    公式:
       SMA(MEAN(DELAY(SMA(CLOSE-DELAY(CLOSE,1),9,1),1),12)-MEAN(DELAY(SMA(CLOSE-DELAY(CLOSE,1),9,1),1), 26),10,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_170(code, end_date=None, fq="pre"):
    """
    公式:
       ((((RANK((1/CLOSE))*VOLUME)/MEAN(VOLUME,20))*((HIGH*RANK((HIGH-CLOSE)))/(SUM(HIGH, 5)/5)))-RANK((VWAP-DELAY(VWAP, 5))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_171(code, end_date=None, fq="pre"):
    """
    公式:
       ((-1 * ((LOW - CLOSE) * (OPEN^5))) / ((CLOSE - HIGH) * (CLOSE^5)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_172(code, end_date=None, fq="pre"):
    """
    公式:
       MEAN(ABS(SUM((LD>0&LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0&HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0 & LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0 & HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_173(code, end_date=None, fq="pre"):
    """
    公式:
       3*SMA(CLOSE,13,2)-2*SMA(SMA(CLOSE,13,2),13,2)+SMA(SMA(SMA(LOG(CLOSE),13,2),13,2),13,2);
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_174(code, end_date=None, fq="pre"):
    """
    公式:
       SMA((CLOSE>DELAY(CLOSE,1)?STD(CLOSE,20):0),20,1)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_175(code, end_date=None, fq="pre"):
    """
    公式:
       MEAN(MAX(MAX((HIGH-LOW),ABS(DELAY(CLOSE,1)-HIGH)),ABS(DELAY(CLOSE,1)-LOW)),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_176(code, end_date=None, fq="pre"):
    """
    公式:
       CORR(RANK(((CLOSE-TSMIN(LOW, 12))/(TSMAX(HIGH, 12)-TSMIN(LOW,12)))), RANK(VOLUME), 6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_177(code, end_date=None, fq="pre"):
    """
    公式:
       ((20-HIGHDAY(HIGH,20))/20)*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_178(code, end_date=None, fq="pre"):
    """
    公式:
       (CLOSE-DELAY(CLOSE,1))/DELAY(CLOSE,1)*VOLUME
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_179(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(CORR(VWAP,VOLUME,4))*RANK(CORR(RANK(LOW), RANK(MEAN(VOLUME,50)), 12)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_180(code, end_date=None, fq="pre"):
    """
    公式:
       ((MEAN(VOLUME,20)<VOLUME)?((-1*TSRANK(ABS(DELTA(CLOSE,7)),60)) * SIGN(DELTA(CLOSE,7)):(-1*VOLUME)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_181(code,benchmark='000300.XSHG',end_date=None, fq="pre"):
    """
    公式:
       SUM(((CLOSE/DELAY(CLOSE,1)-1)-MEAN((CLOSE/DELAY(CLOSE,1)-1),20))-(BANCHMARKINDEXCLOSE-MEAN(BANCHMARKINDEXCLOSE,20))^2,20)/SUM((BANCHMARKINDEXCLOSE-MEAN(BANCHMARKINDEXCLOSE,20))^3)
    Inputs:
        code: 股票池
        benchmark: 基准指数，默认为沪深300
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_182(code, benchmark='000300.XSHG', end_date=None, fq="pre"):
    """
    公式:
       COUNT((CLOSE>OPEN&BANCHMARKINDEXCLOSE>BANCHMARKINDEXOPEN)OR(CLOSE<OPEN&BANCHMARKINDEXCLOSE<BANCHMARKINDEXOPEN),20)/20
    Inputs:
        code: 股票池
        benchmark: 基准指数，默认为沪深300
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_183(code, end_date=None, fq="pre"):
    """
    公式:
       MAX(SUMAC(CLOSE-MEAN(CLOSE,24)))-MIN(SUMAC(CLOSE-MEAN(CLOSE,24)))/STD(CLOSE,24)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    raise Exception("该因子未实现")


@assert_auth
def alpha_184(code, end_date=None, fq="pre"):
    """
    公式:
       (RANK(CORR(DELAY((OPEN - CLOSE), 1), CLOSE, 200)) + RANK((OPEN - CLOSE)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_185(code, end_date=None, fq="pre"):
    """
    公式:
       RANK((-1 * ((1 - (OPEN / CLOSE))^2)))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_186(code, end_date=None, fq="pre"):
    """
    公式:
       (MEAN(ABS(SUM((LD>0&LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0&HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0 & LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0 & HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6)+DELAY(MEAN(ABS(SUM((LD>0   & LD>HD)?LD:0,14)*100/SUM(TR,14)-SUM((HD>0 & HD>LD)?HD:0,14)*100/SUM(TR,14))/(SUM((LD>0 & LD>HD)?LD:0,14)*100/SUM(TR,14)+SUM((HD>0 & HD>LD)?HD:0,14)*100/SUM(TR,14))*100,6),6))/2
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_187(code, end_date=None, fq="pre"):
    """
    公式:
       SUM((OPEN<=DELAY(OPEN,1)?0:MAX((HIGH-OPEN),(OPEN-DELAY(OPEN,1)))),20)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_188(code, end_date=None, fq="pre"):
    """
    公式:
       ((HIGH-LOW–SMA(HIGH-LOW,11,2))/SMA(HIGH-LOW,11,2))*100
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())

@assert_auth
def alpha_189(code, end_date=None, fq="pre"):
    """
    公式:
       MEAN(ABS(CLOSE-MEAN(CLOSE,6)),6)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_190(code, end_date=None, fq="pre"):
    """
    公式:
       LOG((COUNT(CLOSE/DELAY(CLOSE)-1>((CLOSE/DELAY(CLOSE,19))^(1/20)-1),20)-1)*(SUMIF(((CLOSE/DELAY(C LOSE)-1-(CLOSE/DELAY(CLOSE,19))^(1/20)-1))^2,20,CLOSE/DELAY(CLOSE)-1<(CLOSE/DELAY(CLOSE,19))^(1/20)- 1))/((COUNT((CLOSE/DELAY(CLOSE)-1<(CLOSE/DELAY(CLOSE,19))^(1/20)-1),20))*(SUMIF((CLOSE/DELAY(CLOS E)-1-((CLOSE/DELAY(CLOSE,19))^(1/20)-1))^2,20,CLOSE/DELAY(CLOSE)-1>(CLOSE/DELAY(CLOSE,19))^(1/20)-1))))
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())


@assert_auth
def alpha_191(code, end_date=None, fq="pre"):
    """
    公式:
       ((CORR(MEAN(VOLUME,20),LOW,5)+((HIGH+LOW)/2))-CLOSE)
    Inputs:
        code: 股票池
        end_date: 查询日期
    Outputs:
        因子的值
    """
    end_date = to_date_str(end_date)
    func_name = sys._getframe().f_code.co_name
    return JQDataClient.instance().get_alpha_191(**locals())
