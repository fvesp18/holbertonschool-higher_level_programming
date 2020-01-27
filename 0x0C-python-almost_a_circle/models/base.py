#!/usr/bin/python3
""" creates a base class """
import json


class Base:
    """ define class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ some doc """
        if list_dictionaries is None:
            return "[]"
        elif list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
