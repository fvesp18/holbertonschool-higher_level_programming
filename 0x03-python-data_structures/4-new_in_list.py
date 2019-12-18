#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    my_list.copy()
    if my_list:
        if idx < 0:
            return my_list
        if idx >= len(my_list) - 1:
            return my_list
        if new_list[idx]:
            new_list.remove(idx + 1)
            new_list.insert(idx, element)
            return new_list
