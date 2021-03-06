#!/usr/bin/env python3
import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exponent(self):
        result = rpn.calculate("3 3 ^")
        self.assertEqual(27, result)
    def test_exponent2(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)
    def test_exponent3(self):
        result = rpn.calculate("4 1 ^")
        self.assertEqual(4, result)        
    def test_modulo(self):
        result = rpn.calculate("1 2 %")
        self.assertEqual(1, result)
    def test_modulo2(self):
        result = rpn.calculate("2 2 %")
        self.assertEqual(0, result)
        
if __name__ == '__main__':
    unittest.main()
