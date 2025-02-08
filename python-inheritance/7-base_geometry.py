#!/usr/bin/python3
'''
module
'''


class BaseGeometry:
    '''
    class
    '''
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name if name else '<unnamed>'} must be an integer")
        if value <= 0:
            raise ValueError(f"{name if name else '<unnamed>'} must be greater than 0")
