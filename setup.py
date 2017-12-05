#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(join(dirname(__file__), *names), encoding=kwargs.get('encoding', 'utf8')).read()


setup(
    name='sample',
    use_scm_version=True,
    license='BSD',
    author='Matt Reynolds',
    author_email='sample@example.com',
    description='sample_description',
    long_description='%s\n%s' % (read('README.rst'), read('CHANGELOG.rst')),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3.6',
    ],
    keywords=[
        'analysis',
    ],
    setup_requires=[
        'setuptools-scm',
    ],
    install_requires=[
        'click',
        'click_log',
        'numpy',
    ],
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'sample = sample.cli:cli',
        ]
    },
)
