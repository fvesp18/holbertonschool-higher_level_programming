#!/usr/bin/python3
def safe_print_integer(value):
    try:
        while isinstance(value, int):
            print("{:d}".format(value))
            return True
    except TypeError:
        return False
