#!/usr/bin/python3
""" prints chars to uppercase """


def uppercase(str):
    for ch in str:
        if (ord(ch) >= 97 and ord(ch) <= 122):
            ch = ord(ch) - 32
            print("{:s}".format(chr(ch)), end="")
        else:
            print("{:s}".format(ch), end="\n")