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
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))
