# coding: utf-8

import os
import sys
import logging
from importlib import import_module


def pytest_sessionstart(session):
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    sys.path.insert(0, proj_dir)

    jqdatasdk = import_module("jqdatasdk")
    client = jqdatasdk.JQDataClient.instance()
    client.ensure_auth()
    assert jqdatasdk.is_auth()


def pytest_sessionfinish(session, exitstatus):
    import_module("jqdatasdk").logout()
    logging.info("test session finish, exit status: %s", exitstatus)


def pytest_collection_modifyitems(items):
    for item in import_module("copy").copy(items):
        if item.name == 'test_network_speed':
            items.remove(item)
