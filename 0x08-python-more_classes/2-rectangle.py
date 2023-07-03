#!/usr/bin/python3
"""Defines the rectangle"""


class Rectangle:
    """Represents the triangle"""

    def __init__(self, width=0, height=0):
        """Initialize the height and width of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculates the perimeter of the rectangle."""
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Represents the rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for m in range(self.__height):
            [rec.append('#') for s in range(self.__width)]
            if m != self.height - 1:
                rec.append("\n")
        return ("".join(rec))
