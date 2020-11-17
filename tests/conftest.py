# coding: utf-8

import os
import sys
import logging


def pytest_sessionstart(session):
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    sys.path.insert(0, proj_dir)

    import jqdatasdk
    username = os.getenv("JQDATASDK_USERNAME")
    password = os.getenv("JQDATASDK_PASSWORD")
    host = os.getenv("JQDATASDK_HOST")
    port = os.getenv("JQDATASDK_PORT")
    assert username and password
    jqdatasdk.auth(username, password, host, port)
