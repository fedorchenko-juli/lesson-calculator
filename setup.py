"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['calculator.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    author='Yuliia Fedorchenko',
    author_email='julia.fdrchnk@gmail.com',
    setup_requires=['py2app', 'python-dateutil==2.8.2'],
)
