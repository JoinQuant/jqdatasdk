# -*- coding: utf-8 -*-

__version__ = "1.9.3"


_VersionInfo = __import__("collections").namedtuple(
    "version_info", ["major", "minor", "micro"]
)
version_info = ([int(v) for v in __version__.split('.')[:3]] + [0] * 3)[:3]
version_info = _VersionInfo(*version_info)

version_str = "jqdatasdk version {}, python version {}".format(
    __version__,
    ".".join(str(item) for item in __import__("sys").version_info)
)
