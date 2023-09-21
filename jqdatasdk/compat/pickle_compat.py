# -*- coding: utf-8 -*-

import sys
import copy
from inspect import isclass
try:
    import cPickle as pickle
except ImportError:
    import pickle

import numpy as np
from pandas import Index
from pandas.compat.pickle_compat import pkl, Unpickler, load as _load

try:
    from pandas._libs.arrays import NDArrayBacked
except ImportError:
    NDArrayBacked = None
try:
    from pandas._libs.tslibs import BaseOffset
except ImportError:
    BaseOffset = None
try:
    from pandas.core.arrays import PeriodArray
except ImportError:
    PeriodArray = None
try:
    from pandas.core.arrays import DatetimeArray
except ImportError:
    DatetimeArray = None
try:
    from pandas.core.arrays import TimedeltaArray
except ImportError:
    TimedeltaArray = None
try:
    from pandas.core.internals import BlockManager
except ImportError:
    try:
        from pandas.core.internals.managers import BlockManager
    except ImportError:
        BlockManager = None


def load_reduce(self):
    stack = self.stack
    args = stack.pop()
    func = stack[-1]

    try:
        stack[-1] = func(*args)
        return
    except Exception as err:
        msg = "_reconstruct: First argument must be a sub-type of ndarray"

        if msg in str(err):
            try:
                cls = args[0]
                stack[-1] = object.__new__(cls)
                return
            except TypeError:
                pass

        if args and isclass(args[0]) and issubclass(args[0], BaseOffset):
            # TypeError: object.__new__(Day) is not safe, use Day.__new__()
            try:
                cls = args[0]
                stack[-1] = cls.__new__(*args)
                return
            except TypeError:
                pass

        if args and isclass(args[0]) and issubclass(args[0], PeriodArray):
            try:
                cls = args[0]
                stack[-1] = NDArrayBacked.__new__(*args)
                return
            except TypeError:
                pass

        # try to re-encode the arguments
        if getattr(self, "encoding", None) is not None:
            args = tuple(
                arg.encode(self.encoding) if isinstance(arg, str) else arg
                for arg in args
            )
            try:
                stack[-1] = func(*args)
                return
            except TypeError:
                pass

        # unknown exception, re-raise
        if getattr(self, "is_verbose", None):
            print(sys.exc_info())
            print(func, args)
        raise


# If classes are moved, provide compat here.
_class_locations_map = {
    ("pandas.core.sparse.array", "SparseArray"): ("pandas.core.arrays", "SparseArray"),
    # 15477
    ("pandas.core.base", "FrozenNDArray"): ("numpy", "ndarray"),
    ("pandas.core.indexes.frozen", "FrozenNDArray"): ("numpy", "ndarray"),
    ("pandas.core.base", "FrozenList"): ("pandas.core.indexes.frozen", "FrozenList"),
    # 10890
    ("pandas.core.series", "TimeSeries"): ("pandas.core.series", "Series"),
    ("pandas.sparse.series", "SparseTimeSeries"): (
        "pandas.core.sparse.series",
        "SparseSeries",
    ),
    # 12588, extensions moving
    ("pandas._sparse", "BlockIndex"): ("pandas._libs.sparse", "BlockIndex"),
    ("pandas.tslib", "Timestamp"): ("pandas._libs.tslib", "Timestamp"),
    # 18543 moving period
    ("pandas._period", "Period"): ("pandas._libs.tslibs.period", "Period"),
    ("pandas._libs.period", "Period"): ("pandas._libs.tslibs.period", "Period"),
    # 18014 moved __nat_unpickle from _libs.tslib-->_libs.tslibs.nattype
    ("pandas.tslib", "__nat_unpickle"): (
        "pandas._libs.tslibs.nattype",
        "__nat_unpickle",
    ),
    ("pandas._libs.tslib", "__nat_unpickle"): (
        "pandas._libs.tslibs.nattype",
        "__nat_unpickle",
    ),
    # 15998 top-level dirs moving
    ("pandas.sparse.array", "SparseArray"): (
        "pandas.core.arrays.sparse",
        "SparseArray",
    ),
    ("pandas.indexes.base", "_new_Index"): ("pandas.core.indexes.base", "_new_Index"),
    ("pandas.indexes.base", "Index"): ("pandas.core.indexes.base", "Index"),
    ("pandas.indexes.numeric", "Int64Index"): (
        "pandas.core.indexes.base",
        "Index",  # updated in 50775
    ),
    ("pandas.indexes.range", "RangeIndex"): ("pandas.core.indexes.range", "RangeIndex"),
    ("pandas.indexes.multi", "MultiIndex"): ("pandas.core.indexes.multi", "MultiIndex"),
    ("pandas.tseries.index", "_new_DatetimeIndex"): (
        "pandas.core.indexes.datetimes",
        "_new_DatetimeIndex",
    ),
    ("pandas.tseries.index", "DatetimeIndex"): (
        "pandas.core.indexes.datetimes",
        "DatetimeIndex",
    ),
    ("pandas.tseries.period", "PeriodIndex"): (
        "pandas.core.indexes.period",
        "PeriodIndex",
    ),
    # 19269, arrays moving
    ("pandas.core.categorical", "Categorical"): ("pandas.core.arrays", "Categorical"),
    # 19939, add timedeltaindex, float64index compat from 15998 move
    ("pandas.tseries.tdi", "TimedeltaIndex"): (
        "pandas.core.indexes.timedeltas",
        "TimedeltaIndex",
    ),
    ("pandas.indexes.numeric", "Float64Index"): (
        "pandas.core.indexes.base",
        "Index",  # updated in 50775
    ),
    # 50775, remove Int64Index, UInt64Index & Float64Index from codabase
    ("pandas.core.indexes.numeric", "Int64Index"): (
        "pandas.core.indexes.base",
        "Index",
    ),
    ("pandas.core.indexes.numeric", "UInt64Index"): (
        "pandas.core.indexes.base",
        "Index",
    ),
    ("pandas.core.arrays.sparse.dtype", "SparseDtype"): (
        "pandas.core.dtypes.dtypes",
        "SparseDtype",
    ),

    # add by Huayong Kuang
    ("pandas._libs.tslib", "Timestamp"): ("pandas.tslib", "Timestamp"),
    ("pandas._libs.tslibs.timestamps", "Timestamp"): (
        "pandas.tslib",
        "Timestamp"
    ),
    ('pandas.core.internals.managers', 'BlockManager'): (
        "pandas.core.internals",
        "BlockManager",
    ),
    ('pandas.core.indexes.base', '_new_Index'): (
        "pandas.core.index",
        "_new_Index",
    ),
    ('pandas.core.indexes.base', 'Index'): ("pandas", "Index"),
    ('pandas.core.indexes.numeric', 'Float64Index'): ("pandas", "Index"),
    ('pandas.core.indexes.datetimes', '_new_DatetimeIndex'): (
        "pandas.tseries.index",
        "_new_DatetimeIndex",
    ),
    ('pandas.core.indexes.datetimes', 'DatetimeIndex'):  (
        "pandas",
        "DatetimeIndex",
    ),
}


class Unpickler2(Unpickler):

    def find_class(self, module, name, *args, **kwargs):
        key = (module, name)
        module, name = _class_locations_map.get(key, key)
        return Unpickler.find_class(self, module, name, *args, **kwargs)


Unpickler2.dispatch = copy.copy(Unpickler2.dispatch)
Unpickler2.dispatch[pkl.REDUCE[0]] = load_reduce


def load_newobj(self):
    args = self.stack.pop()
    cls = self.stack[-1]

    # compat
    if issubclass(cls, Index):
        obj = object.__new__(cls)
    elif issubclass(cls, DatetimeArray) and not args:
        arr = np.array([], dtype="M8[ns]")
        obj = cls.__new__(cls, arr, arr.dtype)
    elif issubclass(cls, TimedeltaArray) and not args:
        arr = np.array([], dtype="m8[ns]")
        obj = cls.__new__(cls, arr, arr.dtype)
    elif cls is BlockManager and not args:
        obj = cls.__new__(cls, (), [], False)
    else:
        obj = cls.__new__(cls, *args)

    self.stack[-1] = obj


Unpickler2.dispatch[pkl.NEWOBJ[0]] = load_newobj


def load_newobj_ex(self):
    kwargs = self.stack.pop()
    args = self.stack.pop()
    cls = self.stack.pop()

    # compat
    if issubclass(cls, Index):
        obj = object.__new__(cls)
    else:
        obj = cls.__new__(cls, *args, **kwargs)
    self.append(obj)


try:
    Unpickler2.dispatch[pkl.NEWOBJ_EX[0]] = load_newobj_ex
except (AttributeError, KeyError):
    pass


def load(fh, encoding, is_verbose=True):
    """
    Load a pickle, with a provided encoding,

    Parameters
    ----------
    fh : a filelike object
    encoding : an optional encoding
    is_verbose : show exception output
    """
    try:
        if encoding is not None:
            return pickle.load(fh)
        else:
            return pickle.load(fh, encoding=encoding)
    except Exception:
        try:
            fh.seek(0)
            return _load(fh, encoding=encoding)
        except Exception as ex:
            try:
                fh.seek(0)
                if encoding is not None:
                    up = Unpickler2(fh, encoding=encoding)
                else:
                    up = Unpickler2(fh)
                up.is_verbose = is_verbose

                return up.load()
            except Exception:
                raise ex
