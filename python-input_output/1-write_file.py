#!/usr/bin/python3
"""
modulo
"""


def write_file(filename="", text=""):
    """
    write_file
    """
    with open(filename, 'w') as file:
        return file.write(text)
