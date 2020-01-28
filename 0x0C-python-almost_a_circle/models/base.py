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

    @classmethod
    def save_to_file(cls, list_objs):
        aList = []
        if list_objs is None:
            return []
        for aLine in list_objs:
            aList.append(aLine.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as aFile:
            aFile.write(cls.to_json_string(aList))
