import unittest
from modules.calculator import *

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.first = 10
        self.second = 5
    # test math functions return correct results
    def test_add(self):
        self.assertEqual(15, add(self.first, self.second))

    def test_subtract(self):
        self.assertEqual(5, subtract(self.first, self.second))

    def test_divide(self):
        self.assertEqual(2.0, divide(self.first, self.second))
    
    def test_multiply(self):
        self.assertEqual(50, multiply(self.first, self.second))