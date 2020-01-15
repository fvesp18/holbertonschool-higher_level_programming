#!/usr/bin/python3
""" Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py). """


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an intege")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        self.__area = self.__height * self.__width
        return self.__area

    def perimeter(self):
        if self.__width is 0 and self.__height is 0:
            self.__perimeter = 0
            return self.__perimeter
        self.__perimeter = 2 * (self.__width) + 2 * ( self.__height)
        return self.__perimeter