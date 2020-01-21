#!/usr/bin/python3
""" returns true if obj is exactly an instace of a specified class """


def is_same_class(obj, a_class):
    if issubclass(a_class, type(obj)) is True:
        return True
    else:
        return False
