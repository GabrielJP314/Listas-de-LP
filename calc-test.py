import unittest
from calc import *

class CalcTest(unittest.TestCase):
    def test_add_int(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add_float(self):
        self.assertEqual(add(10.5, 2), 12.5)
        
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract_int(self):
        self.assertEqual(subtract(1, 2), -1)
        
    def test_subtract_float(self):
        self.assertEqual(subtract(10.5, 2), 8.5)
        
    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 0), 0)
        
    def test_multiply_int(self):
        self.assertEqual(multiply(1, 2), 2)
        
    def test_multiply_float(self):
        self.assertEqual(multiply(10.5, 2), 21)
        
    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 0), 0)
        
    def test_divide_int(self):
        self.assertEqual(divide(1, 2), 0.5)
        
    def test_divide_float(self):
        self.assertEqual(divide(10.5, 2), 5.25)
        
    def test_divide_zero(self):
        self.assertRaises(ValueError, divide, 1, 0)
        
    def test_exp_int(self):
        self.assertEqual(exp(2,2), 4)
        
    def test_exp_float(self):
        self.assertEqual(exp(2.5,2), 5.656854249492381)
        
    def test_exp_zero(self):
        self.assertEqual(exp(0, 0), 1)
      
if __name__ == '__main__':
    unittest.main(verbosity=2)          