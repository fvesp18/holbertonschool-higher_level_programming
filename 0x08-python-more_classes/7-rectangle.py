#!/usr/bin/python3
""" creates public class attribute """


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        self.number_of_instances += 1
        self.print_symbol
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
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width) + 2 * (self.__height)
    
    def __str__(self):
        rec_rep = ''
        if self.__width is 0 or self.__height is 0:
            return ''
        else:
            for i in range(self.__height):
                rec_rep += (str(self.print_symbol)) * (self.__width) + ('\n')
            return rec_rep[:-1]
    def __repr__(self):
        return 'Rectangle(%d, %d)' % (self.__width, self.__height)
    def __del__(self):
        self.number_of_instances -= 1
        print("Bye rectangle...")
