#!/usr/bin/env python
from distutils.core import setup

setup(
    name='NumpyFb',
    version=open('VERSION').read(),
    packages=['numpyfb',],
    author='Steven A. Bjornson',
    author_email='info@sabjorn.net',
    url='https://github.com/sabjorn/NumpyFb',
    license='MIT License',
    long_description=open('README.md').read(),
)