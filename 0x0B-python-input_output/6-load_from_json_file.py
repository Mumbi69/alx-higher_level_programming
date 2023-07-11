#!/usr/bin/python3
"""Defines an object from "JSON file": """


import json
"""Imports json"""


def load_from_json_file(filename):
    """Represents  a function that creates an Object from a “JSON file”:"""
    with open(filename) as f:
        return json.load(f)
