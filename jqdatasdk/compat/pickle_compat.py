# -*- coding: utf-8 -*-

import copy
from inspect import isclass
from pandas.compat.pickle_compat import pkl, Unpickler, load as _load


def load_reduce(self):
    stack = self.stack
    args = stack.pop()
    func = stack[-1]

    if len(args) and type(args[0]) is type:
        n = args[0].__name__  # noqa

    try:
        stack[-1] = func(*args)
        return
    except Exception as e:
        msg = "_reconstruct: First argument must be a sub-type of ndarray"

        if msg in str(e):
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


class Unpickler2(Unpickler):
    pass


Unpickler2.dispatch = copy.copy(Unpickler2.dispatch)
Unpickler2.dispatch[pkl.REDUCE[0]] = load_reduce


def load(fh, encoding=None, is_verbose=True):
    try:
        return _load(fh, encoding=encoding)
    except (ValueError, TypeError) as ex:
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
