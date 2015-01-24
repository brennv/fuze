#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import fuze
version = fuze.__version__

setup(
    name='fuze',
    version=version,
    author='',
    author_email='brennanv03@gmail.com',
    packages=[
        'fuze',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['fuze/manage.py'],
)
