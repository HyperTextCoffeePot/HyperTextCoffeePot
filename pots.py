""" Coffee and teapots. """
import subprocess

import flask
import trollius
import wiringpi2


class Pot(object):

    def __init__(self, name):
        self.name = name

    def get(self):
        return are_you_a_teapot()

    def when(self):
        return are_you_a_teapot()

    def brew(self):
        return are_you_a_teapot()


class RaspCoffeePot(Pot):
    gpio_pin = None
    busy = None
    brew_time = None

    def __init__(self, name, brew_time, pin):
        super(RaspCoffeePot, self).__init__(name)
        self.gpio_pin = pin
        subprocess.check_call('gpio export {} out'.format(self.gpio_pin).split())
        wiringpi2.wiringPiSetupSys()
        self.busy = False
        self.brew_time = brew_time

    def brew(self):
        if flask.request.get_data().strip() == 'stop':
            return self.brew_stop()
        else:
            return self.brew_start()

    def brew_start(self):
        if self.busy:
            flask.abort(409)
        self.busy = True
        trollius.get_event_loop().call_later(self.brew_time, self.brew_stop)
        wiringpi2.digitalWrite(self.gpio_pin, 1)
        return 'started brewing', 200

    def brew_stop(self):
        if not self.busy:
            flask.abort(409)
        self.busy = False
        wiringpi2.digitalWrite(self.gpio_pin, 0)
        return 'stopped brewing', 200


def are_you_a_teapot():
    flask.abort(418)
