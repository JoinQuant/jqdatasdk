# -*- coding: utf-8 -*-
# Copyright (c) JoinQuant Development Team

from jqdatasdk.client import JQDataClient


class TestClient(object):

    def setup_class(cls):
        cls.client = JQDataClient.instance()

    def teardown_class(cls):
        cls.client.logout()

    def test_set_http_token(self):
        self.client.http_token = None
        self.client.set_http_token()
        assert self.client.http_token
        assert self.client.get_http_token() is self.client.http_token
