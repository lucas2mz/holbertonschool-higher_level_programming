#!/usr/bin/python3
"""
modulo
"""


def read_file(filename=""):
    """
    read_file
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
