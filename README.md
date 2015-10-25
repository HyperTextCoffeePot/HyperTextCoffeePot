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


Installation
------------

```shell
apt-get install wiringpi
pip install -r requirements.txt
```


Run the server
--------------

```shell
gunicorn --worker-class gevent server:app
```

The server will be running on port 8000, you can use a command like this to make brew requests:

```shell
curl -X BREW http://localhost:8000/teapot
```


What to help?
-------------

Check out our `CONTRIBUTING` guidelines.
