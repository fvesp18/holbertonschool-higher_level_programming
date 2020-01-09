#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    try:
        new = [i / j for i, j in zip(my_list_1, my_list_2)]
        return new
    except TypeError:
        print("wrong type")
        return
    except ZeroDivisionError:
        print("division by 0")
        return
    return new
