""" Coffee and teapots. """
import flask


class Pot(object):

    def __init__(self, name):
        self.name = name

    def get(self):
        return are_you_a_teapot()

    def when(self):
        return are_you_a_teapot()

    def brew(self):
        return are_you_a_teapot()


def are_you_a_teapot():
    flask.abort(418)
