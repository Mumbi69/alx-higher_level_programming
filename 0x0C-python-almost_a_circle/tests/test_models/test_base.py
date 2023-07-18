#!/usr/bin/python3
"""Defines the base.py unittest"""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Represents the unittest for Base class"""
    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

if __name__ == "__main__":
    unittest.main()
