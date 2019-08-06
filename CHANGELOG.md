# 2019-08-06
- get_ticks默认过滤无成交tick
- get_current_tick支持多个标的
- 依赖包pandas版本限制
- crontab 不打印广告信息

# 2019-07-27
- 更新测试用例
- 将API与官网API保持一致

# 2019-07-24
- 增加新接口get_concept

# 2019-07-15
- fix bug: socket.timeout

# 2019-07-05
- try catch兼容Windows平台

# 2019-07-05
- 数据返回直接写入内存, 减少反序列化时间
- alpha因子日期序列化
- thriftpy协议异常, 重新尝试请求

# 2019-06-05
- 添加sup库

# 2019-05-10
- 更新python2环境下run_query不支持中文

# 2019-04-17
- 添加bond库
- 添加db统一查询接口

# 2019-04-16
- 添加超对称数据库`ssymmgit etry`
- 数据库查询默认查询条数改为5000

# 2019-04-11
- thrift改为thrift2
- 添加退出logout函数
- 添加get_all_factor函数

# 2019-03-18
- MANIFEST.in添加md文件

# 2019-03-12
- 添加因子分层效果接口
- 添加通用请求接口
- alpha191接口默认前复权
- 更新import动态生成
- 更新测试方式
- 删除打包文件

# 2019-02-11
- 合并客户端模拟交易分支，支持token认证登陆

# 2018-12-06
- 添加接口
    + 查询程序版本
    + get_bars
    + get_current_tick
    + get_fund_info
    + get_query_count
    + get_industry
    + get_industries
- 新上期权数据
- 数据压缩传输
- 修复已知问题

# 2018-08-15
- 修复get_all_trade_days和官网返回数据不一样的bug
- 因子数据上线
- 股票tick数据上线

# 2018-07-12
- 添加沪深市场每日成交概况数据
- jqdatasdk上线新数据无需更新代码
- 修复get_ticks时间显示的bug
- alpha191因子从数据库读取，优化速度

# 2018-06-28
- 添加了市场通主题数据

# 2018-06-26
- 修改财经数据库的查询方式为finance.run_query(query_object)

# 2018-06-15
- 添加了公司概况和股东股本主题

# 2018-06-06
- 支持pyinstall调用jqdatasdk

# 2018-05-31
- 修复了查询get_fundamentals_continuously的bug

# 2018-05-28
- 修复了测试用例test_ta的bug

# 2018-05-25
- 修复了py3查询龙虎榜字符编码的bug


