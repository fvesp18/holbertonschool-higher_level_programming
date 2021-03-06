#!/usr/bin/python3
""" create a base class """
from models.base import Base


class Rectangle(Base):
    """ create new class with inheritance from Base """
    width = 0
    height = 0
    x = 0
    y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area declaration """
        return self.width * self.height

    def display(self):
        """ displays rectangle with # """
        for spaces in range(self.y):
            print("")
        for offset in range(self.height):
            print("", end="")
            for i in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ string representation """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ declaration of update """
        if len(args) != 0 and args is not None:
            for position, arg in enumerate(args):
                if position is 0:
                    self.id = arg
                if position is 1:
                    self.width = arg
                if position is 2:
                    self.height = arg
                if position is 3:
                    self.x = arg
                if position is 4:
                    self.y = arg
        else:
            self.id = kwargs.get("id", self.id)
            self.height = kwargs.get("height", self.height)
            self.width = kwargs.get("width", self.width)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """ declaration of to_dictionary """
        new = {
                "id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
        return new
