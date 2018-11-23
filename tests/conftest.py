# coding: utf-8
import sys
from os.path import abspath, dirname, join


def pytest_configure(config):
    proj_dir = abspath(join(dirname(abspath(__file__)), '../'))
    sys.path.insert(0, proj_dir)