#!/usr/bin/python3


def no_c(my_string):
    unacc = ["c", "C"]
    newstr = my_string

    newstr = newstr.translate({ord(i): None for i in unacc})

    return newstr
