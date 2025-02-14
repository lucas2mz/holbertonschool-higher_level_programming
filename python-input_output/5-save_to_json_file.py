#!/usr/bin/python3
"""
modulo
"""


import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
