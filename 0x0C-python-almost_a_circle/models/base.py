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
        """ save to file """
        aList = []
        if list_objs is not None:
            for aLine in list_objs:
                aList.append(aLine.to_dictionary())

        with open("{}.json".format(cls.__name__), "w") as aFile:
            aFile.write(cls.to_json_string(aList))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        if json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            anInstance = cls(1, 1)
            anInstance.update(**dictionary)
            return anInstance
        if cls.__name__ is "Square":
            anInstance = cls(1)
            anInstnace.update(**dictionary)
            return anInstance
        return None
