import unittest
from unittest.mock import MagicMock
from Pets.Cat import Cat

class CatTest_Test1(unittest.TestCase):
    def test_cat_learns_tricks(self):
        d = Cat('fido')
        d.add_trick("trick1")
        d.add_trick("trick2")
        self.assertEqual(len(d.get_tricks()), 2)

    def test_cat_always_passes(self):
        print("testB")

if __name__ == '__main__':
    unittest.main()