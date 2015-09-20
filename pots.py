""" Coffee and teapots. """
import logging
import subprocess
import warnings

import flask
import gevent
import wiringpi2

logger = logging.getLogger()


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
    stop_task = None

    def __init__(self, name, brew_time, pin):
        super(RaspCoffeePot, self).__init__(name)
        self.gpio_pin = pin
        try:
            subprocess.check_call('gpio export {} out'.format(self.gpio_pin).split())
        except OSError:
            logger.warn('Not running in a Raspberry Pi environment or wiringpi is not installed. Continuing in simulation mode.')
            self.simulate = True
        else:
            wiringpi2.wiringPiSetupSys()
        self.busy = False
        self.brew_time = brew_time

    def brew(self):
        if flask.request.get_data().strip() == 'stop':
            if self.stop_task:
                self.stop_task.kill()
            return self.brew_stop()
        else:
            return self.brew_start()

    def brew_start(self):
        if self.busy:
            flask.abort(409)
        self.busy = True
        self.stop_task = gevent.spawn_later(self.brew_time, self.brew_stop)
        self.power_pot_on()
        return 'started brewing', 200

    def brew_stop(self):
        if not self.busy:
            flask.abort(409)
        self.busy = False
        self.power_pot_off()
        return 'stopped brewing', 200

    def power_pot_on(self):
        logger.debug('Power pot on.')
        if not self.simulate:
            wiringpi2.digitalWrite(self.gpio_pin, 1)

    def power_pot_off(self):
        logger.debug('Power pot off.')
        if not self.simulate:
            wiringpi2.digitalWrite(self.gpio_pin, 0)


def are_you_a_teapot():
    flask.abort(418)
