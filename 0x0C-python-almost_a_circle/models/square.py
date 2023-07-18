#!/usr/bin/python3
"""Defines a class square that inerits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the attributes of the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        """Assigns attributes to the class square"""
        if len(args):
            for m, val in enumerate(args):
                if m == 0:
                    self.id = val
                elif m == 1:
                    self.size = val
                elif m == 2:
                    self.x = val
                elif m == 3:
                    self.y = val
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            elif "size" in kwargs:
                self.size = kwargs["size"]
            elif "x" in kwargs:
                self.x = kwargs["x"]
            elif "y" in kwargs:
                self.y = kwargs["y"]


    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
       }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
