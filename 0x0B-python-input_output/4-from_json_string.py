#!/usr/bin/python3
"""Defines an object respresented by a JSON string"""


import json
"""Imports json data interchange format"""


def from_json_string(my_str):
    """Representation of an object by a json string"""
    return json.loads(my_str)
