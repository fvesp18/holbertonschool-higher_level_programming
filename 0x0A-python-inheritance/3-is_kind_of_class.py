#!/usr/bin/python3
""" returns true if obj is exactly an instace of a specified class """


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
