#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
__version__ = "0.1.0"
__author__ = "Tyler Bruno"

with open("README.md", "r", encoding="utf-8") as file:
    README = file.read()

with open("requirements.txt", "r") as file:
    INSTALL_REQUIRES = file.read().splitlines()


setup(
    name='pytest-basic-types',
    version=__version__,
    author=__author__,
    author_email='tybruno@cisco.com',
    maintainer='Tyler Bruno',
    maintainer_email='tybruno@cisco.com',
    license='MIT',
    url='https://github.com/tybruno/pytest-basic-types',
    description='Predefined basic types to help with testing.',
    long_description=README,
    py_modules=['pytest_basic_types'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'basic-types = pytest_basic_types',
        ],
    },
)
