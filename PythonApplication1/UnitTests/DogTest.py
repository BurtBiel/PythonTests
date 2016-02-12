import unittest
from unittest.mock import MagicMock
from Pets.Dog import Dog

class DogTest_Test1(unittest.TestCase):
    def test_dog_learns_tricks(self):
        d = Dog('fido')
        d.add_trick("trick1")
        d.add_trick("trick2")
        self.assertEqual(len(d.get_tricks()), 2)

    def test_dog_always_passes(self):
        print("testB")

if __name__ == '__main__':
    unittest.main()