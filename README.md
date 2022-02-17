[![img](https://raw.githubusercontent.com/JoinQuant/jqdatasdk/master/logo.png)](https://raw.githubusercontent.com/JoinQuant/jqdatasdk/master/logo.png)

## 公司介绍

**JoinQuant 聚宽，专业量化投研平台、技术驱动的平台型资管。**

办公地点位于北上广深、西安等多个城市，2015年5月成立，目前已在量化领域深耕6年多。早期做量化投研交易系统起家，积淀了深厚的系统、交易、数据、算法、风控等多方面经验，并获得众多头部券商认可。平台拥有40万用户的量化优秀人才储备库，活跃的量化学习交流社区、自研的量化系列课程获得国内外众多一线高校青睐。

目前聚宽包含4大业务线：平台服务、数据服务、算法服务、量化基金。四大业务相辅相成，基于聚宽量化平台积累的用户、技术、市场优势，以量化基金和算法服务进行商业变现。

·  聚宽量化投研平台，服务超40万+量化投研用户
·  聚宽算法，服务于券商客户，交易资产超过50亿
·  量化数据JQData，服务国内超过4500家量化机构
·  聚宽量化基金，当前资产管理规模达110+亿

## 产品介绍

### JQData是什么？

JQData是聚宽数据团队专门为金融机构、学术研究和量化研究者们提供的本地量化金融数据服务。使用JQData，可快速查看和计算金融数据，无障碍解决本地、Web、金融终端调用数据的需求。历经6年沉淀，40万宽客及数千家机构投研交易验证。

使用上，JQData适用Windows、Mac、Linux多种操作系统，支持python2、python3（更多语言详情咨询管理员）。数据通过简洁的API方式提供，pip即可直接安装使用，挣脱使用束缚，实现更多场景。只需三行代码，即可随取随用~

### JQData提供什么数据？

JQData提供多个市场数据，详情可查看官网 [https://www.joinquant.com/data](https://www.joinquant.com/data)，内含JQData包含的数据接口和详细的更新时间。

在此基础上，我们提供不同粒度的数据供您使用，包括日线、分钟线、tick级的行情数据，极大地满足您的各项需求。

### 为什么选择JQData？

**本地使用：** JQData避免了各个量化平台的限制，适用于Windows，Mac，Linux多种操作系统，用户只需三行Python代码即可完成本地安装和调用，帮助您实现一整套本地化部署的量化投资研究。（支持Python2和Python3）

**易于量化：** JQData在设计过程中，聚宽团队基于量化行业专业知识及对投研的经验，对数据进行清洗及整理，使数据更能适用量化的研究习惯，并进一步赋能数据在本地投研的可行性及便利性。

**调用方便：** 在JQData里，不同品种同一属性的数据用同一个接口就能获取，例如，使用get_price就能获取所有股票，基金，指数，期货的行情数据，从而大大减少用户的学习成本，代码也更加简洁；与之相反，大部分传统数据商提供的数据分散在不同的数据表中，需要用户自己来回查找。

**JQData精准度介绍：** 截至目前，聚宽自营基金管理规模已达百亿，使用聚宽数据，一创聚宽平台的实盘交易验证，其精准度满足交易需求。聚宽数据团队研发了数据监控系统和多数据源比对系统，通过一整套系统化的机制保证数据的准确性。另外，我们还提供了指定日期参数，杜绝未来数据。

**JQData稳定性介绍：** JQData采用与聚宽官网一致的账户校验系统，登录账号即可使用。提供独立的数据服务，采用负载均衡、高可用服务架构，配备完善的灾备体系，保证业务系统24小时不中断，并支持海量用户同时在线。数据传输方面，采用RPC协议传输，并压缩成特有数据格式，减少传输数据量，更加节省带宽。

## 申请试用

- 申请链接：https://www.joinquant.com/default/index/sdk?utm_campaign=JQData%E7%94%B3%E8%AF%B7&utm_medium=%E7%BD%91%E9%A1%B5&utm_source=%E8%81%9A%E5%AE%BD&gio_link_id=xRxqAjP5
- 申请方法：如实填写资料后提交


## 调用方法

### 安装方法

```shell
# 首次安装
pip install jqdatasdk

# 升级版本
pip install -U jqdatasdk
```

超详细安装指引： https://www.joinquant.com/view/community/detail/cdf86c624992fc86ed51d920ef8c637b

### 使用方法

```python
import jqdatasdk

# 登录认证
jqdatasdk.auth(username, password)

# 获取数据
jqdatasdk.get_price("000001.XSHE", start_date="2017-01-01", end_date="2017-12-31")
```

详细的使用说明文档见：[https://www.joinquant.com/help/api/help?name=JQData](https://www.joinquant.com/help/api/help?name=JQData)

## 机构合作方式

公司机构用户，可以联系官网右下角在线客服或微信号JQData02，进行洽谈。
