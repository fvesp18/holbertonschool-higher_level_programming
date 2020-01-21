#!/usr/bin/python3
""" returns true if obj is exactly an instace of a specified class """


def inherits_from(obj, a_class):
    if not issubclass(a_class, type(obj)):
        return True
    else:
        return False
