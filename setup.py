import sys
import os
import subprocess

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='adafruitrpi',
    version='1.0.0',
    description='',
    author='',
    author_email='',
    url='https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code',
    packages=[entry for entry in os.listdir('.') if entry.startswith('Adafruit_')],
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    license='BSD',
)
