#!/usr/bin/python3
"""Unittest fot max_integer."""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """My testcase that inherits from unittest.Testcase"""

    def test_ordered_list(self):
        """Test an ordered list of int."""
        ordered = [1, 2, 3]
        self.assertEqual(max_integer(ordered), 3)

    def test_empty_list(self):
        """Test if the list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_argument(self):
        """Tests when only one argument is passed"""
        One = [4]
        self.assertEqual(max_integer(One), 4)

    def test_unordered(self):
        """Test if the list is unordered"""
        unordered = [10, 20, 40, 30]
        self.assertEqual(max_integer(unordered), 40)

    def test_max_start(self):
        """Tests a max integer at the beginning of list"""
        max = [40, 30, 20, 10]
        self.assertEqual(max_integer(max), 40)

    def test_floats(self):
        """Tests a list of floats for max"""
        float = [1.0, 2.0, 3.0, 4.0, 5.5]
        self.assertEqual(max_integer(float), 5.5)

    def test_max_end(self):
        """Tests for a maximum integer at the end"""
        end = [10, 20, 30, 40]
        self.assertEqual(max_integer(end), 40)

    def test_max_middle(self):
        """Tests when max is in the middle"""
        middle = [1, 2, 8, 3, 4]
        self.assertEqual(max_integer(middle), 8)

    def test_negative_max(self):
        """Tests when max are all negative"""
        negative = [-10, -20, -30]
        self.assertEqual(max_integer(negative), -10)

if __name__ == '__main__':
    unittest.main()
