from .IPet import IPet

class Dog(IPet):
    kind = 'canine'

    def __init__(self, name):
        super(Dog, self).__init__(name)

    def speak(self):
        """
        Issue 'speak' command:

        >>> from Pets.Dog import Dog
        >>> d = Dog('fido')
        >>> d.speak()
        ''
        >>> d.add_trick("speak")
        >>> d.speak()
        'woof'
        >>>
        """

        if("speak" in self._tricks):
            return "woof"
        return ""

if __name__ == "__main__":
    import doctest
    doctest.testmod()