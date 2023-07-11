#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted."""

    def __eq__(self, value):
        """== and != operators inverted."""
        return self.real != value

    def __ne__(self, value):
        """!= operator with ==."""
        return self.real == value
