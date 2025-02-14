#!/usr/bin/python3
"""
modulo
"""


def append_write(filename="", text=""):
    """
    append_write
    """
    with open(filename, 'a') as file:
        return file.write(text)
