HyperTextCoffeePot
==================

A real implementation of the Hyper Text Coffee Pot Control Protocol. Get a
cheap coffee pot, a programmable power strip, and a Raspberry Pi and you'll
have your own HTCPCP server.

Goals
-----

The goal of this project is to implement a complient HTCPCP server after the
[HTCPCP][1] protocol.

[1]: https://en.wikipedia.org/wiki/HTCPCP

Design
------

The overall design will involve a Flask server that communicates with a
`coffeed` daemon that actually controls the coffee/tea pot. Therefore, the Flask app should return responses immediately.

Design of the Flask app (at time or writing) is nearly complete and trivially
implemented. Implementation of the `coffeed` daemon is in the brainstorming
phase. Please checkout the issues for more information.

GPIO Library (RPi.GPIO)
-----

Installation
------------

Installation instructions were stolen from this writeup: [GPIO Library][2]

1. Download the library ($ wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.1.0.tar.gz)

2. Unarchive the tar ball ($ tar zxf RPi.GPIO-0.1.0.tar.gz)
3. Install GPIO Library

    a. $ cd RPi.GPIO-0.1.0
    
    b. $ sudo python setup.py install

[2]: http://openmicros.org/index.php/articles/94-ciseco-product-documentation/raspberry-pi/217-getting-started-with-raspberry-pi-gpio-and-python

What to help?
-------------

Check out our `CONTRIBUTING` guidelines.
