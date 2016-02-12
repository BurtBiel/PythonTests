import sys
import os

from Pets.Dog import Dog
import BingUtil.Bing as bing


print(sys.argv[1:])

d = Dog('Fido')
d.add_trick('roll over')
d.add_trick('speak')
print (d._tricks)

dir(os)

class Puppy(Dog):
    def __init__(self, name):
        return super().__init__(name)

p = Puppy("puppyName")
print (p._tricks)

