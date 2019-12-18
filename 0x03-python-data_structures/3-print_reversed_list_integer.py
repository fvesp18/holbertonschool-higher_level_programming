#!/usr/bin/python3
""" prints list in reverse order """


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()

    if my_list:
        for i in my_list:
            print("{:d}".format(i))
