### jqdatasdk

>jqdatasdk是提供给用户获取聚宽金融数据的SDK。用户可以在自己搭建的环境中获取聚宽提供的金融数据，除了需要验证之外，其余的功能特性与官网的投资研究模块保持一致。



#### 权限申请

个人用户如果想使用，请向运营人员申请授权，授权后方可使用。

权限分为三个方面，分别是每天查询条数、可查询的类别和可查询的时间范围。

- 每天查询条数

  查询条数为返回的结果内容的数据，不是查询的次数。如果返回结果为一个list，则查询的条数为该list的长度。

- 可查询的类别

  

- 可查询的时间范围

  ​

#### 安装


```
pip install jqdatasdk
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
- get_trade_days
- get_all_trade_days
- get_extras
- get_index_stocks
- get_industry_stocks
- get_concept_stocks
- get_all_securities
- get_security_info
- get_money_flow
- get_fundamentals
- get_mtss
- get_future_contracts
- get_dominant_future
- normalize_code
- read_file
- write_file
- macro.run_query

