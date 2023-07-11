#!/usr/bin/python3
    """Defines a text-file reading function."""


    def read_file(filename=""):
        """reads a text file (UTF8) and prints it to stdout:"""

        with open(filename, "r", encoding="utf-8") as f:
            """reads a text file (UTF8) and prints it to stdout."""
            for line in f:
                print(line, end='')
