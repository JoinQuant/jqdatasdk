# -*- coding: utf-8 -*-

import pandas as pd

# pandas 版本 (major, minor)
try:
    PANDAS_VERSION = tuple(int(x) for x in pd.__version__.split('.')[:2])
except Exception:
    PANDAS_VERSION = (0, 0)


def pd_astype(obj, dtypes, copy=False, **kwargs):
    """
    兼容不同版本 pandas 的 astype 调用

    pandas 3.0+ 废弃了 copy 参数（引入 Copy-on-Write 机制），
    此时 copy 参数会被忽略

    Parameters
    ----------
    obj : DataFrame, Series or Panel
    dtypes : dict or dtype
    copy : bool, default False
        是否复制数据，pandas 3.0+ 中此参数被忽略
    **kwargs
        传递给 astype 的其他参数，如 errors 等

    Returns
    -------
    DataFrame, Series or Panel
    """
    if PANDAS_VERSION >= (3, 0):
        return obj.astype(dtypes, **kwargs)
    else:
        return obj.astype(dtypes, copy=copy, **kwargs)
