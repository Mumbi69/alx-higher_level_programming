#!/usr/bin/python3
"""Defines JSON serialization of an object."""


def class_to_json(obj):
    """Represents a function that returns the dictionary description"""
    return obj.__dict__
