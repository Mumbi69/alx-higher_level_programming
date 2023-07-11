#!/usr/bin/python3
"""Defines an object to a text file."""


import json
"""Imports json data interchange format"""


def save_to_json_file(my_obj, filename):
    """Representation of JSON writing an object to a textfile"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
