#!/usr/bin/python3
"""Defines the rectangle.py unittest"""


import sys
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Represents the unittest for class Rectangle"""
    def test_OneArg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

if __name__ == "__main__":
    unittest.main()
