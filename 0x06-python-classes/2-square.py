#!/usr/bin/python3
""" creates class Square """


class Square:
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size

        def area(self):
            return self.__size*self.__size
