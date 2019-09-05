# -*- coding: utf-8 -*-

import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)


class ThriftConnectorHook(object):
    def __init__(self, name):
        self.name = name
        self.callbacks = set()

    def register(self, callback, raises=None):
        if isinstance(raises, list):
            raises = tuple(raises)

        self.callbacks.add((callback, raises))

    def send(self, *args, **kwds):
        for (callback, raises) in self.callbacks:
            try:
                callback(*args, **kwds)
            except raises:
                raise
            except Exception as e:
                logger.warning(e, exc_info=True)


before_call = ThriftConnectorHook('before_call')
after_call = ThriftConnectorHook('after_call')
after_get_client_from_pool = ThriftConnectorHook('after_get_client_from_pool')


def api_call_context(pool, client, api_name):
    def deco(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            before_call.send(pool, client, api_name, start)
            ret = None
            try:
                ret = func(*args, **kwargs)
                return ret
            except Exception as e:
                ret = e
                raise
            finally:
                now = time.time()
                client.incr_use_count()
                client.set_latest_use_time(now)
                cost = now - start
                after_call.send(pool, client, api_name, start, cost, ret)
        return wrapper
    return deco


def client_get_hook(func):
    @wraps(func)
    def _(pool, *args, **kwds):
        start = time.time()
        client, exception = None, None
        try:
            client = func(pool, *args, **kwds)
        except BaseException as e:
            exception = e
            raise
        finally:
            cost = time.time() - start
            after_get_client_from_pool.send(
                pool, client, start, cost, exception)
        return client
    return _
