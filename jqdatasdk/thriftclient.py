# -*- coding: utf-8 -*-
# Copyright (c) JoinQuant Development Team

api_description = """
enum DataType {
    Serial = 1,
    DataFrame = 2,
    Panel = 3
}

struct St_Query_Rsp {
    1:required bool status,
    2:optional string msg,
    5:optional string error
}

struct St_Query_Req {
    1:required string method_name,
    2:required binary params,
}

service JqDataService {
    St_Query_Rsp query(1:St_Query_Req rsp),
    St_Query_Rsp auth(1:string username,
                      2:string password,
                      5:bool compress,
                      8:string mac,
                      10:string version2,
                      11:string pyversion),
    St_Query_Rsp auth_by_token(1: string token)
}
"""

import six
import thriftpy2 as thriftpy
thrift = thriftpy.load_fp(six.StringIO(api_description), "jqdata_thrift")
