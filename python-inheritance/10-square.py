#!/usr/bin/python3
'''
module
'''


BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(BaseGeometry):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return size * size
