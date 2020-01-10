#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        my_list = [x for x in my_list if type(x) == int]
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        print("")
        return x
    except TypeError:
        return x
    except ValueError:
        print("")
        return i
    print("\n")
