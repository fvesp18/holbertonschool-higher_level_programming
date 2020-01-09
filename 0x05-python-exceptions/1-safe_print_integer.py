#!/usr/bin/python3
def safe_print_integer(value):
    while isinstance(value, int):
        try:
            print("{:d}".format(value))
            return True
        except TypeError:
            return False
