import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_subt(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)

    def test_mult(self):
        result = rpn.calculate('7 3 -')
        self.assertEqual(21, result)

    def test_div(self):
        result = rpn.calculate('8 2 /')
        self.assertEqual(4, result)

    def test_neg(self):
        result = rpn.calculate('-4 -3 -')
        self.assertEqual(-1, result)

    def test_exp(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)
