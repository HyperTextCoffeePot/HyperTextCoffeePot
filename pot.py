""" A sample coffee or tea pot. """


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
    return 'I am a teapot.\n', 418






