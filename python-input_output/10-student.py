#!/usr/bin/python3
"""
modulo
"""


class Student:
    """
    class student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {key: V for key, V in self.__dict__.items() if key in attrs}
