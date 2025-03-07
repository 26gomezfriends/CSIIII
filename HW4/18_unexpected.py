import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)

def divide(a, b):
    return a / b

class TestUnexpected(unittest.TestCase):
    # Test get_sqrt with a positive number
    def test_get_sqrt_valid(self):
        self.assertEqual(get_sqrt(144), 12)
    
    # Test get_sqrt with a negative number
    def test_get_sqrt_negative(self):
        with self.assertRaises(ValueError):
            get_sqrt(-1)
    
    # Test divide with valid numbers
    def test_divide_valid(self):
        self.assertEqual(divide(144, 12), 12)
    
    # Test divide by zero
    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(144, 0)

if __name__ == '__main__':
    unittest.main()
