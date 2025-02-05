#!/usr/bin/python3
"""
This module define a MyList class
the class MyList print a sorted list
"""


class MyList(list):
    """
This class inherits from the built-in Python list class.
It adds a method to print the list in ascending order without modifying the original list.
    """
    def print_sorted(self):
        print(sorted(self))
