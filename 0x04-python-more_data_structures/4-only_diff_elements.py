#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    buff_1 = list(set_1)
    buff_2 = list(set_2)
    new = list(set(buff_1 + buff_2))
    return new
