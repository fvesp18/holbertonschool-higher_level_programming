#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0:
        return None
    else:
        while i < idx:
            i = i + 1
            if idx > len(my_list):
                return None
            elif i == idx:
                return my_list[i]
