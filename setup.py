# -*- coding:utf8 -*-
# Author: JohnHerry
# Mail: qhlonline@163.com
# Desc: setup file


from setuptools import setup

setup(
    name='POC',
    version='1.0.0',
    author='JohnHerry',
    author_email='qhlonline@163.com',
    description='ordered concurrency of python coroutines',
    keywords='python, coroutine, concurrent, order',
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires='>=3.6'
)
