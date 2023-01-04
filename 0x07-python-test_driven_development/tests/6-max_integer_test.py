#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_return(self):
        # Test the correct return of a max int in a list
        self.assertEqual(max_integer([1, 2, 3, 5, 4, 6, 8]), 8)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([6, 3, 5, 3]), 6)
        self.assertEqual(max_integer([-4, 5, 1, -8]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -5]), -1)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)
