import unittest
import doctest
import Pets

class DogTest_Test1(unittest.TestCase):
    def test_Dog_docs(self):
        self.assertEqual(doctest.testfile(r"..\Pets\Dog.py")[0], 0, "Doc tests failed")

if __name__ == '__main__':
    unittest.main()