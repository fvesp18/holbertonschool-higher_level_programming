#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            if i == idx + 1:
                return i
