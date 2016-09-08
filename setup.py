#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'nose==1.3.7',
    'rednose==1.2.1',
    'coverage==4.2',
    'watchdog==0.8.3',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pywatch4test',
    version='0.1.0',
    description="Auto test script ( watchdog + nose ) for TDD ( with test )",
    long_description=readme + '\n\n' + history,
    author="Thada Wangthammang",
    author_email='mildronize@gmail.com',
    url='https://github.com/mildronize/pywatch4test',
    packages=[
        'pywatch4test',
    ],
    package_dir={'pywatch4test':
                 'pywatch4test'},
    entry_points={
        'console_scripts': [
            'pywatch4test=pywatch4test.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pywatch4test',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
