#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)."""
    with open(filename, "w", encoding='utf-8') as f:
        nb_characters = f.write(text)
        return (nb_characters)
