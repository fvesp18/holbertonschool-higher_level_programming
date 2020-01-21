#!/usr/bin/python3
""" returns true if obj is exactly an instace of a specified class """


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
