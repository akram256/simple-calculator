import unittest
from calculator import *

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class TestCalculator(unittest.TestCase):

    # Create an instance of the calculator that can be used in all tests
    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.calc = Calculator()

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    # Write test methods for subtract, multiply, and divide
    def test_add(self):
        pass

    def test_subtract(self):
        pass

    def test_multiply(self):
        pass

    def test_divide(self):
        pass
      


if __name__ == '__main__':
    unittest.main()