#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with the given size."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """"Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Comparision between two squares to see if they are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares are != in terms of area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """ Check if area of one square is < than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if area of a square is less than or equal to."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Checks if area of square is > than the other square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if area of a square is >= the other square."""
        return self.area() >= other.area()
