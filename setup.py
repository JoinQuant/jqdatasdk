#!/usr/bin/env python
# coding=utf-8
import re
import sys
from os.path import dirname, join

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements


from setuptools import (
    find_packages,
    setup,
)


with open(join(dirname(__file__), 'jqdatasdk', '__init__.py'), 'r') as f:
    version = re.match(r".*__version__ = \"(.*?)\"", f.read(), re.S).group(1)

with open(join(dirname(__file__), 'README.md'), 'rb') as f:
    long_description = f.read().decode('utf-8')

requirements = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)]


setup(
    name="jqdatasdk",
    version=version,
    description="jqdatasdk<easy utility for getting financial market data of China>",
    packages=["jqdatasdk"],
    author="JoinQuant",
    author_email="xlx@joinquant.com",
    maintainer="tech_data",
    maintainer_email="tech_data@joinquant.com",
    license='Apache License v2',
    package_data={'': ['*.*']},
    url="https://www.joinquant.com/data",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
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
