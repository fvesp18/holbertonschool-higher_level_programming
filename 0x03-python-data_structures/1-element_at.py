#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    else:
        return my_list[idx]
