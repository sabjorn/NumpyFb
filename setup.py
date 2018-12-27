from distutils.core import setup

setup(
    name='NumpyFb',
    version=open('VERSION').read(),
    packages=['numpyfb',],
    license='MIT License',
    long_description=open('README.md').read(),
)