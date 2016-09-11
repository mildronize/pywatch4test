pywatch4test
============

|Build Status| |Coverage Status| |Updates|

A command line for instantly testing python codes when the file is
modified

Moved from https://github.com/mildronize/autotest

Features
--------

-  Use `watchdog <https://pypi.python.org/pypi/watchdog>`__ for watching
   python file in order to test using
   `nose <http://nose.readthedocs.io/>`__
-  Added coverage test when use flag ``--package-name``

Installation
------------

-  Install globally

   ::

       git clone https://github.com/mildronize/pywatch4test.git /tmp/pywatch4test
       cd /tmp/pywatch4test
       python setup.py install

-  Install in your project locally

   ::

       git submodule add https://github.com/mildronize/pywatch4test.git .pywatch4test
       pip install -r .pywatch4test/requirements.txt
       ln -sr .pywatch4test/bin/pywatch4test .

   -  For installing git submodule:
      ``git submodule update --init --recursive``
   -  For running: ``./pywatch4test``

Usage
-----

1. Make sure you create your tests structure like your project
   structure. Example:

   ::

       .
       ├── package_a
       │   ├── file_1.py
       │   ├── file_2.py
       │   └── package_b
       │       └── file_3.py
       └── tests
           ├── test_file_1.py
           ├── test_file_2.py
           └── package_b
               └── test_file_3.py

2. run the script: ``pywatch4test``

Options
-------

-  ``-d``, ``--unittest-dir`` : Where is tests directory (default:
   tests)
-  ``-p``, ``--package-name`` : The main package e.g. ``package_a`` if
   you don't add this flag, it won't enable coverage test.
-  ``-s``, ``--endswith-test``: ``pywatch4test`` supports 2 styles of
   naming tests

   1. ``test_*.py`` as a default
   2. ``*_test.py`` you need to enable this flag for using this style

CLI
---

::

    Usage: pywatch4test [OPTIONS]

      Console script for pywatch4test

    Options:
      -d, --unittest-dir TEXT  Where is tests directory?
      -p, --package-name TEXT  Your package name
      -s, --endswith-test      Naming styles, if enable this flag, pattern is
                               `*_test`
      --help                   Show this message and exit.

Credits
-------

This package was created with
`Cookiecutter <https://github.com/audreyr/cookiecutter>`__ and the
`audreyr/cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`__
project template.

License
-------

MIT license

.. |Build Status| image:: https://travis-ci.org/mildronize/pywatch4test.svg?branch=master
   :target: https://travis-ci.org/mildronize/pywatch4test
.. |Coverage Status| image:: https://coveralls.io/repos/github/mildronize/pywatch4test/badge.svg?branch=master
   :target: https://coveralls.io/github/mildronize/pywatch4test?branch=master
.. |Updates| image:: https://pyup.io/repos/github/mildronize/pywatch4test/shield.svg
   :target: https://pyup.io/repos/github/mildronize/pywatch4test/
