# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="linked_list",
    description="Linked list data structure.",
    version='0.1.0',
    author="Zach Rickert, Jeffery Ray Russell",
    author_email="zachrickert@gmail.com",
    license='MIT',
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'tox']},
)
