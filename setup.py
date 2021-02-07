#!/usr/bin/env python
# coding=utf-8

import os
import sys
import re
from setuptools import setup, find_packages


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def get_version():
    scope = {}
    version = '1.0'
    version_file = os.path.join(THIS_FOLDER, "jqdatasdk", "version.py")
    if os.path.exists(version_file):
        with open(version_file) as fp:
            exec(fp.read(), scope)
        version = scope.get('__version__', '1.0')
    return version


def get_long_description():
    with open(os.path.join(THIS_FOLDER, 'README.md'), 'rb') as f:
        long_description = f.read().decode('utf-8')
    return long_description


def _parse_requirement_file(path):
    if not os.path.isfile(path):
        return []
    with open(path) as f:
        requirements = [line.strip() for line in f if line.strip()]
    return requirements


def get_install_requires():
    if sys.version_info.major < 3:
        requirement_file = os.path.join(THIS_FOLDER, "requirements-py2.txt")
    else:
        requirement_file = os.path.join(THIS_FOLDER, "requirements.txt")
    return _parse_requirement_file(requirement_file)


setup(
    name="jqdatasdk",
    version=get_version(),
    description="jqdatasdk<easy utility for getting financial market data of China>",
    packages=find_packages(exclude=("tests", "tests.*")),
    author="JoinQuant",
    author_email="xlx@joinquant.com",
    maintainer="tech_data",
    maintainer_email="tech_data@joinquant.com",
    license='Apache License v2',
    package_data={'': ['*.*']},
    url="https://www.joinquant.com/data",
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    install_requires=get_install_requires(),
    zip_safe=False,
    platforms=["all"],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
