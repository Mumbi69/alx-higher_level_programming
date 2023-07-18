#!/usr/bin/python3
"""Defines the square.py unittest"""


import unittest
import io
import sys
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Represents the unittest for class square"""
    def test_NoArgs(self):
        with self.assertRaises(TypeError):
            Square()

if __name__ == "__main__":
    unittest.main()
