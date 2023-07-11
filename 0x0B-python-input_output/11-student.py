#!/usr/bin/python3
"""Defines a class student."""


class Student:
    """Represents a class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of a student."""
        for m, s in json.items():
            setattr(self, m, s)
