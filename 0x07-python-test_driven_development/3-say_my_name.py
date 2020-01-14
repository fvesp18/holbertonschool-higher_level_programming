#!/usr/bin/python3
""" PRINTS STRING WITH QUOTE """


def say_my_name(first_name, last_name=""):
    if type(first_name) is int:
        raise TypeError("first_name must be a string")

    if type(last_name) is int:
        raise TypeError("last_name must be a string")

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    if type(first_name) is None:
        raise TypeError("first_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
