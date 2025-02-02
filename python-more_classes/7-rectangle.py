#!/usr/bin/python3
'''
This module defines a class Rectangle.
The Rectangle class represents a geometric rectangle object.
'''


class Rectangle:
    '''
    This class defines a rectangle.
    It currently has no attributes or methods.
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return ((2 * self.height) + (2 * self.width))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) * 
        self.width for _ in range(self.height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
