#!/usr/bin/python3
def safe_print_integer(value):
    while value in range(-1000, 1000):
        try:
            print("{:d}".format(value))
            return True
        except TypeError:
            return False
