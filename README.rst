pywatch4test
============

|Build Status| |Updates|

A command line for instantly testing python codes when the file is
modified

Moved from https://github.com/mildronize/autotest

Features
--------

-  Use `watchdog <https://pypi.python.org/pypi/watchdog>`__ for watching
   python file in order to test using
   `nose <http://nose.readthedocs.io/>`__

Installation
------------

::

    git clone https://github.com/mildronize/pywatch4test.git /tmp/pywatch4test
    cd /tmp/pywatch4test
    python setup.py install

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
.. |Updates| image:: https://pyup.io/repos/github/mildronize/pywatch4test/shield.svg
   :target: https://pyup.io/repos/github/mildronize/pywatch4test/
