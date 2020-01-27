#!/usr/bin/python3
""" create calss that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ initialize stuff """
    def __init__(self, size, x=0, y=0, id=None):
        """ load vars from Rect """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str decorator """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """ set size """
        return self.width

    @size.setter
    def size(self, value):
        """ size get """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """
        if len(args) is not 0 and args is not None:
            for position, arg in enumerate(args):
                if position is 0:
                    self.id = arg
                if position is 1:
                    self.__size = arg
                if position is 2:
                    self.x = arg
                if position is 3:
                    self.y = arg
        else:
            self.id = kwargs.get("id", self.id)
            self.__size = kwargs.get("size", self.__size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
