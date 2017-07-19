#!/usr/bin/env python3

from setuptools import setup, find_packages
import mira
import mirapie
import os


def extra_dependencies():
    import sys
    ret = []
    if sys.version_info < (2, 7):
        ret.append('argparse')
    return ret


def read(*names):
    values = dict()
    extensions = ['.txt', '.rst']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values

long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

setup(
    name             = 'mirapie',
    version          = mirapie.__version__,
    description      = 'Instant coding answers via the command line',
    long_description = long_description,
    classifiers      = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Documentation",
    ],
    keywords='howdoi help console command line answer',
    author='Diego Di Carlo',
    author_email='diego.dicarlo89@gmail.com',
    maintainer='Diego Di carlo',
    maintainer_email='diego.dicarlo89@gmail.com',
    url='https://github.com/gleitz/howdoi',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'howdoi = howdoi.howdoi:command_line_runner',
        ]
    },
    install_requires=[
        'pyquery',
        'pygments',
        'requests',
        'requests-cache'
    ] + extra_dependencies(),
)
