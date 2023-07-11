#!/usr/bin/python3
"""Defines a string appended at the end of a text."""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""
    with open(filename, "a", encoding='utf-8') as f:
        nb_characters_added = f.write(text)
        return (nb_characters_added)
