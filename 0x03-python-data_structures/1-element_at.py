#!/usr/bin/python3
""" program prints element from list at idx """


def element_at(my_list, idx):
    """ compares i to len(my_list) """
    i = 0
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    else:
        while i < idx:
            i = i + 1
            if i == idx:
                return my_list[i]
