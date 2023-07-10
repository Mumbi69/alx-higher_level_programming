#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """raises an ExceptionError message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
