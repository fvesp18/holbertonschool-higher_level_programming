#!/usr/bin/python3
""" ADD INTEGERS """


def add_integer(a, b=98):
    """
    RETURNS ADDITION OF A AND B AS INTEGER.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "Holberton")
    Traceback:

    PARAMETERS: 
        A: SOME INTEGER
        B: 98
    """
    if type(a) is not (int, float):
        raise TypeError("a must be an integer")
    if type(b) is not (int, float):
        raise TypeErrpr("b must be an integer")
    return int(a) + int(b)
