#!/usr/bin/python3
""" create calss that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ initialize stuff """
    def __init__(self, size, x=0, y=0, id=None):
        """ load vars from Rect """
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str decorator """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = self.__size = value
