#!/usr/bin/python3
'''
module
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    '''
    class
    '''
    def __init__(self, width, height):
        if integer_validator(width) == True:
            self.__width = width
        if integer_validator(height) == True:
            self.__height = height
