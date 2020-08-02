#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# pysynscan
# Copyright (c) July 2020 Nacho Mas

from setuptools import setup, find_packages

# Get the long description from the relevant file
with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='synscan',
    version='0.0.1',
    description=u"Pure python3 skywatcher synscan protocol",
    long_description=long_description,
    classifiers=[],
    keywords=['robotic','telescope','skywatcher','synscan'],
    author=u"Nacho Mas",
    author_email='mas.ignacio@gmail.com',
    url='https://github.com/nachoplus/pysynscan',
    license='GPL3',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['click'],
    extras_require={
        'test': ['pytest'],
    },
    package_data={
        '': ['config.ini', 'config.ini.spec'],
    },
    entry_points="""
      [console_scripts]
      synscanGoto=synscan.scripts.cli:goto
      synscanTrack=synscan.scripts.cli:track
      """)