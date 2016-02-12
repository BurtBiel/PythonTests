class IPet(object):
    kind = 'abstract'
    
    def __init__(self, name):
        self._name = name
        self._tricks = []

    def add_trick(self, trickName):
        self._tricks.append(trickName)

    def get_tricks(self):
        return self._tricks.copy()
