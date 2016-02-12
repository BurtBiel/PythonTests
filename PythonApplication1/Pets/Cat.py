from .IPet import IPet

class Cat(IPet):
    kind = 'canine'

    def __init__(self, name):
        super(Cat, self).__init__(name)
