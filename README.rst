yedis
========

The Python interface to the Redis key-value store, extended to support additional features from YugaByteDB.

This has been forked from https://github.com/andymccurdy/redis-py and is intended to be
used against the Yedis API end point of YugaByteDB. This client also supports additional
commands (such as the time-series related commands) for use againist YugaByte DB that
are not part of the official Redis API.

Please refer to `YugaByte DB docs <https://docs.yugabyte.com/>`_ for reference.


Installation
------------

yedis requires a running YugaByteDB instance listening on the YEDIS end point, or a normal Redis server. See `YugaByteDB quickstart <https://docs.yugabyte.com/v1.0/quick-start/install/>`_ or `Redis's quickstart
<http://redis.io/topics/quickstart>`_ for installation instructions.

To install yedis, simply:

.. code-block:: bash

    $ sudo pip install yedis

or alternatively (you really should be using pip though):

.. code-block:: bash

    $ sudo easy_install yedis

or from source:

.. code-block:: bash

    $ sudo python setup.py install


Getting Started
---------------

.. code-block:: pycon

    >>> import redis
    >>> r = redis.StrictRedis(host='localhost', port=6379, db=0)
    >>> r.set('foo', 'bar')
    True
    >>> r.get('foo')
    'bar'

By default, all responses are returned as `bytes` in Python 3 and `str` in
Python 2. The user is responsible for decoding to Python 3 strings or Python 2
unicode objects.

If **all** string responses from a client should be decoded, the user can
specify `decode_responses=True` to `StrictRedis.__init__`. In this case, any
Redis command that returns a string type will be decoded with the `encoding`
specified.

API Reference
-------------
Please refer to `YugaByte API Refernce <https://docs.yugabyte.com/latest/api/>`_ for details on
the commmands that Yugabyte's YEDIS end point supports.
For other use cases, the `official Redis command documentation <http://redis.io/commands>`_ does a
great job of explaining each command in detail.

yedis is forked off redis-py, please refer to
https://github.com/andymccurdy/redis-py for the details of the implementation and limitations.

Author
^^^^^^

yedis is based on a fork of redis-py, extended to support the additional
commands for use against YugaByteDB's YEDIS API end point.

redis-py is developed and maintained by Andy McCurdy (sedrik@gmail.com).
It can be found here: http://github.com/andymccurdy/redis-py

