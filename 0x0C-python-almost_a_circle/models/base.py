#!/usr/bin/python3
"""Defines a class Base"""

import json
import csv
import turtle

class Base:
    """Represents the first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        return json_loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Serializes and deserializes in CVS"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangle and Square"""
        win = turtle.Screen()
        win.bgcolor("#e6ccff")
        win.title("Kidding")
        shelly = turtle.Turtle()
        shelly.shape("turtle")
        shelly.pensize(3)

        shelly.color('#b399ff')
        for rec in list_rectangles:
            shelly.showturtle()
            shelly.up()
            shelly.goto(rec.x, rec.y)
            shelly.down()
            for m in range(2):
                shelly.forward(rec.width)
                shelly.left(90)
                shelly.forward(rec.height)
                shelly.left(90)
            shelly.hideturtle()

        shelly.color('#660033')
        for squ in list_squares:
            shelly.showturtle()
            shelly.up()
            shelly.goto(squ.x, squ.y)
            shelly.down()
            for m in range(2):
                shelly.forward(squ.width)
                shelly.left(90)
                shelly.forward(squ.height)
                shelly.left(90)
            shelly.hideturtle()

        turtle.exitonclick()
