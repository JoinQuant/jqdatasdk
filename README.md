### jqdatasdk

>jqdatasdk是提供给用户获取聚宽金融数据的SDK。用户可以在自己搭建的环境中获取聚宽提供的金融数据，除了需要验证之外，其余的功能特性与官网的投资研究模块保持一致。

  ​

#### 安装


```
pip install git+https://github.com/JoinQuant/jqdatasdk.git
```




#### 使用简介

```
import jqdatasdk
jqdatasdk.auth(username, password)
jqdatasdk.get_price("000001.XSHE")
```



#### 支持的接口

> 各API接口的含义及说明见官网：https://www.joinquant.com/api

- get_price

  可查询股票、基金、指数、期货的历史行情数据

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

- get_concept_stocks

  查询指定概念在指定交易日的成分股

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


- get_mtss

  查询股票、基金的融资融券数据

  ​


- get_future_contracts

  查询期货可交易合约列表

  ​

- get_dominant_future

  查询主力合约对应的标的

  ​

- normalize_code

  归一化证券编码

  ​

- macro.run_query

  查询宏观经济数据，具体数据见官网API https://www.joinquant.com/data/dict/macroData