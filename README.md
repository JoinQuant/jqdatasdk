![logo](https://raw.githubusercontent.com/JoinQuant/jqdatasdk/master/logo.png)

### jqdatasdk

>jqdatasdk是提供给用户获取聚宽金融数据的SDK。用户可以在自己搭建的环境中获取聚宽提供的金融数据，除了需要验证之外，其余的功能特性与官网的投资研究模块保持一致。



#### 安装

- 方式一：pip install git+https://github.com/JoinQuant/jqdatasdk.git -i https://mirrors.aliyun.com/pypi/simple/
- 方式二：python setup.py install



#### 升级

```
pip install -U git+https://github.com/JoinQuant/jqdatasdk.git -i https://mirrors.aliyun.com/pypi/simple/
```



#### 使用简介

例如：获取平安银行2017-01-01到2017-12-31的所有日行情数据

```
import jqdatasdk
jqdatasdk.auth(username, password)
jqdatasdk.get_price("000001.XSHE", start_date="2017-01-01", end_date="2017-12-31")
```

结果显示：

```
             open  close   high    low       volume         money
2017-01-03   8.98   9.03   9.05   8.96   46650858.0  4.205952e+08
2017-01-04   9.02   9.03   9.05   9.01   45584521.0  4.115034e+08
2017-01-05   9.04   9.04   9.05   9.02   34936662.0  3.157697e+08
2017-01-06   9.04   9.00   9.04   8.98   36334775.0  3.271764e+08
2017-01-09   9.00   9.02   9.04   8.98   36631757.0  3.299946e+08
2017-01-10   9.02   9.02   9.03   9.01   24454945.0  2.205751e+08
2017-01-11   9.01   9.01   9.04   9.00   30783091.0  2.775532e+08
2017-01-12   9.00   9.02   9.04   9.00   43421325.0  3.918694e+08
2017-01-13   9.01   9.03   9.06   8.99   44059912.0  3.976019e+08
...
```



#### 试用

如果您想试用该数据包接口，请联系我们的运营（微信:jqdata01），添加时请备注jqdatasdk。



#### 支持的接口

> 各API接口的含义及说明见官网：https://www.joinquant.com/api

- get_price

  可查询股票、基金、指数、期货的历史及当前交易日的行情数据

  可指定单位时间长度，如一天、一分钟、五分钟等

  可查询开盘价、收盘价、最高价、最低价、成交量、成交额、涨停、跌停、均价、前收价、是否停牌

  支持不同的复权方式

  ​

- get_trade_days

  查询指定时间范围的交易日

  ​

- get_all_trade_days

  查询所有的交易日

  ​

- get_extras

  查询股票是否是ST

  查询基金的累计净值、单位净值

  查询期货的结算价、持仓量

  ​


- get_index_stocks

  查询指定指数在指定交易日的成分股

  ​

- get_industry_stocks

  查询指定行业在指定交易日的成分股

  ​

- get_industries

  查询行业列表

  ​

- get_concept_stocks

  查询指定概念在指定交易日的成分股

  ​

- get_concepts

  查询概念列表

  ​

- get_all_securities

  查询股票、基金、指数、期货列表

  ​

- get_security_info

  查询单个标的的信息

  ​


- get_money_flow

  查询某只股票的资金流向数据

  ​

- get_fundamentals

  查询财务数据，包含估值表、利润表、现金流量表、资产负债表、银行专项指标、证券专项指标、保险专项指标

  ​

- get_fundamentals_continuously 

  查询多日的财务数据

  ​


- get_mtss

  查询股票、基金的融资融券数据

  ​

- get_billbord_list

  查询股票龙虎榜数据

  ​

- get_locked_shares

  查询股票限售解禁股数据

  ​

- get_margincash_stocks 

  获取融资标的列表

  ​

- get_marginsec_stocks

  获取融券标的列表

  ​


- get_future_contracts

  查询期货可交易合约列表

  ​


- get_dominant_future

  查询主力合约对应的标的

  ​

- get_ticks

  查询股票、期货的tick数据

  ​

- normalize_code

  归一化证券编码

  ​


- macro.run_query

  查询宏观经济数据，具体数据见官网API https://www.joinquant.com/data/dict/macroData

  ​



- alpha101

  查询WorldQuant 101 Alphas 因子数据，具体因子解释见官网API https://www.joinquant.com/data/dict/alpha101

  ​


- alpha191

  查询短周期价量特征 191 Alphas 因子数据，具体因子解释见官网API https://www.joinquant.com/data/dict/alpha191

  ​

- technical_analysis

  技术分析指标，具体因子解释见官网API https://www.joinquant.com/data/dict/technicalanalysis

  ​

- baidu_factor

  查询股票某日百度搜索量数据


- get_factor_values

  获取质量因子、基础因子、情绪因子、成长因子、风险因子、每股因子等数百个因子数据，详细的因子列表请参考https://www.joinquant.com/help/api/help?name=factor_values

