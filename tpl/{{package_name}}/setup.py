# -*- coding:utf-8 -*-

import os
from setuptools import find_packages, setup

PRJECT_DIR = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(PRJECT_DIR, 'README.md')).read()
REQUIREMENTS = [requirement.strip() for requirement in
                open(os.path.join(PRJECT_DIR, 'requirements.txt')).read().split('\n') if requirement.strip()]

setup(
    name='{{package_name}}',
    description='{{description}}',
    long_description=README,
    author='{{author}}',
    packages=find_packages(exclude=['tests']),
    install_requires=REQUIREMENTS,
    py_modules=['cli'],
    entry_points={
        'console_scripts': ['{{package_name}}=cli:{{package_name}}'],
    },
    zip_safe=True,
    license='{{license}}',
    classifiers={{classifiers}}
)