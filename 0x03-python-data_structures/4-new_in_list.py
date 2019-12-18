#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0:
            return my_list
        if idx > len(my_list):
            return my_list
        if my_list[idx]:
            my_list.insert(idx, element)
            my_list.remove(idx + 1)
            return my_list
