#!/usr/bin/python3
"""
modulo
"""


import json


def load_from_json_file(filename):
    """
    load_from_json_file
    """
    with open(filename, 'r') as file:
        return json.load(file)
